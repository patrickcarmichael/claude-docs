---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## These are all the same answer but look different:

response_1 = "The answer is 42 dollars"
response_2 = "[RESULT]\n42\n[/RESULT]"  
response_3 = "Therefore, the total is $42.00"
response_4 = "\\boxed{42}"
```

We need evaluation tools that can:

* Extract answers from any response format
* Normalize numbers (handle commas, decimals, currency)
* Track multiple metrics (accuracy, extraction success)

**Building Our Evaluation System**

Let's build two essential functions that will power our model comparisons:

**Answer Extraction Engine**
```python
def extract_answer(text: str) -> Optional[str]:
    """
    Answer extraction that tries multiple methods
    """
    # Method 0: [RESULT] tags (primary method for our SFT model)

    result_match = re.search(r'\[RESULT\](.*?)\[/RESULT\]', text, re.DOTALL)
    if result_match:
        answer = result_match.group(1).strip()
        number = extract_number_from_text(answer)
        if number:
            return number

    # Method 1: <answer> tags

    answer_tag_match = re.search(r'<answer>\s*(.*?)\s*</answer>', text, re.IGNORECASE | re.DOTALL)
    if answer_tag_match:
        answer = answer_tag_match.group(1).strip()
        number = extract_number_from_text(answer)
        if number:
            return number

    # Method 2: \\boxed{} format

    boxed_match = re.search(r'\\boxed\{([^}]+)\}', text)
    if boxed_match:
        number = extract_number_from_text(boxed_match.group(1))
        if number:
            return number

    # Method 3: Last number in the entire text

    all_numbers = re.findall(r'\b(\d+(?:,\d{3})*(?:\.\d+)?)\b', text)
    if all_numbers:
        # Filter out small numbers that might be step numbers

        significant_numbers = [n for n in all_numbers if float(n.replace(',', '')) >= 1]
        if significant_numbers:
            return clean_number(significant_numbers[-1])

    # Method 4: "Therefore" or conclusion patterns

    conclusion_patterns = [
        r'[Tt]herefore,?\s+.*?(\d+(?:,\d{3})*(?:\.\d+)?)',
        r'[Ss]o,?\s+.*?(\d+(?:,\d{3})*(?:\.\d+)?)',
        r'[Tt]hus,?\s+.*?(\d+(?:,\d{3})*(?:\.\d+)?)',
        r'[Ii]n total,?\s+.*?(\d+(?:,\d{3})*(?:\.\d+)?)',
        r'[Aa]ltogether,?\s+.*?(\d+(?:,\d{3})*(?:\.\d+)?)',
    ]

    for pattern in conclusion_patterns:
        matches = re.findall(pattern, text)
        if matches:
            return clean_number(matches[-1])  # Take the last match

    # Method 5: "The answer is" patterns

    answer_is_patterns = [
        r'[Tt]he answer is\s+(\d+(?:,\d{3})*(?:\.\d+)?)',
        r'[Aa]nswer:\s*(\d+(?:,\d{3})*(?:\.\d+)?)',
        r'[Ff]inal answer:\s*(\d+(?:,\d{3})*(?:\.\d+)?)',
    ]

    for pattern in answer_is_patterns:
        match = re.search(pattern, text)
        if match:
            return clean_number(match.group(1))

    # Method 6: Numbers at the end of sentences

    sentences = text.split('.')
    for sentence in reversed(sentences[-3:]):  # Check last 3 sentences

        numbers = re.findall(r'\b(\d+(?:,\d{3})*(?:\.\d+)?)\b', sentence)
        if numbers:
            return clean_number(numbers[-1])

    return None

def extract_number_from_text(text: str) -> Optional[str]:
    """Extract the main number from a piece of text"""
    # Look for numbers, prioritizing larger ones

    numbers = re.findall(r'\b(\d+(?:,\d{3})*(?:\.\d+)?)\b', text)
    if numbers:
        return clean_number(numbers[-1])  # Take the last/most significant number

    return None

def clean_number(number_str: str) -> str:
    """Clean and normalize number string"""
    # Remove commas and extra whitespace

    cleaned = number_str.replace(',', '').strip()

    # Convert to int if it's a whole number

    try:
        if '.' in cleaned:
            float_val = float(cleaned)
            if float_val.is_integer():
                return str(int(float_val))
            else:
                return str(float_val)
        else:
            return str(int(cleaned))
    except ValueError:
        return cleaned
```

**Evaluation System**
```python
def evaluate_model(MODEL, deployment_id, problems):
    """Evaluate model"""

    results = []
    correct = 0
    total = 0
    extraction_failures = 0

    for i in range(0, len(problems)):
      problem = problems[i]

      # Get model response

      llm = LLM(
        model=MODEL,
        deployment_type="on-demand",
        id=deployment_id  # The deployment ID that already exists

      )

      response = llm.chat.completions.create(
          messages=[{"role": "user", "content": problem["question"]}]
      )
      model_response = response.choices[0].message.content
      model_answer = extract_answer(model_response)  # Use answer extraction

      ground_truth = problem["ground_truth"]

      # Track extraction failures

      if model_answer is None:
          extraction_failures += 1

      # Check correctness (only if we extracted something)

      is_correct = model_answer == ground_truth if model_answer else False
      if is_correct:
          correct += 1
      total += 1

    accuracy = correct / total if total > 0 else 0

    return accuracy
```

### Test Model Performance

```python
base_accuracy = evaluate_model(
    "qwen2p5-7b",
    "kd-base-model",
    gsm8k_test_problems
)

rft_accuracy = evaluate_model(
    "<rft-model-output-name>", # Replace <rft-model-output-name> with the model ID from your completed fine-tuning job

    "kd_rft_model",
    gsm8k_test_problems
)
```

### Actual Results Analysis

```
ACCURACY PROGRESSION:
Base Model:  52%
→ RFT:       70% (+18pp)
Total Gain:  +18 percentage point improvement

FORMAT COMPLIANCE:
SFT Model:  ~95% use [WORK]/[RESULT] format automatically  
RFT Model:  ~95% maintain format + higher accuracy
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
