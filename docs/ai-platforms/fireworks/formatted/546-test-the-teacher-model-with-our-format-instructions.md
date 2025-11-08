---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Test the teacher model with our format instructions

sample_question = "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much does she make every day at the farmers' market?"

messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": sample_question}]

teacher_llm = LLM(model="deepseek-v3", deployment_type="serverless")

teacher_response = teacher_llm.chat.completions.create(
    messages=messages
)

teacher_response.choices[0].message.content
```

**Actual teacher model response:**
```json
[WORK]
1. Janet's ducks lay 16 eggs per day.
2. She eats 3 eggs for breakfast daily.
3. She uses 4 eggs for baking muffins daily.
4. Total eggs used or consumed: \(3 + 4 = 7\)
5. Eggs remaining for sale: \(16 - 7 = 9\)
6. Price per egg: \$2
7. Daily earnings at the farmers' market: \(9 \times 2 = 18\)
[/WORK]

[RESULT]
18
[/RESULT]
```

### Generating High-Quality Training Data

**The Process**:

1. Take problems from GSM8K training set
2. Have teacher model solve them using our format
3. Verify teacher got the right answer
4. Create training examples from successful solutions
```python
def extract_answer_from_result_tags(response: str) -> str:
    """Extract answer from [RESULT] tags"""
    result_match = re.search(r'\[RESULT\](.*?)\[/RESULT\]', response, re.DOTALL)
    if result_match:
        return result_match.group(1).strip()
    return None

def generate_sft_training_data(train_problems_sample):
    """Generate training data using teacher model with format instructions"""

    sft_dataset = []
    successful_examples = 0

    for i, problem in enumerate(train_problems_sample):

        # Get teacher response with format instructions

        messages = [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": problem["question"]}]

        teacher_llm = LLM(model="deepseek-v3", deployment_type="serverless")

        teacher_response_obj = teacher_llm.chat.completions.create(
            messages=messages
        )

        teacher_response = teacher_response_obj.choices[0].message.content

        # Check if teacher got the right answer

        teacher_answer = extract_answer_from_result_tags(teacher_response)

        # Only include if teacher got the answer right AND used proper format

        if teacher_answer == problem["ground_truth"] and "[WORK]" in teacher_response and "[RESULT]" in teacher_response:
            # Don't include system prompt in training data so model learns

            # that the format should be followed even when not in system prompt

            training_example = {
                "messages": [
                    {"role": "user", "content": problem["question"]},
                    {"role": "assistant", "content": teacher_response}
                ]
            }
            sft_dataset.append(training_example)
            successful_examples += 1

    return sft_dataset, successful_examples

random.seed(42)
sampled_problems = random.sample(gsm8k_train_problems, 6000)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
