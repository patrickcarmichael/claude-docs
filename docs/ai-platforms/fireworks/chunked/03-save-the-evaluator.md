**Navigation:** [← Previous](./02-with-display-name-and-description.md) | [Index](./index.md) | [Next →](./04-7-report-results.md)

---

# Save the evaluator
rft_evaluator_filename = "kd-rft-evaluator.py"
with open(rft_evaluator_filename, 'w') as f:
    f.write(rft_evaluator_code)
```

### Setting Up RFT Training (Manual Dashboard Configuration)

Due to the complexity of reinforcement learning setup, we'll use the Fireworks dashboard for the final configuration steps.

#### Step 1: Upload the RFT Evaluator

1. **Navigate to Evaluators**
   * Go to [https://app.fireworks.ai/dashboard/evaluations](https://app.fireworks.ai/dashboard/evaluations)

2. **Create New Evaluator**
   * Click **"Create Evaluator"**
   * **Evaluator Name**: `kd-rft-evaluator`

3. **Configure Dataset**
   * Select **"Select an existing dataset"**
   * Choose the `kd-rft-dataset` you uploaded earlier

4. **Add Evaluator Code**
   * Choose **"Start from scratch"**
   * Click **"Next"**
   * In the code editor, delete any existing code
   * Copy and paste the complete code from `kd-rft-evaluator.py`

5. **Save Evaluator**
   * Click **"Save Evaluator"**
   * Your evaluator is now ready for RFT training

#### Step 2: Create RFT Training Job

1. **Navigate to Fine-Tuning**
   * Go to the **Fine-Tuning** tab in the dashboard
   * Click **"Fine-Tune a Model"**
   * Select **"Reinforcement"** tab

2. **Configure Training Job**

   **Model Selection:**

   * Select your SFT-trained model
   * Use `job.output_model` from your SFT job to obtain SFT model name (e.g., `accounts/your-account/models/kd-sft-model`)

   **Dataset:**

   * Select `kd-rft-dataset` from the dropdown

   **Evaluator:**

   * Select `kd-rft-evaluator` (the one you just created)

   **Training Settings:**

   * **Rollout Settings**: Leave as default values
   * **Model Output Name**:
     * Option 1: Leave blank for auto-generated name
     * Option 2: Enter custom name (e.g., `kd-rft-model`)
   * **Other Hyperparameters**: Leave as defaults

3. **Launch Training**
   * Review your configuration
   * Click **"Create Job"**
   * **Important**: Note the output model name for evaluation later

4. **Monitoring**

* Track progress in the dashboard's [Fine Tuning section](https://app.fireworks.ai/dashboard/fine-tuning).
* Once the job status is `Completed`, you can deploy your model.

### Deploying the Fine-Tuned Model

```python  theme={null}
rft_llm = LLM(
    model="<rft-model-output-name>", # Replace <rft-model-output-name> with the model ID from your completed fine-tuning job
    deployment_type="on-demand",
    id="kd-rft-model",
    min_replica_count=0,
    max_replica_count=1
)
rft_llm.apply()
```

## Chapter 7: Evaluate Complete Knowledge Distillation Pipeline

Now that we've completed our knowledge distillation pipeline, it's time to evaluate our results. But first, we need robust evaluation tools that can handle the complexity of comparing different models fairly.

**Why We Need Sophisticated Evaluation Tools**

The Challenge: We now have models that may respond in different formats:

* Baseline model: Natural language, inconsistent formatting
* RFT model: Structured \[WORK]/\[RESULT] format

**The Problem**: Simple string matching won't work because:

```
# These are all the same answer but look different:
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

```python  theme={null}
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

```python  theme={null}
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

```python  theme={null}
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

## Course Summary and Key Takeaways

### What We Demonstrated

**1. SFT for Internalized Format Learning**:

* **Training Strategy**: Include format examples without system prompts in training data
* **Testing Strategy**: No system prompts needed - format is internalized
* **Result**: Model automatically uses `[WORK]/[RESULT]` structure as default behavior
* **Key Insight**: SFT teaches "how to respond" by making patterns the model's natural behavior

**2. RFT for Accuracy Improvement**:

* **Foundation**: Builds on SFT model
* **Optimization**: Reward-based learning improves content quality
* **Result**: Significantly improves reasoning accuracy
* **Key Insight**: RFT optimizes "what to respond with"

**3. Two-Stage Pipeline Synergy**:

* **Stage 1 (SFT)**: Establishes reliable, consistent response structure
* **Stage 2 (RFT)**: Optimizes content quality within that structure
* **Combined Result**: Models that are both well-formatted AND accurate

### Practical Applications

This knowledge distillation approach is valuable for:

* **API Integrations**: Reliable output parsing + improved accuracy
* **Structured Reasoning Tasks**: Clear thinking process + better results
* **Production Pipelines**: Consistent format + higher quality content
* **Evaluation Systems**: Easy answer extraction + improved performance
* **Cost Optimization**: Small models with large model capabilities

### Expected Resources

* **Cost**: \~Costs apply for API calls, deployments and training jobs

## Conclusion

This tutorial demonstrated how to systematically apply knowledge distillation using [Fireworks AI](https://app.fireworks.ai/account/home) to create models that combine the structural reliability of supervised learning with the performance optimization of reinforcement learning.

**Key Success Factors**:

1. **Clear separation of concerns**: SFT for structure, RFT for accuracy
2. **Consistent evaluation methodology**: Test without system prompts to measure true learning
3. **Building on foundations**: RFT builds on SFT rather than starting from scratch
4. **Quality training data**: High teacher model accuracy and format consistency

The result is a compact, efficient model that maintains the reasoning capabilities and output structure of much larger models, making it suitable for production deployment at significantly lower cost and latency.

**Next Steps**: Apply this methodology to your own domain-specific tasks by:

1. Defining appropriate outputs for your use case
2. Generating high-quality teacher demonstrations
3. Fine tuning
4. Evaluating performance improvements

This systematic approach to knowledge distillation enables you to create specialized, efficient models that retain the capabilities of their larger teachers while being practical for real-world deployment.

Questions or feedback? Reach out to us on [Discord](https://discord.gg/fireworks-ai).


# null
Source: https://docs.fireworks.ai/examples/reward-hacking



# Reward-Driven Summarizer - RFT on Fireworks

## Introduction

In this demo, we will demonstrate how thoughtful reward‑function design can steer a language model toward producing clear, 50‑token summaries that balance brevity with relevance. Using Fireworks’ reinforcement‑fine‑tuning workflow, you’ll see how adjusting a few well‑chosen signals can transform raw model outputs into reliable digests suitable for news briefs, chat recaps, and study notes—revealing, along the way, why defeating reward hacking is central to building trustworthy summarizers.

### Goals

Every summarizer will look different. Let’s set up some goals:

* Use `llama-v3p1-8b-instruct` to balance speed and model intelligence
* Summaries should be under 50 tokens
* Summaries should capture relevant information within a much larger text

### Why Reinforcement Fine-Tune?

Reinforcement Fine‑Tuning augments standard supervised training by adding a reward signal that scores each model output after it is generated. Instead of optimizing only for next‑token likelihood, the model learns from these scores—gradually preferring strategies that maximize the reward and discarding those that do not.

Traditional supervised fine‑tuning simply teaches a model to imitate example summaries, but it never checks whether the *finished* output actually satisfies our broader goals—like striking the right balance between brevity and substance. Reinforcement  Fine‑Tuning adds a feedback step after each summary is generated, letting us reward outputs that hit that balance and discourage ones that don’t. Because we can adjust this feedback on the fly, RFT gives us a practical steering mechanism: tweak the reward, observe how the model adapts, and quickly converge on summaries that are both concise and informative. For this sort of summarization task, that end‑to‑end feedback loop is essential—imitation alone can’t capture the nuanced trade‑offs we care about.

For more information on RFT on the Fireworks platform and when to use it, take a look at our examples on Knowledge Distillation

## Setup & Utils

If you haven’t already, head to [https://fireworks.ai/](https://fireworks.ai/), make an account, and grab an API key - you’ll need one for this demo.

```python  theme={null}
!pip install --upgrade fireworks-ai rouge-score transformers torch
```

```python  theme={null}
# Imports
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional
from fireworks import LLM
from rouge_score import rouge_scorer
import math, torch
import os

FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")

from fireworks import LLM

# Set Up Client
llm = LLM(
  model="llama-v3p1-8b-instruct",
  id="my-deployment-id",
  deployment_type="on-demand", # Can only fine-tune a dedicated deployment
  precision="FP8",
  accelerator_type="NVIDIA_H100_80GB",
) 
```

## Initial Test

Before we touch any fine-tuning or reward functions, we first run the task with an off‑the‑shelf model and record how its raw summaries perform. This baseline reveals the model’s natural tendencies—what it captures well, what it omits, and where it drifts from our goals.

Let’s define a system prompt:

```python  theme={null}
sys_prompt = """
Your job is to read a long document and produce a single, fluent English paragraph ≤ 50 GPT-2 tokens that captures the document’s four most important facts.

Rules you must obey for every response

1. Token limit – maximum 50 tokens
2. Importance – include the most critical factual points; leave out everything else.
3. No PII – never output emails, phone numbers, SSNs, or other personally identifying strings that may occur in the input.
4. Fluency – write clear, grammatical English in a single paragraph.
5. Output only the paragraph – no explanations, bullet lists, or metadata.

If the rules conflict, the priority is: Length > Coverage > No PII > Fluency.
"""
```

And try a sample document (I’m using a news article):

```python  theme={null}
long_document = """
MONTEREY PARK (KABC) -- Authorities are investigating an apparent explosion at an LASD training facility in Monterey Park where at least three deputies were killed.

The incident was reported just before 7:30 a.m. Friday at what looked to be LASD's SEB compound, which houses the sheriff's department's special enforcement units and bomb squad.

It appears the Sheriff's Enforcement Bureau personnel were handling some kind of explosives when there was a blast, according to preliminary information from sources. Three deputies were killed in the incident.

The Los Angeles County Fire Department responded to the scene. It's unclear if there were any other injuries.

It is believed to have been an accident. More is expected soon from the sheriff.

There were no other details immediately available regarding this incident.

L.A. City Mayor Karen Bass confirmed that the LAPD bomb squad is responding to the scene and assisting with the incident.

Governor Gavin Newsom's Office said the governor has been briefed on the apparent explosion and that the Governor's Office of Emergency Services is in contact with LASD while closely monitoring the situation.

L.A. County Supervisor Kathryn Barger issued the following statement regarding the deadly incident:

"I am heartbroken to hear of the terrible tragedy that has unfolded today at an L.A. County Sheriff's Department facility. I am closely tracking the situation as we learn more about what occurred and the condition of those affected. My heart is heavy, and my thoughts are with the brave men and women of the Sheriff's Department during this difficult time. We stand with them and their families as they navigate the hours and days ahead."

L.A. County Supervisor Hilda Solis also issued a statement:

"I am deeply saddened by the tragic incident that occurred this morning at the Los Angeles County Sheriff's Department Biscailuz Training Academy in East Los Angeles. My heart goes out to the families, friends, and colleagues of the three individuals who lost their lives in what appears to have been a devastating explosion. I am in contact with Sheriff Robert Luna and closely monitoring the situation as we await further details. My thoughts are with all those grieving and the first responders who are on the scene."

The FBI and ATF responded to the scene, according to a post from U.S. Attorney General Pam Bondi posted on X.

"Our federal agents are at the scene and we are working to learn more. Please pray for the families of the sheriff's deputies killed," the post said.
"""
```

```python  theme={null}
response = llm.chat.completions.create(
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": long_document}
    ],
    max_tokens=100, # can't set it to 50 as the model might just stop in the middle of a sentence

)

print(response.choices[0].message.content)

```

```python  theme={null}
"An apparent explosion occurred at the Los Angeles County Sheriff's Department training facility in Monterey Park, resulting in the deaths of at least three deputies. The incident occurred during a training exercise involving explosives, and authorities are investigating the cause as an accident. The Los Angeles County Fire Department and LAPD bomb squad responded to the scene, with the FBI and ATF also arriving to assist. L.A. County Supervisors Kathryn Barger and Hilda Solis expressed their condolences to the families of the victims, while Governor"
```

Pretty clear that the “summary” is hardly concise and starts simply copy the input text after a little bit, even though we specified to limit itself to 50 tokens in the system prompt. Not what we want from a summary.

To get around this, we’ll need to fine-tune our model. To understand the fundamentals of RFT and how the fireworks platform makes it easy, check out our course on Knowledge Distillation.

We’ll need to set up a reward function that gives the fireworks training kernel a signal on how *good* a certain response is. It’s our job to figure out what “good” means. Let’s get started!

## Part 1: Teach brevity (Length Gate)

Our opening baseline is a **binary “length‑only” reward**: a summary earns full credit if it stays within the token budget and zero otherwise. This simple gate makes it crystal‑clear to the model that excess verbosity is unacceptable.

```python  theme={null}
def token_len(txt: str) -> int:
    return len(txt.strip().split())

def extract_summary(msgs: List[Dict]) -> Optional[str]:
    for m in reversed(msgs):
        if m.get("role") == "assistant" and not m.get("tool_calls"):
            return m.get("content", "").strip()
    return None
```

```python  theme={null}
@reward_function
def length_gate_only(
    messages:           List[Dict[str, str]],
    original_messages:  Optional[List[Dict[str, str]]] = None,
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)

    if summary is None:
        return EvaluateResult(
            score   = 0.0,
            reason  = "parse error",
            metrics = {"token_len": MetricResult(0, False, "parse error")},
            error   = "parse_error",
        )

    tok_len = token_len(summary)
    if tok_len > 50:
        return EvaluateResult(
            score   = 0.0,
            reason  = f"length {tok_len} > 50 tokens",
            metrics = {"token_len": MetricResult(tok_len, False, str(tok_len))},
        )

    return EvaluateResult(
        score   = 1.0,
        reason  = f"length {tok_len} tokens (within limit)",
        metrics = {"token_len": MetricResult(tok_len, True,  str(tok_len))},
    )
```

Drop this evaluator into Fireworks’ RFT pipeline, point it at your dataset, and you’ll immediately force the model to tighten its summaries. Taking a look at a sample output, we see the following issue:

```python  theme={null}
"An explosion at an LASD training site killed 3 deputies."
```

The model learned that it can output very short “summaries” and achieve very high rewards. We’ll need to iterate on our reward function again.

## Part 2: Reward substance (ROUGE-L)

Once the model has learned that shorter is better, we need to remind it that substance still counts. The second evaluator rewards each summary according to how much of the source document’s wording it captures. A quick overlap measure—ROUGE‑L—is enough to push the policy toward mentioning the main ideas instead of trimming indiscriminately.

```python  theme={null}
# One global Rouge scorer – re-use for speed
_ro = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)

def rouge_recall(pred: str, ref: str) -> float:
    return _ro.score(pred, ref)["rougeL"].recall

def extract_doc(orig: List[Dict]) -> Optional[str]:
    return orig[-2].get("content", "").strip() if orig else None  

@reward_function
def summary_reward_v2_doc(
    messages:          List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)
    doc     = extract_doc(original_messages)

    if summary is None or doc is None:
        return EvaluateResult(0.0, "parse error",
                              {"coverage": MetricResult(0, False, "parse")},
                              error="parse_error")

    if token_len(summary) > 50:
        tl = token_len(summary)
        return EvaluateResult(0.0, f"length {tl} > 50",
                              {"coverage": MetricResult(0, False, "too long"),
                               "token_len": MetricResult(tl, False, str(tl))})

    cov = rouge_recall(summary, doc)    # 0–1

    return EvaluateResult(round(cov, 4),
                          f"Rouge-L recall {cov:.2f}",
                          {"coverage": MetricResult(cov, cov > .7, f"{cov:.2f}"),
                           "token_len": MetricResult(token_len(summary), True, str(token_len(summary)))})
```

Running it through the Fireworks RFT pipeline shows us that summaries regain essential details - which is an important counter-balance to the brevity score that we implemented earlier.

```python  theme={null}
"Three LASD deputies dead explosion at SEB training place, maybe accident with explosives, unclear if more hurt, FBI ATF LAPD there, waiting sheriff talk more."
```

This reads much better than before, but it still reads like a bullet mash‑up—missing verbs, punctuation, and time context—so clarity and polish are next on the fix‑list.

## Part 3: Focus on key facts (Bullet Recall)

Our third evaluator narrows the comparison window from the **entire source document** to a **curated bullet list of key facts**. Pure document‑level ROUGE can reward nonsense phrases that merely echo scattered words; by contrast, scoring against a focused checklist forces the model to mention the specific points humans actually care about.

The downside is cost: generating high‑quality bullet lists requires either human or much larger LLM annotation.

For example, a bullet point list of our new example might look like the following:

```python  theme={null}
[
"An explosion occurred at the LASD Special Enforcement Bureau (SEB) training facility in Monterey Park around 7:30 a.m.",
"Three sheriff’s deputies were killed, reportedly while handling explosives; cause appears accidental.",
"FBI, ATF, LAPD bomb squad, and L.A. County Fire responded; further injuries are unconfirmed.",
"Officials including Governor Newsom and Supervisors Barger and Solis issued condolences; more details pending from Sheriff Luna.",
]
```

Let’s enhance our dataset by adding this list and start writing our reward function. We’ll keep parts that we’ve developed so far and build upon that.

```python  theme={null}
def extract_bullets(orig: List[Dict]) -> Optional[List[str]]:
    return orig[-1].get("bullets") if orig else None

@reward_function
def summary_reward_v3_bullets(
    messages:          List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    bullets:           Optional[List[str]]
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)
    bullets = extract_bullets(original_messages)

    if summary is None or bullets is None:
        return EvaluateResult(0.0, "parse error",
                              {"coverage": MetricResult(0, False, "parse")},
                              error="parse_error")

    if token_len(summary) > 50:
        tl = token_len(summary)
        return EvaluateResult(0.0, f"length {tl} > 50",
                              {"coverage": MetricResult(0, False, "too long"),
                               "token_len": MetricResult(tl, False, str(tl))})

    joined = "\n".join(bullets)
    cov    = rouge_recall(summary, joined)

    return EvaluateResult(round(cov, 4),
                          f"Rouge-L recall {cov:.2f}",
                          {"coverage": MetricResult(cov, cov > .7, f"{cov:.2f}"),
                           "token_len": MetricResult(token_len(summary), True, str(token_len(summary)))})
```

Once again, let’s run it through our pipeline and get a sample result:

```python  theme={null}
"Three LASD deputies died in a likely accidental blast at SEB facility. FBI, ATF, LAPD responded. Officials expressed condolences. Details from Sheriff awaited."
```

By rewarding matches to these distilled key facts, the model learns to deliver summaries that are short **and** on-point—no more empty verbage, far fewer hallucinations. It looks a lot better than when we first started. We could reasonably stop here—the summaries are now short and reliably cover the must‑know facts—but let’s push one step further.

## Advanced Reward: Polish style (Fluency)

With essentials and length under control, the last step is polish: we combine the bullet‑coverage score with a fluency bonus (low perplexity from a tiny GPT‑2 scorer). The reward is a weighted average, so you can dial emphasis toward clarity or content with one line of code through the use of `reward-kit`

```python  theme={null}
# GPT-2 tiny fluency model (load once)
_tok  = AutoTokenizer.from_pretrained("gpt2")
_gpt2 = AutoModelForCausalLM.from_pretrained("gpt2"); _gpt2.eval()

def fluency(text: str) -> float:
    with torch.no_grad():
        ids  = _tok(text, return_tensors="pt").input_ids
        loss = _gpt2(ids, labels=ids).loss.item()
    return max(0.0, min(1.0, 1 - (loss - 2) / 8))   # maps loss ≈2-10 → score 1-0

@reward_function
def summary_reward_final(
    messages:          List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs,
) -> EvaluateResult:

    summary = extract_summary(messages)
    bullets = extract_bullets(original_messages)

    if summary is None or bullets is None:
        return EvaluateResult(0.0, "parse error",
                              {"coverage": MetricResult(0, False, "parse"),
                               "fluency" : MetricResult(0, False, "parse")},
                              error="parse_error")

    if token_len(summary) > 50:
        tl = token_len(summary)
        return EvaluateResult(0.0, f"length {tl} > 50",
                              {"coverage": MetricResult(0, False, "too long"),
                               "fluency" : MetricResult(0, False, "too long"),
                               "token_len": MetricResult(tl, False, str(tl))})

    cov = max(0.05, rouge_recall(summary, "\n".join(bullets)))
    fl  = max(0.05, fluency(summary))
    score = math.sqrt(cov * fl)

    return EvaluateResult(round(score, 4),
                          f"cov={cov:.2f}, flu={fl:.2f}",
                          {"coverage": MetricResult(cov, cov > .7, f"{cov:.2f}"),
                           "fluency" : MetricResult(fl,  fl > .7, f"{fl:.2f}"),
                           "token_len": MetricResult(token_len(summary), True, str(token_len(summary)))})
```

This blended signal nudges the model to mention every must‑know bullet **and** read naturally, giving us crisp, on‑topic summaries with human‑friendly flow—our final polish after the earlier length and coverage stages.

Here’s an output:

```python  theme={null}
"An explosion at LASD’s SEB facility killed three deputies during explosives training. FBI, ATF, and LAPD responded. Officials offered condolences, and further details are expected from Sheriff Luna as the investigation continues into the apparent accident."
```

Exactly 47 tokens! It names the location, casualties, training context, responding agencies, public response, and the pending investigation—all in polished, complete sentences with no filler.

## Takeaways

By walking a plain language model through four reward tweaks—length gate, document overlap, key‑bullet focus, and a final fluency blend—we steered it into a dependable 50‑token summarizer. Each change showed, in minutes, how the model bends to whatever signal we supply, thanks to the lightweight evaluator‑swap workflow built into Fireworks’ RFT platform.

1. **A model follows its incentives, not your intentions.** Define the right reward and you steer behaviour directly; leave gaps and the model finds them.
2. **Start simple, then layer complexity.** A binary length check exposed verbosity problems instantly; later signals refined relevance and style.
3. **End‑to‑end feedback beats imitation alone.** Rewarding the full output captures goals that token‑level training can’t touch.

The exercise also showed how quickly you can iterate when evaluators are first‑class citizens: swap one in, rerun, and immediately trace the effect. Keep that loop handy, keep the reward honest, and your models will do exactly what you ask—**nothing more, nothing less.**

That’s the demo — let the summaries speak for themselves.


# null
Source: https://docs.fireworks.ai/examples/text-to-sql



# ✈️ Natural-Language → SQL with Reinforcement-Fine-Tuning (RFT)

## 🎯 What You'll Build

Welcome! This tutorial will show you how to fine-tune a 7B parameter model to answer natural language (NL) questions by writing SQL to execute against your database, without using real production data in fine-tuning the process. Thus, you will end up with a model that can accurately translate natural language to SQL, which can be executed against a database, for workflows like:

<div
  align="center"
  style={{
fontSize: '24px', 
fontWeight: 'bold',
border: '2px solid #667eea',
borderRadius: '12px',
padding: '16px 24px',
background: 'linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%)',
margin: '20px auto',
maxWidth: 'fit-content'
}}
>
  👤 User asks question → 🤖 Model generates SQL → 📊 Database returns results
</div>

## 🚀 Peformance Benefits of RFT

Before diving in to the tutorial, here's a summary of the accuracy we achieved, using the [OpenFlights dataset](https://openflights.org/data.html) as a base, across various models:

| Model                          | Accuracy on Test Set | Size  | Speed |
| ------------------------------ | -------------------- | ----- | ----- |
| **Qwen 2.5 7B (base)**         | 23.91%               | Small | Fast  |
| **DeepSeek V3**                | 27.17%               | Large | Slow  |
| **Kimi K2 Instruct**           | 28.26%               | Large | Slow  |
| **OpenAI GPT-4o**              | 23.91%               | Large | Slow  |
| **Anthropic Claude Sonnet 4**  | 29.35%               | Large | Slow  |
| **Qwen3 Coder 480B**           | 34.78%               | Large | Slow  |
| **Our Fine-Tuned Qwen 2.5 7B** | **56.52%** ✨         | Small | Fast  |

<div style={{ fontSize: '0.8em' }}>
  > Note on methodology: to compare accuracy across the above models, we created a synthetic dataset that mirrors the OpenFlights schema, an initial set of synthetic queries written by Qwen3 Coder 480B,
  > and a synthetic set of natural language questions (also written by Qwen3 Coder 480B) corresponding to those queries. The task above is for the LLM to translate each natural language question into SQL, and then execute the SQL query against the synthetic dataset.
  > Accuracy is computed as the percent of queries that return the correct result (N = 92). "Correct" is defined as the query returning the same result on the synthetic dataset as each initial synthetic query did.
  > Thus, the relative performance between these models is a more meaningful metric than the absolute performance. More details on the data and evaluation process can be found throughout the tutorial below.
</div>

**Key takeaway**: Our fine-tuned 7B model outperforms models that are 50-200x larger, while being faster and cheaper to run.

## 💡 Why Reinforcement Fine-Tuning?

### The Problem with Supervised Fine-Tuning (SFT) for this use-case

SFT teaches models to mimic exact SQL syntax by showing them question-SQL pairs. But the key insight is that **we care more about the result of the query than the exact SQL syntax**.

With SFT, the model is penalized if it generates a different SQL query from the training example, even though both are perfectly correct. This can lead to:

* ❌ Overfitting to specific SQL patterns
* ❌ Poorer generalization to new questions
* ❌ Need for thousands of perfectly-matched examples

### The RFT Solution

Reinforcement Fine-Tuning (RFT) takes a fundamentally different approach:

* ✅ **Rewards correct results**, regardless of SQL syntax
* ✅ **Explores multiple solution paths** during training
* ✅ **Works with just hundreds of examples** instead of thousands

## 🔄 The Process: From Schema to Expert Model

Here's the complete pipeline you'll implement:

1. **Start with just your schema** (no real data needed!): Extract table structures and relationships
2. **Generate synthetic data**: Use LLMs to create realistic fake data that maintains referential integrity
3. **Create SQL queries**: Use historical logs or generate diverse query patterns
4. **Execute for ground truth**: Run queries against synthetic data to get expected results
5. **Generate natural language questions**: Convert SQL to questions users would actually ask
6. **Train with RFT**: Model learns through trial and error, rewarded for correct results

### Why this matters

Off-the-shelf LLM copilots often guess column names, ignore schema quirks, or hallucinate tables. **Reinforcement Fine-Tuning (RFT)** fixes this by teaching the model the shape of your data *and* the patterns in your queries, boosting exact-match accuracy.

***

## What this tutorial will cover

| You'll practice …                                              | … and walk away with                                                                      |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| ✅ **Generate a synthetic DuckDB** that mirrors your schema     | `synthetic_openflights.db` (\<20 MB) served via an MCP endpoint                           |
| ✅ **Create a MECE query set** & compute ground-truth rows      | `generated_queries.json` & `ground_truth_results.json`                                    |
| ✅ **Build NL ↔ SQL result pairs** for fine-tuning and eval     | `final_rft_sql_train_data.jsonl` & `final_rft_sql_test_data.jsonl`                        |
| ✅ **Run an RFT job on Fireworks AI**                           | A tuned **Qwen 2.5-7B** checkpoint                                                        |
| ✅ **Benchmark baseline vs. tuned model** and a larger baseline | > 30% exact-match improvement over Qwen 2.5-7B base model and > 20% over SoTA base models |

### Agenda

0. 🛠️ Development Environment Setup
1. 🗄️ Simulate the "Production" Database
2. 📋 Acquire the Schema (No Real Data!)
3. 🧪 Create the Synthetic Training Sandbox with an LLM
4. ✅ Validate the Sandbox
5. 📝 Generate Example SQL Queries
6. ♻️ Query-Aware Augmentation of the Synthetic Sandbox
7. 🎯 Execute Queries to Get Ground-Truth Answers
8. 💬 Generate Natural Language Questions for Final RFT Training Data
9. 🛰️ Deploy an MCP Server for the Synthetic Data
10. ☁️ Set Up Google Cloud CLI & .gcloudignore
11. 📦 Containerize & Deploy the MCP Server
12. 🔍 Define an evaluation function for RFT
13. 🧪 Test English -> SQL of a base model without fine-tuning
14. 🚀 Launch the Fine-Tuning Job & Deploy via the UI
15. ⚖️ Evaluate Model Performance
16. ✨ Cleanup & Conclusion

> **Demo vs Real World 🌍**\
> Look for these call-outs to see the difference between the self-contained demo steps in this notebook and the equivalent actions you’d perform on your own private schema, logs, and query store.

### 0. 🛠️ Development Environment Setup

**Complete these steps once in your terminal, *outside* this notebook.**

1. **Get a Fireworks AI API Key**
   * Go to [fireworks.ai](https://fireworks.ai) and sign up.
   * Create an API key from your settings page.
   * Create a file named `.env` in your project directory and add your key:
     ```
     FIREWORKS_API_KEY="YOUR_API_KEY_HERE"
     ```

2. **Install `uv`**
   * `uv` is a fast Python package manager from Astral. Follow the official installation instructions at [docs.astral.sh/uv/](https://docs.astral.sh/uv/).
   * It's significantly faster than pip and handles dependency resolution more reliably.

3. **Create a Virtual Environment and Install Packages**
   * Once `uv` is installed, initialize a project.
   ```bash  theme={null}
   # Run this in your terminal
   uv init --python 3.12
   ```
   * Install all required packages using `uv add`.
   ```bash  theme={null}
   # Run this in your terminal
   uv add duckdb tabulate pandas pyarrow requests \
          pydantic python-dotenv \
          jsonlines fireworks-ai \
          mcp-server-motherduck ipykernel
   ```
   * Create and activate a virtual environment
   ```bash  theme={null}
   # Run this in your terminal
   uv sync
   source .venv/bin/activate
   ```

After running these commands, your environment is ready. You can proceed with the tutorial.

### 1. 🗄️ Simulate the "Production" Database

First, we'll create a database that represents your real, populated production database. We'll download the public OpenFlights dataset and load it into a DuckDB file.

#### What is DuckDB?

DuckDB is an in-process SQL OLAP database management system. Think of it as "SQLite for analytics". It's perfect for this tutorial because:

* It's embedded (no server setup required)
* It's fast for analytical queries
* It has excellent SQL compatibility
* The entire database is just a single file
* It has an existing MCP server we can use ([mcp-server-motherduck](https://github.com/motherduckdb/mcp-server-motherduck))

> **Real World 🌍**: You already have this! It's your live production database (or a replica). You would skip this entire step.

```python  theme={null}
import urllib.request
import pathlib
import pandas as pd
import duckdb

# --- Download the raw data files ---
DATA_DIR = pathlib.Path("data")
DATA_DIR.mkdir(exist_ok=True)
BASE_URL = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/"
FILES_TO_DOWNLOAD = {
    "airports": "airports.dat",
    "airlines": "airlines.dat",
    "routes": "routes.dat",
    "countries": "countries.dat",
    "planes": "planes.dat"
}
# Define column names as the files don't have headers
COLUMN_NAMES = {
    "airports": ["airport_id", "name", "city", "country", "iata", "icao", "latitude", "longitude", "altitude", "timezone", "dst", "tz_db", "type", "source"],
    "airlines": ["airline_id", "name", "alias", "iata", "icao", "callsign", "country", "active"],
    "routes": ["airline", "airline_id", "source_airport", "source_airport_id", "destination_airport", "destination_airport_id", "codeshare", "stops", "equipment"],
    "countries": ["name", "iso_code", "dafif_code"],
    "planes": ["name", "iata", "icao"]
}

PROD_DB_PATH = "data/prod_openflights.db"

# --- Load the real data into our "production" DuckDB ---
with duckdb.connect(PROD_DB_PATH) as con:
    for name, filename in FILES_TO_DOWNLOAD.items():
        url = f"{BASE_URL}{filename}"
        path = DATA_DIR / filename
        if not path.exists():
            urllib.request.urlretrieve(url, path)
            print(f"✅ Downloaded: {path}")

        # Load data using pandas to handle missing headers and null values
        df = pd.read_csv(path, header=None, names=COLUMN_NAMES[name], na_values=["\\N"])
        con.execute(f"CREATE OR REPLACE TABLE {name} AS SELECT * FROM df")

    print(f"\n✅ 'Production' database simulated at: {PROD_DB_PATH}")
    print("Tables created:", con.sql("SHOW TABLES;").fetchall())
```

✅ 'Production' database simulated at: data/prod\_openflights.db
Tables created: \[('airlines',), ('airports',), ('countries',), ('planes',), ('routes',)]

### 2. 📋 Acquire the Schema (No Real Data!)

This is a critical step. We connect to our "production" database and extract **only its schema** (the table structure, column names, and data types). We do not touch or read any of the data rows. This schema is the only artifact we need from the production environment.

#### Why Schema-Only?

This approach is powerful because:

* **Privacy**: No actual customer data leaves your production environment
* **Security**: No risk of exposing sensitive data during fine-tuning
* **Efficiency**: Schema information is tiny compared to actual data

The `DESCRIBE` command in DuckDB gives us comprehensive schema information without accessing any rows.

> **Real World 🌍**: You would connect to your production database and run the DESCRIBE command shown below, thus obtaining the schema information for all its tables.

```python  theme={null}
import duckdb

# Connect to the "production" database we just created
with duckdb.connect(PROD_DB_PATH, read_only=True) as con:
    # The DESCRIBE command gives us the schema information for all tables
    schema_df = con.sql("DESCRIBE;").df()

print("✅ Schema successfully extracted from 'production' database:")
print(schema_df.to_markdown(index=False))

# We can also store this for later use in prompts
schema_for_prompt = schema_df.to_markdown(index=False)
```

✅ Schema successfully extracted from 'production' database:

| database          | schema | name      | column\_names                                                                | column\_types                                                          | temporary |
| :---------------- | :----- | :-------- | :--------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :-------- |
| prod\_openflights | main   | airlines  | \['airline\_id' 'name' 'alias' 'iata' 'icao' 'callsign' 'country' 'active']  | \['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' | False     |
|                   |        |           |                                                                              | 'VARCHAR']                                                             |           |
| prod\_openflights | main   | airports  | \['airport\_id' 'name' 'city' 'country' 'iata' 'icao' 'latitude' 'longitude' | \['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'DOUBLE'  | False     |
|                   |        |           | 'altitude' 'timezone' 'dst' 'tz\_db' 'type' 'source']                        | 'DOUBLE' 'BIGINT' 'DOUBLE' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR']    |           |
| prod\_openflights | main   | countries | \['name' 'iso\_code' 'dafif\_code']                                          | \['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False     |
| prod\_openflights | main   | planes    | \['name' 'iata' 'icao']                                                      | \['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False     |
| prod\_openflights | main   | routes    | \['airline' 'airline\_id' 'source\_airport' 'source\_airport\_id'            | \['VARCHAR' 'DOUBLE' 'VARCHAR' 'DOUBLE' 'VARCHAR' 'DOUBLE' 'VARCHAR'   | False     |
|                   |        |           | 'destination\_airport' 'destination\_airport\_id' 'codeshare' 'stops'        | 'BIGINT' 'VARCHAR']                                                    |           |
|                   |        |           | 'equipment']                                                                 |                                                                        |           |

### 3. 🧪 Create the Synthetic Training Sandbox with an LLM

Now that we have the schema, we will use a large language model to generate a complete, contextually-aware synthetic dataset.

#### Key Concepts in This Step:

**Dynamic Pydantic Model Generation**: We dynamically create Pydantic models based on your database schema. This ensures the LLM's output is structured and parseable, adapting to any database schema automatically.

**Chunked Generation Strategy**: Instead of asking for all data at once (which could overwhelm the LLM or hit token limits), we generate data in small chunks of 2 rows per API call. This approach:

* Ensures high-quality, coherent data
* Avoids token limit issues

**Contextual Awareness**: Each generation request includes previously generated data as context, preventing duplicates and ensuring variety.

To fine-tune our model with RFT, **we will only interact with this synthetic database.**

> **Real World 🌍**: This pattern is directly applicable. You would use the same approach with your production schema to generate synthetic data that maintains the structure and relationships of your real data without exposing any actual records.

```python  theme={null}
import pandas as pd
import os
from pydantic import create_model, BaseModel
from fireworks import LLM
import duckdb
import json
from dotenv import load_dotenv
from typing import List, Optional, Any, Dict, Type
import datetime
import decimal
import uuid
import math
import time


TARGET_ROW_COUNT = 100  # The number of rows to generate for each table.

# --- 1. Dynamically Create Pydantic Models from the SQL Schema ---
def map_sql_type_to_python(sql_type: str) -> Type:
    """Maps SQL data types to Python types for Pydantic models."""
    sql_type_upper = str(sql_type).upper()
    if 'DECIMAL' in sql_type_upper: return decimal.Decimal
    if 'DOUBLE' in sql_type_upper or 'FLOAT' in sql_type_upper or 'REAL' in sql_type_upper: return float
    if 'BIGINT' in sql_type_upper or 'INT' in sql_type_upper: return int
    if 'VARCHAR' in sql_type_upper or 'TEXT' in sql_type_upper or 'STRING' in sql_type_upper: return str
    if 'TIMESTAMP' in sql_type_upper: return datetime.datetime
    if 'DATE' in sql_type_upper: return datetime.date
    if 'TIME' in sql_type_upper: return datetime.time
    if 'BOOLEAN' in sql_type_upper: return bool
    if 'BLOB' in sql_type_upper or 'BYTEA' in sql_type_upper: return bytes
    if 'UUID' in sql_type_upper: return uuid.UUID
    return object

pydantic_models: Dict[str, Type[BaseModel]] = {}
table_names = schema_df['name'].unique()

for table_name in table_names:
    table_schema = schema_df[schema_df['name'] == table_name].iloc[0]
    fields: Dict[str, Any] = {}
    col_names = table_schema['column_names']
    col_types = table_schema['column_types']
    for i, col_name in enumerate(col_names):
        python_type = map_sql_type_to_python(col_types[i])
        fields[col_name] = (Optional[python_type], None)
    model_name = table_name.capitalize() + "Model"
    pydantic_models[table_name] = create_model(model_name, **fields)

dataset_fields: Dict[str, Any] = {
    table_name: (List[model], ...) for table_name, model in pydantic_models.items()
}
SyntheticDataset = create_model('SyntheticDataset', **dataset_fields)
print("✅ Dynamically created Pydantic models for all tables.")


# --- 2. Define Total Row Counts and Chunking Strategy ---
TOTAL_ROW_COUNTS = {name: TARGET_ROW_COUNT for name in table_names}
ROWS_PER_API_CALL = 2 # Ask for data in small, safe chunks
print("\n✅ Data Generation Plan:")
print(f" - Target rows per table: {list(TOTAL_ROW_COUNTS.values())[0]}")
print(f" - Will make API calls asking for {ROWS_PER_API_CALL} rows/call until target is met.")


# --- 3. Setup LLM and Loop to Generate Data in Chunks ---
SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"
load_dotenv()
llm = LLM(model="accounts/fireworks/models/deepseek-v3", deployment_type="serverless", api_key=os.getenv("FIREWORKS_API_KEY"))

all_synthetic_data: Dict[str, List[Dict]] = {name: [] for name in table_names}
chunk_row_counts = {name: ROWS_PER_API_CALL for name in table_names}

base_generation_prompt = f"""
You are a highly intelligent AI data generator. Your task is to create a realistic, synthetic dataset based on the provided database schema.
The data you generate must be internally consistent. For example, an `airline_id` in a `routes` table must correspond to an existing `airline_id` in an `airlines` table within this same generated chunk.
This applies to any schema you might be working with, not just airline-related data.
You must generate a single JSON object that strictly adheres to the provided JSON schema.

The database schema is as follows:
{schema_for_prompt}
"""

call_count = 0
# Loop until all tables have at least the desired number of rows
while not all(len(rows) >= TOTAL_ROW_COUNTS[name] for name, rows in all_synthetic_data.items()):
    call_count += 1
    print(f"\n📞 --- Generating data chunk #{call_count} ---")
    
    # --- Create a summary of existing data to guide the LLM ---
    existing_data_summary = ""
    if any(len(rows) > 0 for rows in all_synthetic_data.values()):
        summary_parts = ["\nYou have already generated the following data. Do NOT generate rows that are substantially similar to these examples. Create new, unique data.\n"]
        for table_name, rows in all_synthetic_data.items():
            if rows:
                summary_parts.append(f"\n--- Existing data in '{table_name}' table ---")
                sample_rows = rows[-100:] if len(rows) > 100 else rows  # sample the last 100 rows
                df = pd.DataFrame(sample_rows)
                if len(df.columns) > 10:
                    df = df.iloc[:, :10]
                markdown_summary = df.to_markdown(index=False, tablefmt="grid")
                if markdown_summary:
                    summary_parts.append(markdown_summary)
        existing_data_summary = "\n".join(summary_parts)


    # --- Construct the final prompt for this iteration ---
    final_prompt = (
        base_generation_prompt +
        existing_data_summary +
        f"\n\nNow, generate a NEW JSON object with a key for each table. The number of new rows for each table should be:\n" +
        json.dumps(chunk_row_counts, indent=2)
    )

    response = llm.chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        response_format={"type": "json_schema", "json_schema": {"name": "SyntheticDataset", "schema": SyntheticDataset.model_json_schema()}},
        temperature=0.7
    )

    choice = response.choices[0]
    response_content = choice.message.content

    if choice.finish_reason == "length":
        print(f"⚠️ WARNING: Chunk #{call_count} was truncated. Skipping.")
        continue
    if not response_content:
        print(f"⚠️ WARNING: Received empty content for chunk #{call_count}. Skipping.")
        continue

    try:
        chunk_data = json.loads(response_content)
        print(f"✅ Received and parsed chunk #{call_count}.")
        for table_name, rows in chunk_data.items():
            if table_name in all_synthetic_data and rows:
                all_synthetic_data[table_name].extend(rows)
        # Log progress
        for name, rows in all_synthetic_data.items():
             print(f"   - '{name}': {len(rows)} / {TOTAL_ROW_COUNTS[name]} rows")
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Failed to parse JSON for chunk #{call_count}. Reason: {e}. Skipping.")
    
    time.sleep(1)

# --- 4. Deduplicate and Write to DB ---
print("\n✨ Data generation complete. Aggregating, deduplicating, and saving to database...")

synthetic_data = all_synthetic_data
print("\n--- Deduplicating generated data ---")
for table_name, rows in synthetic_data.items():
    if not rows: continue
    initial_count = len(rows)
    df = pd.DataFrame(rows).drop_duplicates()
    final_count = len(df)
    synthetic_data[table_name] = df.to_dict('records')
    print(f" - Table '{table_name}': Removed {initial_count - final_count} duplicates ({initial_count} -> {final_count}).")

# Final trim to ensure exact counts
for table_name, total_rows_needed in TOTAL_ROW_COUNTS.items():
    if table_name in synthetic_data:
        synthetic_data[table_name] = synthetic_data[table_name][:total_rows_needed]

with duckdb.connect(SYNTHETIC_DB_PATH) as con:
    for table_name, rows in synthetic_data.items():
        if rows:
            df = pd.DataFrame(rows)
            schema_cols = schema_df[schema_df['name'] == table_name].iloc[0]['column_names']
            for col in schema_cols:
                if col not in df.columns: df[col] = None
            df = df[schema_cols]
            con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
    
    print(f"\n✅ Synthetic training sandbox created at: {SYNTHETIC_DB_PATH}")
    print("Tables created:", con.sql("SHOW TABLES;").fetchall())
```

#### 4. ✅ Validate the Sandbox

Let's run a few queries against our new synthetic database to ensure the LLM did a good job generating plausible, interconnected data.

We expect to see non-empty, realistic-looking data that follows the schema constraints.

```python  theme={null}
import duckdb
from tabulate import tabulate

SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"

# Connect to the synthetic database
with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    
    # Get the list of all tables created
    all_tables = [table[0] for table in con.sql("SHOW TABLES;").fetchall()]
    
    # Select the first 3 tables to display (or all if fewer than 3)
    tables_to_validate = all_tables[:3]

    print("--- Validating the first few tables in the synthetic sandbox ---\n")

    # Execute and print results for the selected tables
    for table_name in tables_to_validate:
        print(f"--- SELECT * FROM {table_name} LIMIT 3; ---")
        try:
            result_df = con.sql(f"SELECT * FROM {table_name} LIMIT 3;").df()
            if not result_df.empty:
                print(tabulate(result_df, headers='keys', tablefmt='psql'))
            else:
                print(f"(Table '{table_name}' is empty)")
        except Exception as e:
            print(f"Query failed for table '{table_name}': {e}")
        print("\n")
```

\--- Validating the first few tables in the synthetic sandbox ---

\--- SELECT \* FROM airlines LIMIT 3; ---

| airline\_id | name                  | alias | iata | icao | callsign     | country      | active |
| ----------- | --------------------- | ----- | ---- | ---- | ------------ | ------------ | ------ |
| 58          | Nordic Eagle Airlines | NEA   | NE   | NEA  | NORDIC EAGLE | Finland      | Y      |
| 70          | Sapphire Sky Airlines | SSA   | SS   | SSA  | SAPPHIRESKY  | South Africa | Y      |
| 86          | Polar Air             | PA    | PL   | POL  | POLARAIR     | Malaysia     | Y      |

\--- SELECT \* FROM airports LIMIT 3; ---

| airport\_id | name                    | city   | country | iata | icao | latitude | longitude | altitude | timezone | dst | tz\_db       | type    | source      |
| ----------- | ----------------------- | ------ | ------- | ---- | ---- | -------- | --------- | -------- | -------- | --- | ------------ | ------- | ----------- |
| 17          | Rainbow Paris Airport   | Paris  | France  | RPA  | RPA  | 48.8566  | 2.3522    | 35       | 1        | E   | Europe/Paris | airport | OurAirports |
| 32          | Orbit Paris Airport     | Paris  | France  | ORP  | ORPA | 48.8566  | 2.3522    | 35       | 1        | E   | Europe/Paris | airport | OurAirports |
| 77          | Red Star Moscow Airport | Moscow | Russia  | RSM  | RSMA | 55.7558  | 37.6173   | 15       |          |     |              |         |             |

\--- SELECT \* FROM countries LIMIT 3; ---

| name         | iso\_code | dafif\_code |
| ------------ | --------- | ----------- |
| Norway       | NO        | NOR         |
| Italy        | IT        | ITA         |
| Saudi Arabia | SA        | SAU         |

### 5. 📝 Generate Example SQL Queries

With our synthetic database in place, the next step is to create a set of synthetic SQL queries. These SQL queries will be executed against our database of synthetic data to get the ground truth labels for RFT. Furthermore, these same SQL queries will be used as input to an LLM to generate queries in natural language. This will enable us to form our final RFT dataset, which pairs natural language queries with ground truth results from the database.

#### Query Generation Strategy:

* **Diversity**: We want queries covering different SQL features (JOINs, GROUP BY, aggregates)
* **Complexity Range**: From simple SELECT statements to complex multi-table joins
* **Deterministic Results**: Queries include ORDER BY clauses where necessary to break ties and ensure consistent results
* **MECE Principle**: Mutually Exclusive, Collectively Exhaustive - covering all major query patterns

> **Real World 🌍**: You would use a historical log of real SQL queries that have been run against your production database; aim for \~500 unique SQL queries. These logs are the most valuable source of training data because they represent the *actual* way your users query your data.

```python  theme={null}
import pandas as pd
import json
import time
from pydantic import BaseModel, Field
from typing import List
from fireworks import LLM
import os
import duckdb
from dotenv import load_dotenv

load_dotenv()

# --- 1. Define Generation Parameters and Pydantic Model ---
llm = LLM(model="accounts/fireworks/models/qwen3-coder-480b-a35b-instruct", deployment_type="serverless", api_key=os.getenv("FIREWORKS_API_KEY"))  # Use Qwen3-coder for SQL queries
TOTAL_QUERIES_TO_GENERATE = 1000  # Note, some of these queries will likely be duplicates or invalid, reducing the final number used for fine-tuning
QUERIES_PER_API_CALL = 30

class SqlQueryBatch(BaseModel):
    queries: List[str] = Field(description=f"A list of exactly {QUERIES_PER_API_CALL} unique and diverse SQL queries.")

print(f"🎯 Goal: Generate {TOTAL_QUERIES_TO_GENERATE} unique queries in batches of {QUERIES_PER_API_CALL}.")

# --- 2. Get Clean Schema From Synthetic DB ---
with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    schema_df = con.sql("DESCRIBE;").df()
    schema_for_prompt = schema_df.to_markdown(index=False)

# --- 3. Setup Base Prompt and Generation Loop ---
base_query_generation_prompt = f"""
You are an expert SQL data analyst. Your task is to generate unique and diverse SQL queries based on the database schema provided.
The queries should be realistic and cover a range of complexities and SQL features (JOINS, GROUP BY, aggregates, etc.).
Ensure you break ties with ORDER BY clauses so that the same queries produce the same results when executed against the database.
Write only the raw SQL query text and nothing else (i.e., no markdown formatting); your output should be a directly executable valid SQL query.
Make sure your queries do not return duplicate rows (i.e., GROUP BY all columns that are not aggregate functions).
Ensure the generated SQL is valid for DuckDB.

**Database Schema:**
{schema_for_prompt}
""".strip()

all_generated_queries = []
# Loop until we have enough queries
while len(all_generated_queries) < TOTAL_QUERIES_TO_GENERATE:
    print(f"\n📞 --- Generating batch #{len(all_generated_queries) // QUERIES_PER_API_CALL + 1} ---")

    # Create a summary of queries generated so far to prevent duplicates
    existing_queries_summary = ""
    if all_generated_queries:
        summary_parts = ["\nYou have already generated the following queries:\n"]
        for i, q in enumerate(all_generated_queries):
            summary_parts.append(f"{i+1}. {q}")
        existing_queries_summary = "\n".join(summary_parts)

    # Construct the final prompt for this iteration
    final_prompt = (
        base_query_generation_prompt +
        existing_queries_summary +
        f"\n\nNow, generate {QUERIES_PER_API_CALL} new, unique SQL queries, which cover different analytic scenarios and are not already in the list above. Return your response as a single JSON object adhering to the specified schema."
    )

    response = llm.chat.completions.create(
        messages=[{"role": "user", "content": final_prompt}],
        response_format={"type": "json_schema", "json_schema": {"name": "SqlQueryBatch", "schema": SqlQueryBatch.model_json_schema()}},
        temperature=0.8
    )

    response_content = response.choices[0].message.content
    if response_content:
        try:
            new_queries = json.loads(response_content).get("queries", [])
            all_generated_queries.extend(new_queries)
            print(f"   - Received {len(new_queries)} new queries. Total now: {len(all_generated_queries)} / {TOTAL_QUERIES_TO_GENERATE}")
        except json.JSONDecodeError as e:
            print(f"❌ ERROR: Failed to parse generated queries in this batch: {e}")
    
    time.sleep(1) # Be nice to the API

# --- 4. Deduplicate, Trim, and Save --- 
print("\n✨ Generation complete. Deduplicating and saving...")
initial_count = len(all_generated_queries)
# Simple, fast deduplication preserving order
unique_queries = list(dict.fromkeys(all_generated_queries))
final_count = len(unique_queries)
print(f" - Removed {initial_count - final_count} duplicates ({initial_count} -> {final_count}).")

# Trim to the exact number we need
final_queries = unique_queries[:TOTAL_QUERIES_TO_GENERATE]

# Save the final list to a file
QUERIES_FILE_PATH = "data/generated_queries.json"
with open(QUERIES_FILE_PATH, 'w') as f:
    json.dump({"queries": final_queries}, f, indent=2)

print(f"\n✅ Successfully saved {len(final_queries)} unique queries to `{QUERIES_FILE_PATH}`.")
print("\n--- Here are a few examples: ---")
for query in final_queries[:5]:
    print(f"- {query}")
```

```python  theme={null}
# Check the proportion of generated SQL queries that return zero rows

import json
import duckdb

try:
    SYNTHETIC_DB_PATH
except NameError:
    SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"

try:
    QUERIES_FILE_PATH
except NameError:
    QUERIES_FILE_PATH = "data/generated_queries.json"

with open(QUERIES_FILE_PATH, "r") as f:
    queries = json.load(f).get("queries", [])

total = len(queries)
zero_rows = 0
success = 0
failed = 0

with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    for q in queries:
        try:
            cnt = con.sql(f"SELECT COUNT(*) AS c FROM ({q}) AS t").fetchone()[0]
            zero_rows += (cnt == 0)
            success += 1
        except Exception:
            failed += 1

print(f"Total queries: {total}")
print(f"Executed successfully: {success}")
print(f"Execution errors: {failed}")
print(f"Zero-row results: {zero_rows}")
if total > 0:
    print(f"Proportion zero-row (overall): {zero_rows/total:.3f}")
if success > 0:
    print(f"Proportion zero-row (successful only): {zero_rows/success:.3f}")
```

Total queries: 549
Executed successfully: 516
Execution errors: 33
Zero-row results: 211
Proportion zero-row (overall): 0.384
Proportion zero-row (successful only): 0.409

### 6. ♻️ Query-Aware Augmentation of the Synthetic Sandbox

To reduce empty results when executing our SQL queries, we augment the synthetic data to be "query-aware." We identify queries that return zero rows and generate minimal, natural-looking data that satisfies their conditions.

#### Why this matters

* **Higher coverage**: More queries produce non-empty results, improving label quality for RFT
* **Minimal changes**: Only adds the data needed to satisfy queries
* **Natural data**: Generated rows look realistic and maintain referential integrity

#### How it works

1. Execute all queries and identify those returning zero rows
2. Process zero-result queries in batches of 10, grouped by involved tables
3. Use the LLM to generate 1-2 new rows per table that satisfy the query conditions
4. Insert rows, check which queries were fixed, and repeat until ≤10% return zero results
5. Remove any duplicate rows

The process tracks which queries have been attempted to avoid redundant processing and can retry stubborn queries up to 2 times.

> **Real World 🌍**: Run the cell below against your synthetic data and real queries. The code is domain-agnostic and will work with any SQL database schema.

```python  theme={null}
import os, json, re, time
import pandas as pd
import duckdb
from typing import List, Optional, Any, Dict, Type, Set
from pydantic import BaseModel, create_model
from fireworks import LLM
import datetime, decimal, uuid
from collections import defaultdict
from dotenv import load_dotenv

# --- Config ---
SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"
QUERIES_FILE_PATH = "data/generated_queries.json"

# --- Setup LLM ---
load_dotenv()
llm = LLM(
    model="accounts/fireworks/models/qwen3-coder-480b-a35b-instruct",
    deployment_type="serverless",
    api_key=os.getenv("FIREWORKS_API_KEY"),
)

# --- Schema helpers ---
def map_sql_type_to_python(sql_type: str) -> Type:
    s = str(sql_type).upper()
    if "DECIMAL" in s: return decimal.Decimal
    if any(k in s for k in ("DOUBLE","FLOAT","REAL")): return float
    if any(k in s for k in ("BIGINT","INT")): return int
    if any(k in s for k in ("VARCHAR","TEXT","STRING")): return str
    if "TIMESTAMP" in s: return datetime.datetime
    if "DATE" in s: return datetime.date
    if "TIME" in s: return datetime.time
    if "BOOLEAN" in s: return bool
    if any(k in s for k in ("BLOB","BYTEA")): return bytes
    if "UUID" in s: return uuid.UUID
    return object

with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con_ro:
    schema_df = con_ro.sql("DESCRIBE;").df()
schema_for_prompt = schema_df.to_markdown(index=False)

def extract_tables_from_query(sql: str) -> Set[str]:
    """Extract table names from SQL query."""
    # Remove comments
    sql = re.sub(r'--.*$', '', sql, flags=re.MULTILINE)
    sql = re.sub(r'/\*.*?\*/', '', sql, flags=re.DOTALL)
    
    tables = set()
    # Match FROM and JOIN clauses
    patterns = [
        r'(?:FROM|JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
        r'(?:FROM|JOIN)\s+"([^"]+)"',
        r'(?:FROM|JOIN)\s+`([^`]+)`',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, sql, re.IGNORECASE)
        tables.update(matches)
    
    # Filter out SQL keywords that might be captured
    sql_keywords = {'select', 'where', 'group', 'order', 'having', 'limit', 'as', 'on', 'and', 'or', 'not', 'in', 'exists'}
    tables = {t for t in tables if t.lower() not in sql_keywords}
    
    return tables

def table_columns(name: str) -> List[str]:
    row = schema_df[schema_df["name"] == name]
    if row.empty:
        return []
    return list(row.iloc[0]["column_names"])

def table_types(name: str) -> List[str]:
    row = schema_df[schema_df["name"] == name]
    if row.empty:
        return []
    return list(row.iloc[0]["column_types"])

def build_rows_payload_model(tables: List[str]) -> Type[BaseModel]:
    per_table_row_models: Dict[str, Type[BaseModel]] = {}
    for t in tables:
        cols = table_columns(t)
        types = table_types(t)
        if not cols:
            continue
        fields: Dict[str, Any] = {}
        for c, ty in zip(cols, types):
            fields[c] = (Optional[map_sql_type_to_python(ty)], None)
        per_table_row_models[t] = create_model(f"{t.capitalize()}Row", **fields)
    
    payload_fields: Dict[str, Any] = {}
    for t, row_model in per_table_row_models.items():
        payload_fields[t] = (List[row_model], [])
    
    if not payload_fields:
        return create_model("RowsPayloadFallback", rows=(List[dict], []))
    return create_model("RowsPayload", **payload_fields)

def count_rows(con, sql: str) -> int:
    try:
        return con.sql(f"SELECT COUNT(*) AS c FROM ({sql}) AS t").fetchone()[0]
    except Exception:
        return -1

def get_sample_data(con, table: str, limit: int = 3) -> List[dict]:
    """Get sample rows from a table for context."""
    try:
        df = con.sql(f'SELECT * FROM "{table}" LIMIT {limit}').df()
        return df.to_dict("records")
    except Exception:
        return []

# --- Load queries ---
with open(QUERIES_FILE_PATH, "r") as f:
    queries = json.load(f).get("queries", [])

total_q = len(queries)
print(f"Total queries: {total_q}")

# --- Parameters ---
TARGET_MAX_ZERO_PERCENT = 10
MAX_ITERATIONS = 20
BATCH_SIZE = 10  # Process up to 10 queries at once
MAX_ROWS_PER_TABLE_PER_BATCH = 2  # Generate at most 2 rows per table per batch

# Initial assessment
with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con_check:
    zero_indices = [i for i, q in enumerate(queries) if count_rows(con_check, q) == 0]
    initial_zero_count = len(zero_indices)
    print(f"Initial zero-result queries: {initial_zero_count}/{total_q} ({initial_zero_count/total_q*100:.1f}%)")

# Track which queries have been attempted
processed_query_indices = set()
retry_count = 0  # Track how many times we've cycled through all queries

iteration = 0
with duckdb.connect(SYNTHETIC_DB_PATH) as con:
    while iteration < MAX_ITERATIONS:
        iteration += 1
        
        # Get ALL current zero-result queries
        all_zero_indices = [i for i, q in enumerate(queries) if count_rows(con, q) == 0]
        zero_count = len(all_zero_indices)
        zero_percent = (zero_count / total_q * 100) if total_q else 0
        
        print(f"\n[Iteration {iteration}] Zero-result: {zero_count}/{total_q} ({zero_percent:.1f}%)")
        
        if zero_percent <= TARGET_MAX_ZERO_PERCENT or zero_count == 0:
            print(f"✅ Target achieved! {zero_percent:.1f}% <= {TARGET_MAX_ZERO_PERCENT}%")
            break
        
        # Get unprocessed zero-result queries
        unprocessed_zero_indices = [i for i in all_zero_indices if i not in processed_query_indices]
        
        # If we've processed all zero-result queries, reset to try stubborn ones again
        if not unprocessed_zero_indices and all_zero_indices:
            retry_count += 1
            print(f"  All zero-result queries have been attempted. Starting retry cycle #{retry_count}")
            processed_query_indices.clear()
            unprocessed_zero_indices = all_zero_indices
            
            # If we've done multiple retry cycles with no progress, stop
            if retry_count > 2:
                print(f"  Stopping after {retry_count} retry cycles")
                break
        
        # Take a batch of unprocessed queries
        batch_indices = unprocessed_zero_indices[:BATCH_SIZE]
        if not batch_indices:
            print(f"[Iteration {iteration}] No queries to process.")
            break
            
        batch_queries = [queries[i] for i in batch_indices]
        processed_query_indices.update(batch_indices)
        
        print(f"  Processing batch: queries {batch_indices[:3]}{'...' if len(batch_indices) > 3 else ''} ({len(batch_indices)} total)")
        
        # Group queries by their involved tables for efficient processing
        query_tables_map = defaultdict(list)
        for idx, q in zip(batch_indices, batch_queries):
            tables = extract_tables_from_query(q)
            if tables:
                # Create a key from sorted table names
                key = tuple(sorted(tables))
                query_tables_map[key].append((idx, q))
        
        if not query_tables_map:
            print(f"  No tables found in batch. Moving to next batch.")
            continue
        
        total_fixed = 0
        
        # Process each group of queries that share the same tables
        for table_tuple, query_list in query_tables_map.items():
            tables = list(table_tuple)
            query_indices = [idx for idx, _ in query_list]
            query_texts = [q for _, q in query_list]
            
            print(f"    Processing {len(query_list)} queries involving tables: {tables}")
            
            # Build Pydantic model
            RowsPayload = build_rows_payload_model(tables)
            rows_schema = RowsPayload.model_json_schema()
            
            # Limit rows per table
            props = rows_schema.get("properties", {})
            for t in list(props.keys()):
                spec = props.get(t, {})
                if isinstance(spec, dict) and spec.get("type") == "array":
                    spec["maxItems"] = min(MAX_ROWS_PER_TABLE_PER_BATCH, len(query_list))
            
            # Get sample data for context
            existing_samples = {}
            for t in tables:
                samples = get_sample_data(con, t, limit=5)
                if samples:
                    existing_samples[t] = samples
            
            # Analyze query patterns to understand what's needed
            query_analysis = []
            for q in query_texts[:3]:  # Analyze first 3 queries for brevity
                query_analysis.append(f"- {q}")
            
            system_prompt = """You are an expert at generating natural, realistic database records.
Generate minimal new rows that will make the provided SQL queries return results.
The data should be diverse, realistic, and consistent with the domain implied by the schema."""
            
            user_prompt = f"""
Given this DuckDB schema and SQL queries that return zero rows, generate the minimum number
of natural, realistic rows needed to make these queries return results.

**Database Schema:**
{schema_for_prompt}

**Tables to populate:** {json.dumps(tables)}

**Example existing data (for style/format reference):**
{json.dumps(existing_samples, indent=2, default=str) if existing_samples else "No existing samples available"}

**Queries that need to return results ({len(query_texts)} total):**
{chr(10).join(query_analysis)}
{f"... and {len(query_texts) - 3} more similar queries" if len(query_texts) > 3 else ""}

**Requirements:**
1. Generate at most {MAX_ROWS_PER_TABLE_PER_BATCH} rows per table
2. Make the data satisfy the WHERE conditions and JOINs in the queries
3. Use natural, realistic values appropriate for the domain
4. Maintain referential integrity between tables
5. Avoid duplicating existing IDs - generate new unique IDs
6. Create diverse data that satisfies multiple queries if possible

Return ONLY the JSON object with the new rows. No explanations.
""".strip()
            
            try:
                resp = llm.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    response_format={
                        "type": "json_schema",
                        "json_schema": {"name": "RowsPayload", "schema": rows_schema}
                    },
                    temperature=0.5,  # Some randomness for natural data
                )
                
                content = resp.choices[0].message.content
                if not content:
                    print(f"      Empty response from LLM")
                    continue
                
                payload = json.loads(content)
                
                # Insert generated rows
                rows_inserted = 0
                for t in tables:
                    rows = payload.get(t, [])
                    if not rows or not isinstance(rows, list):
                        continue
                    
                    # Convert to DataFrame
                    df = pd.DataFrame(rows[:MAX_ROWS_PER_TABLE_PER_BATCH])
                    cols = table_columns(t)
                    if not cols:
                        continue
                    
                    # Align columns
                    for c in cols:
                        if c not in df.columns:
                            df[c] = None
                    df = df[cols]
                    
                    # Insert new rows (avoiding exact duplicates)
                    try:
                        con.register("new_rows_df", df)
                        con.execute(f'INSERT INTO "{t}" SELECT * FROM new_rows_df EXCEPT SELECT * FROM "{t}"')
                        con.unregister("new_rows_df")
                        rows_inserted += len(df)
                    except Exception as e:
                        print(f"      Warning: Failed to insert into {t}: {e}")
                
                # Check how many queries were fixed
                fixed_in_group = 0
                for idx in query_indices:
                    if count_rows(con, queries[idx]) > 0:
                        fixed_in_group += 1
                
                print(f"      Inserted {rows_inserted} rows, fixed {fixed_in_group}/{len(query_list)} queries")
                total_fixed += fixed_in_group
                
            except Exception as e:
                print(f"      Error processing group: {e}")
                continue
            
            time.sleep(0.5)  # Rate limiting
        
        print(f"  [Iteration {iteration}] Total fixed in this iteration: {total_fixed} queries")
        
        # If we're in a retry cycle and made no progress, stop
        if retry_count > 0 and total_fixed == 0:
            print(f"  No progress made in retry cycle. Stopping.")
            break

# Final cleanup - remove exact duplicates
print("\n--- Final deduplication ---")
with duckdb.connect(SYNTHETIC_DB_PATH) as con:
    tables = con.sql("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_type = 'BASE TABLE' 
        AND table_schema = 'main'
    """).fetchall()
    
    for (table_name,) in tables:
        before = con.sql(f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
        con.execute(f'CREATE OR REPLACE TABLE "{table_name}" AS SELECT DISTINCT * FROM "{table_name}"')
        after = con.sql(f'SELECT COUNT(*) FROM "{table_name}"').fetchone()[0]
        if before != after:
            print(f"  {table_name}: removed {before - after} duplicate rows")

# Final report
with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con_read:
    final_zero_indices = [i for i, q in enumerate(queries) if count_rows(con_read, q) == 0]
    final_zero_count = len(final_zero_indices)
    final_zero_percent = (final_zero_count / total_q * 100) if total_q else 0
    
    print(f"\n{'='*60}")
    print(f"AUGMENTATION COMPLETE")
    print(f"{'='*60}")
    print(f"Initial zero-result: {initial_zero_count}/{total_q} ({initial_zero_count/total_q*100:.1f}%)")
    print(f"Final zero-result:   {final_zero_count}/{total_q} ({final_zero_percent:.1f}%)")
    print(f"Improvement:         {initial_zero_count - final_zero_count} queries now return results")
    
    if final_zero_percent <= TARGET_MAX_ZERO_PERCENT:
        print(f"\n✅ SUCCESS: Achieved target of ≤{TARGET_MAX_ZERO_PERCENT}% zero-result queries")
    else:
        print(f"\n⚠️  Partial success. Consider running again or adjusting parameters.")
        
    # Show a few examples of remaining zero-result queries if any
    if final_zero_count > 0 and final_zero_count <= 5:
        print(f"\nRemaining zero-result queries:")
        for idx in final_zero_indices[:5]:
            print(f"  [{idx}]: {queries[idx][:100]}...")
```

### 7. 🎯 Execute Queries to Get Ground-Truth Answers

Now we will act as the "system" and run the queries we just generated against our synthetic sandbox. The output of each query is the **ground-truth result**. During Reinforcement Fine-Tuning, our model will be rewarded if the SQL it writes produces this exact same result.

#### Why RFT is a good choice for a text-to-SQL use-case

In RFT, the model explores the space of possible SQL queries during fine-tuning; the reward signal comes from comparing the result of executing the model's output SQL queries against the ground truth expected results. This is fundamentally different from SFT, where the model learns to mimic the exact SQL syntax. With RFT:

* Multiple SQL queries can be "correct" if they produce the same result
* The model learns to reason about the problem rather than memorize solutions
* Edge cases and query optimization patterns can emerge naturally

> **Real World 🌍**: You would run your real historical queries against the synthetic database we previously created. The correctness of the data is not a concern here, as our aim is to see what a correct query would have generated, so we can compare it to our LLM's generations during the RFT process.

```python  theme={null}
import duckdb
import json
import pandas as pd

# --- 1. Define File Paths ---
SYNTHETIC_DB_PATH = "data/synthetic_openflights.db"
QUERIES_FILE_PATH = "data/generated_queries.json"
GROUND_TRUTH_FILE_PATH = "data/ground_truth_results.jsonl"

# Thresholds to drop overly large results
MAX_RESULT_ROWS = 1000          # skip if result has more than this many rows
MAX_RESULT_BYTES = 100_000      # ~0.1MB; skip if JSON payload exceeds this

# --- 2. Load Generated Queries ---
with open(QUERIES_FILE_PATH, 'r') as f:
    queries_data = json.load(f)
    queries_to_execute = queries_data.get("queries", [])

print(f"Loaded {len(queries_to_execute)} queries to execute.")

# --- 3. Execute Queries and Store Results ---
ground_truth_results = []
successful_executions = 0
failed_executions = 0
oversized_skipped = 0

print("Executing queries against the synthetic database...")
with duckdb.connect(SYNTHETIC_DB_PATH, read_only=True) as con:
    for query in queries_to_execute:
        try:
            result_df = con.sql(query).df()

            # Replace any NaN/NaT values with None, which serializes to JSON `null`
            result_df = result_df.astype(object).where(pd.notna(result_df), None)
            result_records = result_df.to_dict('records')

            # Skip examples that are "much too wide"
            if len(result_records) > MAX_RESULT_ROWS:
                oversized_skipped += 1
                continue
            # Size-based guard (in bytes)
            payload_bytes = len(json.dumps(result_records, ensure_ascii=False).encode("utf-8"))
            if payload_bytes > MAX_RESULT_BYTES:
                oversized_skipped += 1
                continue

            ground_truth_results.append({
                "query": query,
                "result": result_records
            })
            successful_executions += 1
        except Exception as e:
            print(f"⚠️  Skipping query due to execution error: {query}\n   Error: {e}\n")
            failed_executions += 1

print(f"\nExecution complete. Success: {successful_executions}, Skipped (oversized): {oversized_skipped}, Failed: {failed_executions}.")

# --- 4. Save the Ground-Truth Data ---
with open(GROUND_TRUTH_FILE_PATH, 'w') as f:
    for entry in ground_truth_results:
        f.write(json.dumps(entry) + '\n')

print(f"\n✅ Successfully saved {len(ground_truth_results)} ground-truth results to `{GROUND_TRUTH_FILE_PATH}`.")

# --- 5. Print an Example ---
if ground_truth_results:
    print("\n--- Example ground_truth_results dataset entry ---")
    print(json.dumps(ground_truth_results[0], indent=2))
```

### 8. 💬 Generate Natural Language Questions for Final RFT Training Data

We now have pairs of `(SQL Query, Ground-Truth Result)`. The final piece missing from our training data is the user's input: a question in natural language. This is because our final goal is to use RFT to tune an LLM to map from a natural language question to a SQL query, having the reward signal be the actual result of the query, rather than just the query itself. This is important because there are many ways to write the same SQL query that yield the same, correct result.

#### Thus, the complete training loop will look like this:

1. User asks: *"Which countries have the most airlines?"*
2. Model generates: *SQL query*
3. System executes: *Query against database*
4. Reward calculation: *Does result match ground truth?*
5. Model update: *Reinforce successful strategies*

Thus, we will use an LLM once again to translate our "historical" SQL queries into plausible questions a business user might ask, corresponding to that query. This will yield our final training dataset in the format: `(Natural Language Question, SQL Query, Ground-Truth Result)`. Note that the SQL queries themselves will not be used as part of the RFT job itself, but are useful for debugging our evaluation function (more details in a later section).

> **Real World 🌍**: You might not need this step! If you have logs that already link user questions to the queries they ran (e.g., from a BI tool's search bar), you can use those directly. If not, this LLM-based translation is a powerful technique to bootstrap your training data.

```python  theme={null}
import json
import time
import jsonlines
from typing import List
import random
from fireworks import LLM
import os

# --- 1. Define File Paths and Parameters ---
llm = LLM(model="accounts/fireworks/models/qwen3-coder-480b-a35b-instruct", deployment_type="serverless", api_key=os.getenv("FIREWORKS_API_KEY"))
GROUND_TRUTH_FILE_PATH = "data/ground_truth_results.jsonl"
FINAL_TRAINING_DATA_PATH = "data/final_rft_sql_train_data.jsonl"
FINAL_TEST_DATA_PATH = "data/final_rft_sql_test_data.jsonl"

# --- 2. Load Ground-Truth Data ---
query_result_pairs = []
with jsonlines.open(GROUND_TRUTH_FILE_PATH) as reader:
    for obj in reader:
        query_result_pairs.append(obj)

print(f"Loaded {len(query_result_pairs)} query-result pairs.")

# --- 3. Use LLM to Generate Natural Language Questions ---
nl_generation_prompt_template = """
You are an expert data analyst who is great at translating SQL queries into plain English.
Based on the database schema and the provided SQL query, what is a natural language question a business user would ask to get this information?
Ensure that the question is precise enough to accurately map to the corresponding SQL query.

**Database Schema:**
{schema_for_prompt}

**SQL Query:**
{query}

Provide only the user's question, without any preamble or explanation.
""".strip()

# The system prompt that will be included in the final training data for the RFT job.
# It gives the model its instructions at inference time.
rft_system_prompt = f"""
You are an expert SQL data analyst.
Your task is to write a single, valid DuckDB SQL query to answer the user's question, based on the provided database schema.
Write only the raw SQL query text and nothing else (i.e., no markdown formatting); your output should be a directly executable valid SQL query.
Make sure your queries do not return duplicate rows (i.e., GROUP BY all columns that are not aggregate functions).
Ensure the generated SQL is valid for DuckDB.

**Database Schema:**
{schema_for_prompt}
""".strip()

final_generated_data = []
print(f"Generating natural language questions and formatting for RFT for {len(query_result_pairs)} queries...")

for i, pair in enumerate(query_result_pairs):
    print(f" - Processing query {i+1}/{len(query_result_pairs)}...")
    query = pair['query']
    ground_truth = pair['result']
    nl_generation_prompt = nl_generation_prompt_template.format(schema_for_prompt=schema_for_prompt, query=query)
    
    response = llm.chat.completions.create(
        messages=[{"role": "user", "content": nl_generation_prompt}],
        temperature=0.5
    )
    
    nl_question = response.choices[0].message.content
    if nl_question:  # Only include the entry if the LLM generated a question
        # Assemble the final data structure
        rft_entry = {
            "messages": [
                {"role": "system", "content": rft_system_prompt},
                {"role": "user", "content": nl_question.strip()},
                {"role": "assistant", "content": query}
            ],
            "ground_truth": ground_truth  # The ground-truth result for the evaluator
        }
        final_generated_data.append(rft_entry)
    
    time.sleep(0.5) # Be nice to the API

# --- 4. Shuffle and Split the Dataset ---
print(f"\nGenerated {len(final_generated_data)} total examples.")

# Filter out entries where 'ground_truth' is an empty list
original_count = len(final_generated_data)
final_generated_data = [entry for entry in final_generated_data if entry.get("ground_truth")]
print(f"Filtered out {original_count - len(final_generated_data)} examples with empty ground truth.")

print(f"Now splitting the remaining {len(final_generated_data)} examples into train and test sets.")

random.seed(42)
random.shuffle(final_generated_data)

split_index = int(len(final_generated_data) * 0.8)
train_data = final_generated_data[:split_index]
test_data = final_generated_data[split_index:]

print(f"Train set size: {len(train_data)}")
print(f"Test set size: {len(test_data)}")

# --- 5. Save the Final RFT-Ready Datasets ---
with jsonlines.open(FINAL_TRAINING_DATA_PATH, mode='w') as writer:
    writer.write_all(train_data)
print(f"\n✅ Successfully saved training dataset to `{FINAL_TRAINING_DATA_PATH}`.")

with jsonlines.open(FINAL_TEST_DATA_PATH, mode='w') as writer:
    writer.write_all(test_data)
print(f"✅ Successfully saved test dataset to `{FINAL_TEST_DATA_PATH}`.")

# --- 6. Print an Example ---
if train_data:
    print("\n--- Example RFT training entry ---")
    print(json.dumps(train_data[0], indent=2))
```

### 9. 🛰️ Deploy an MCP Server for the Synthetic Data

Now, we'll start a remote server that speaks the Model Context Protocol (MCP). This server will wrap our synthetic DuckDB database, providing a standardized way for any external tool—in our case, the Fireworks RFT evaluator—to interact with it.

#### What is MCP?

The Model Context Protocol is an open standard that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals, MCP provides a standardized way to connect AI models to various data sources and tools.

Key benefits:

* **Flexibility**: Works with any data source or tool
* **Standardization**: One protocol for all integrations instead of custom APIs for each tool; MCP servers for many applications are readily available

> Real World 🌍: This pattern is directly applicable. You would run a similar MCP server to provide a secure, read-only interface to a production database replica or a data warehouse, allowing the fine-tuning process to happen without granting direct database credentials to the training environment.

9. a) Create a server script in this project's root directory (`run_mcp_server.py`). This Python script starts our database server. It is configured to be read-only.

```python  theme={null}
    import os, contextlib, uvicorn
    from starlette.applications import Starlette
    from starlette.routing import Mount
    from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
    from mcp_server_motherduck import build_application

    DB = "data/synthetic_openflights.db"          # ← path from previous steps
    PORT = int(os.environ.get("PORT", 8080))        # Cloud Run injects $PORT

    # 1️⃣ Build the core SQL-aware MCP server (read-only for safety).
    server, _ = build_application(db_path=DB, read_only=True)

    # 2️⃣ Wrap it so HTTP clients can talk to it (ASGI handler).
    sess = StreamableHTTPSessionManager(app=server, event_store=None, stateless=True)

    async def handler(scope, receive, send):
        await sess.handle_request(scope, receive, send)

    @contextlib.asynccontextmanager
    async def lifespan(app):
        async with sess.run():
            yield                                        # keep sessions alive

    # 3️⃣ Starlette turns that handler into a full ASGI app Uvicorn can serve.
    app = Starlette(routes=[Mount("/mcp", app=handler)], lifespan=lifespan)

    if __name__ == "__main__":
        print(f"🔥 MCP endpoint → http://0.0.0.0:{PORT}/mcp")
        uvicorn.run(app, host="0.0.0.0", port=PORT)
```

### 10. ☁️ Set Up Google Cloud CLI & .gcloudignore

We'll first set up the Google Cloud CLI and authenticate. Google Cloud Run provides an easy way to deploy containerized applications without managing infrastructure.

> **Real World 🌍**\
> You would follow along here in the same way. Cloud Run is ideal for MCP servers because it auto-scales based on demand (down to zero when not in use, thus charging only for actual usage).

10. a) **Install** the SDK (macOS/Linux):

    ```bash  theme={null}
    curl -sSL https://sdk.cloud.google.com | bash
    exec -l $SHELL  # reload shell so 'gcloud' is available
    ```

11. b) **Log in** (creates local access token):
    ```bash  theme={null}
    gcloud auth login
    ```

12. c) **Set your active project desired gcloud project**:
    ```bash  theme={null}
    gcloud config set project < YOUR_PROJECT_ID >  # set up project in gcloud console before running this if not already done
    ```

### 11. 📦 Containerize & Deploy the MCP Server

We’ll build a Docker image and push it straight to Cloud Run.\
Remember to replace **`YOUR_PROJECT_ID`** with the project you actually want to bill.

> **Real World 🌍**\
> You would follow along in the same way here.

11. a) Create `mcp_requirements.txt` containing the following:

```bash  theme={null}
mcp
mcp-server-motherduck
duckdb
uvicorn
starlette
```

11. b) Create a `Dockerfile` (no extension) containing the following

```bash  theme={null}
base
FROM python:3.11-slim
WORKDIR /app

COPY mcp_requirements.txt .
RUN pip install --no-cache-dir -r mcp_requirements.txt

COPY run_mcp_server.py .
COPY data/synthetic_openflights.db ./data/

EXPOSE 8080

CMD ["python", "run_mcp_server.py"]
```

11. c) Create a .gcloudignore file in your root dir (to only deploy files needed for MCP server) containing:

```bash  theme={null}
# .gcloudignore

# 1. Ignore EVERYTHING in the directory by default.
*

# 2. Now, create exceptions for ONLY the files needed by the Dockerfile.
# The "!" character means "do not ignore this file".

# The Dockerfile itself is needed for the build process.
!Dockerfile

# The files explicitly copied by your Dockerfile:
!mcp_requirements.txt
!run_mcp_server.py

# 3. To include a specific file in a subdirectory, use this
#    three-line pattern to un-ignore the directory, re-ignore its
#    contents, and then un-ignore the specific file.
!data/
data/*
!data/synthetic_openflights.db
```

11. d) Deploy your MCP server as a Cloud Run app by running (from your project root):

```bash  theme={null}
gcloud run deploy mcp-sql-rft-server \
  --source . \
  --region < YOUR_GCP_REGION > \
  --project < YOUR_GCP_PROJECT_ID > \
  --allow-unauthenticated \
  --port 8080
```

Note this will create a default Docker repository called `cloud-run-source-deploy`; press Y to continue when prompted.

11. e) Test that your MCP server is working as expected by running the following from your terminal:
12. e) i. To get your MCP server's URL:

```bash  theme={null}
gcloud run services describe mcp-sql-rft-server \
--project < YOUR_GCP_PROJECT_ID > \
--region < YOUR_GCP_REGION > \
--format="value(status.url)"
```

11. e) ii. (optional) To check the names of the MCP server's available tools:

```bash  theme={null}
curl -X POST "< YOUR_MCP_SERVER_URL_FROM_STEP_i >/mcp/" \
-H "Content-Type: application/json" \
-H "Accept: application/json, text/event-stream" \
-d '{
    "id": "list-tools-1",
    "jsonrpc": "2.0",
    "method": "tools/list",
    "params": {
        "session": {"id": "test-from-my-laptop"}
    }
}'
```

> Note that the above is a generally useful way to check an MCP server's tools.
> In this case, the tool of interest is the "query" tool.

11. e) iii. To send a test request to the MCP server:

```bash  theme={null}
curl -X POST "< YOUR_MCP_SERVER_URL_FROM_STEP_i >/mcp/" \
-H "Content-Type: application/json" \
-H "Accept: application/json, text/event-stream" \
-d '{
    "id": "query-1",
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "session": {"id": "test-from-my-laptop"},
        "name": "query",
        "arguments": {
            "query": "SELECT COUNT(*) FROM airlines;"
        }
    }
}'
```

### 12. 🔍 Define an evaluation function for RFT

Here, we define an `evaluate` function for RFT, which will interface with our MCP server. Note that you will not directly execute the function here, but will use it as part of the Fireworks Evaluations UI.

#### Understanding the Evaluation Function:

The evaluation function is the heart of RFT. It:

1. Receives the model's generated SQL query
2. Executes it against the real database (via MCP)
3. Compares the result with ground truth
4. Returns a reward score (0 or 1)

This binary reward signal drives the reinforcement learning process. The model learns through trial and error which SQL patterns lead to correct results.

Key design decisions:

* **Exact match comparison**: We normalize values and sort rows to handle different but equivalent result orderings
* **Robust error handling**: SQL syntax errors or execution failures return a score of 0
* **Detailed reasoning**: The function returns explanatory messages for debugging

Ensure that you set MCP\_SERVER\_URL to be your actual MCP server URL from step 11. e) i.

> **Real World 🌍**\
> You would follow along in the same way here. The evaluation function could also be further customized, with, for example:
>
> * Partial credit for near-correct answers
> * Performance-based rewards (faster queries get higher scores)

```python  theme={null}
import requests
import json
import math

MCP_SERVER_URL = None  # <--- PUT MCP SERVER URL HERE without the /mcp/ suffix at the end

def evaluate(messages: list[dict], ground_truth: list[dict], **kwargs) -> dict:
    """
    Evaluates the model's generated SQL query by executing it against a live
    MCP server and comparing the result with the ground_truth.
    """
    
    def parse_duckdb_ascii_table(table_string: str) -> list[dict]:
        """
        Parses a DuckDB-style ASCII table string into a list of dictionaries.
        This version robustly handles 'NULL' values and empty strings.
        """
        lines = table_string.strip().split('\n')
        content_lines = [line for line in lines if line.strip() and not line.startswith('+')]
        if len(content_lines) < 2:
            return []
        
        header_raw = [h.strip() for h in content_lines[0].split('|')[1:-1]]
        data_lines = content_lines[1:]
        
        if len(data_lines) > 0:
            try:
                first_data_values = [v.strip() for v in data_lines[0].split('|')[1:-1]]
                if len(first_data_values) == len(header_raw) and all(v.isupper() for v in first_data_values):
                    data_lines = data_lines[1:]
            except IndexError:
                pass

        rows = []
        for line in data_lines:
            try:
                values_raw = [v.strip() for v in line.split('|')[1:-1]]
                if len(values_raw) == len(header_raw):
                    row_dict = {}
                    for i, header in enumerate(header_raw):
                        value_str = values_raw[i]
                        if value_str.upper() == 'NULL' or value_str == '':
                            row_dict[header] = None
                            continue
                        
                        try:
                            if '.' in value_str:
                                row_dict[header] = float(value_str)
                            else:
                                row_dict[header] = int(value_str)
                        except (ValueError, TypeError):
                            row_dict[header] = value_str
                    rows.append(row_dict)
            except IndexError:
                continue
        return rows

    # --- 1. Get MCP Server URL from Environment Variables ---
    mcp_server_url = MCP_SERVER_URL
    if not mcp_server_url:
        return {"score": 0, "is_score_valid": False, "reason": "FATAL: MCP_SERVER_URL environment variable is not set."}

    # --- 2. Get the SQL query from the model's response ---
    sql_query = messages[-1]['content'].strip()
    if not sql_query:
        return {"score": 0, "reason": "Model returned an empty response."}

    # --- 3. Execute the Query against the MCP Server ---
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    payload = {
        "id": "eval-query-1", "jsonrpc": "2.0", "method": "tools/call",
        "params": {"session": {"id": "stateless-eval-session"}, "name": "query", "arguments": {"query": sql_query}}
    }
    try:
        with requests.post(f"{mcp_server_url}/mcp/", headers=headers, json=payload, timeout=15, stream=True) as response:
            response.raise_for_status()
            response_data = None
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        json_part = decoded_line[len('data:'):].strip()
                        if json_part:
                            response_data = json.loads(json_part)
                            break
            if response_data is None:
                return {"score": 0, "reason": "Could not find JSON data in event stream response from MCP server."}

        if "error" in response_data:
            return {"score": 0, "reason": f"SQL execution failed. Error: {response_data['error'].get('message', 'Unknown')}"}

        ascii_table = response_data['result']['content'][0]['text']
        predicted_rows = parse_duckdb_ascii_table(ascii_table)

    except requests.exceptions.RequestException as e:
        return {"score": 0, "reason": f"Network error calling MCP server: {e}"}
    except json.JSONDecodeError as e:
        return {"score": 0, "reason": f"JSON decode error from server response: {e}"}
    except (KeyError, IndexError):
        return {"score": 0, "reason": f"Failed to parse predicted result from MCP server response structure. Data found: {json.dumps(response_data)}"}
    except Exception as e:
        return {"score": 0, "reason": f"An unexpected error occurred during query execution: {e}"}

    # --- 4. Process Ground Truth ---
    if not isinstance(ground_truth, list):
        return {"score": 0, "is_score_valid": False, "reason": f"FATAL: ground_truth is not a list as expected. Got type: {type(ground_truth)}"}
    ground_truth_rows = ground_truth


    # --- 5. Comparison Logic ---
    def normalize_and_stringify(v):
        """
        Normalizes numbers and None before string conversion.
        """
        if v is None:
            return str(v)
        
        if isinstance(v, float) and not math.isinf(v) and not math.isnan(v) and v == int(v):
            v = int(v)
        return str(v)

    try:
        gt_values = sorted([sorted(map(normalize_and_stringify, row.values())) for row in ground_truth_rows])
        predicted_values = sorted([sorted(map(normalize_and_stringify, row.values())) for row in predicted_rows])

        if gt_values == predicted_values:
            score = 1
            reason = "Success: The SQL query produced the exact expected result."
        else:
            score = 0
            gt_json = json.dumps(ground_truth_rows)
            pred_json = json.dumps(predicted_rows)
            reason = f"Incorrect result. Expected (from ground_truth): {gt_json}. Got (from query): {pred_json}."
    
    except Exception as e:
        return {"score": 0, "reason": f"Error during result comparison: {e}"}

    return {"score": score, "reason": reason}
```

### 13. 🧪 Test English -> SQL of a base model without fine-tuning

Here, we test a base model's ability to generate SQL from a natural language question on a single example from our training data.

This is a quick sanity check that:

1. **Verifies your MCP server is working**: Ensures the server is accessible and can execute queries
2. **Tests the full pipeline**: Confirms that the flow from natural language → SQL generation → execution → result parsing works end-to-end
3. **Shows a concrete example**: Demonstrates what happens when an off-the-shelf model tries to answer a question about your specific database

The test process:

1. Load one example from your training data (by default, the first row)
2. Feed the natural language question to a base model (e.g., Llama 3.1 8B)
3. Execute whatever SQL the model generates against your MCP server
4. Compare the result to the ground truth
5. Print whether it succeeded or failed

What to expect:

* The base model might get it right! Simple queries often work.
* Or, you'll see some kind of failure: wrong column names, missing aliases, incorrect syntax, etc.
* Either outcome is fine; this is just a quick test to see the model in action before fine-tuning.

To try different examples, change `ROW_INDEX_TO_TEST` to test other rows from your dataset.

Ensure that you set MCP\_SERVER\_URL to be your actual MCP server URL from step 11. e) i.

> **Real World 🌍**\
> You can follow along in the same way here. This single-example test is just a quick way to verify everything is wired up correctly before launching the more expensive fine-tuning job.

```python  theme={null}
import requests
import json
import os
from fireworks import LLM

# --- 1. SETUP: Define API keys, server URLs, and the model to use ---

# IMPORTANT: Make sure your FIREWORKS_API_KEY is set as an environment variable.
# You can get one from https://fireworks.ai
if "FIREWORKS_API_KEY" not in os.environ:
    print("FATAL: FIREWORKS_API_KEY environment variable not set.")
    # If not set, you can hardcode it here for testing, but this is not recommended:
    # os.environ["FIREWORKS_API_KEY"] = "YOUR_API_KEY_HERE"

# The model we'll use to generate the SQL. This acts as our "base" model.
LLM_MODEL = "accounts/fireworks/models/llama-v3p1-8b-instruct"
llm = LLM(model=LLM_MODEL, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))

# The URL for your running MCP server.
MCP_SERVER_URL = None  # PUT MCP SERVER URL HERE without the /mcp/ suffix at the end


# --- 2. LOAD THE EXAMPLE DATA ---

# This is the example data you provided.
DATASET_FILE_PATH = "data/final_rft_sql_train_data.jsonl"
ROW_INDEX_TO_TEST = 0  # 0 is the first row, 1 is the second row, etc.

EXAMPLE_DATA = None
try:
    with open(DATASET_FILE_PATH, 'r') as f:
        for i, line in enumerate(f):
            if i == ROW_INDEX_TO_TEST:
                EXAMPLE_DATA = json.loads(line)
                break
    
    if EXAMPLE_DATA is None:
        with open(DATASET_FILE_PATH, 'r') as f:
            line_count = sum(1 for line in f)
        raise IndexError(f"row index {ROW_INDEX_TO_TEST} is out of bounds for file with {line_count} rows.")

    print(f"Successfully loaded row {ROW_INDEX_TO_TEST} from '{DATASET_FILE_PATH}'.\n")
    print(EXAMPLE_DATA)
    print()

except Exception as e:
    print(f"Warning: Could not load from file. Reason: {e}")

# If loading from file failed for any reason, use the hardcoded fallback data.
if EXAMPLE_DATA is None:
    print("Using hardcoded fallback EXAMPLE_DATA.\n")
    EXAMPLE_DATA = {
        "messages": [
            {"role": "system", "content": "\nYou are an expert SQL data analyst. Your task is to write a single, valid DuckDB SQL query to answer the user's question, based on the provided database schema. Do not provide any explanation or text other than the SQL query itself.\n\n**Database Schema:**\n| database              | schema   | name      | column_names                                                               | column_types                                                          | temporary   |\n|:----------------------|:---------|:----------|:---------------------------------------------------------------------------|:----------------------------------------------------------------------|:------------|\n| synthetic_openflights | main     | airlines  | ['airline_id' 'name' 'alias' 'iata' 'icao' 'callsign' 'country' 'active']  | ['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' | False       |\n|                       |          |           |                                                                            |  'VARCHAR']                                                           |             |\n| synthetic_openflights | main     | airports  | ['airport_id' 'name' 'city' 'country' 'iata' 'icao' 'latitude' 'longitude' | ['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'DOUBLE'  | False       |\n|                       |          |           |  'altitude' 'timezone' 'dst' 'tz_db' 'type' 'source']                      |  'DOUBLE' 'BIGINT' 'DOUBLE' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR']  |             |\n| synthetic_openflights | main     | countries | ['name' 'iso_code' 'dafif_code']                                           | ['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False       |\n| synthetic_openflights | main     | planes    | ['name' 'iata' 'icao']                                                     | ['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False       |\n| synthetic_openflights | main     | routes    | ['airline' 'airline_id' 'source_airport' 'source_airport_id'               | ['VARCHAR' 'BIGINT' 'VARCHAR' 'BIGINT' 'VARCHAR' 'BIGINT' 'VARCHAR'   | False       |\n|                       |          |           |  'destination_airport' 'destination_airport_id' 'codeshare' 'stops'        |  'BIGINT' 'VARCHAR']                                                  |             |\n|                       |          |           |  'equipment']                                                              |                                                                       |             |\n"},
            {"role": "user", "content": "Which countries have the most airlines, and how many airlines are there in each country, listed in descending order by the number of airlines and then alphabetically by country name?"},
            {"role": "assistant", "content": "SELECT country, COUNT(*) AS airline_count FROM airlines GROUP BY country ORDER BY airline_count DESC, country ASC"}
        ],
        "ground_truth": [{"country": "Canada", "airline_count": 10}, {"country": "Sweden", "airline_count": 10}, {"country": "Kenya", "airline_count": 9}, {"country": "United States", "airline_count": 9}, {"country": "Australia", "airline_count": 8}, {"country": "Spain", "airline_count": 6}, {"country": "Italy", "airline_count": 4}, {"country": "Switzerland", "airline_count": 4}, {"country": "Finland", "airline_count": 3}, {"country": "France", "airline_count": 3}, {"country": "Mexico", "airline_count": 3}, {"country": "Costa Rica", "airline_count": 2}, {"country": "Germany", "airline_count": 2}, {"country": "Iceland", "airline_count": 2}, {"country": "Ireland", "airline_count": 2}, {"country": "Japan", "airline_count": 2}, {"country": "Norway", "airline_count": 2}, {"country": "Singapore", "airline_count": 2}, {"country": "United Kingdom", "airline_count": 2}, {"country": "Argentina", "airline_count": 1}, {"country": "Brazil", "airline_count": 1}, {"country": "China", "airline_count": 1}, {"country": "Egypt", "airline_count": 1}, {"country": "Fiji", "airline_count": 1}, {"country": "Greece", "airline_count": 1}, {"country": "India", "airline_count": 1}, {"country": "Jordan", "airline_count": 1}, {"country": "Netherlands", "airline_count": 1}, {"country": "New Zealand", "airline_count": 1}, {"country": "Portugal", "airline_count": 1}, {"country": "Saudi Arabia", "airline_count": 1}, {"country": "South Africa", "airline_count": 1}, {"country": "Thailand", "airline_count": 1}, {"country": "United Arab Emirates", "airline_count": 1}]
    }

# Extract the prompts and ground truth from the data
system_prompt = EXAMPLE_DATA["messages"][0]["content"]
user_prompt = EXAMPLE_DATA["messages"][1]["content"]
GROUND_TRUTH_ROWS = EXAMPLE_DATA["ground_truth"]

# --- 3. HELPER FUNCTION: To parse the server's ASCII table response ---

def parse_duckdb_ascii_table(table_string: str) -> list[dict]:
    """
    Parses a DuckDB-style ASCII table string into a list of dictionaries.
    This version robustly handles 'NULL' values and empty strings.
    """
    lines = table_string.strip().split('\n')
    content_lines = [line for line in lines if line.strip() and not line.startswith('+')]
    if len(content_lines) < 2:
        return []
    
    header_raw = [h.strip() for h in content_lines[0].split('|')[1:-1]]
    data_lines = content_lines[1:]
    
    if len(data_lines) > 0:
        try:
            first_data_values = [v.strip() for v in data_lines[0].split('|')[1:-1]]
            if len(first_data_values) == len(header_raw) and all(v.isupper() for v in first_data_values):
                data_lines = data_lines[1:]
        except IndexError:
            pass

    rows = []
    for line in data_lines:
        try:
            values_raw = [v.strip() for v in line.split('|')[1:-1]]
            if len(values_raw) == len(header_raw):
                row_dict = {}
                for i, header in enumerate(header_raw):
                    value_str = values_raw[i]
                    if value_str.upper() == 'NULL' or value_str == '':
                        row_dict[header] = None
                        continue
                    
                    try:
                        if '.' in value_str:
                            row_dict[header] = float(value_str)
                        else:
                            row_dict[header] = int(value_str)
                    except (ValueError, TypeError):
                        row_dict[header] = value_str
                rows.append(row_dict)
        except IndexError:
            continue
    return rows

# --- 4. GENERATE SQL QUERY USING THE LLM ---

print("="*20)
print("LLM QUERY GENERATION")
print("="*20)

model_generated_sql = ""
try:
    print(f"User prompt: {user_prompt}")
    print(f"Ground truth: {GROUND_TRUTH_ROWS}")
    print(f"Calling model '{LLM_MODEL}' to generate SQL query...")
    
    messages_for_llm = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    response = llm.chat.completions.create(
        model=LLM_MODEL,
        messages=messages_for_llm,
        temperature=0.0  # Set to 0 for deterministic output
    )
    
    model_generated_sql = response.choices[0].message.content.strip()
    print("\nModel Generated SQL Query:")
    print(model_generated_sql)
    
except Exception as e:
    print(f"\nAN ERROR OCCURRED during LLM call: {e}")


# --- 5. EXECUTE GENERATED QUERY ON MCP SERVER ---

predicted_rows = []
if model_generated_sql:
    try:
        print("\n" + "="*20)
        print("MCP SERVER EXECUTION")
        print("="*20)
        print(f"Sending query to MCP server...")
        
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        payload = {
            "id": "eval-query-1", "jsonrpc": "2.0", "method": "tools/call",
            "params": {"session": {"id": "stateless-eval-session"}, "name": "query", "arguments": {"query": model_generated_sql}}
        }

        with requests.post(f"{MCP_SERVER_URL}/mcp/", headers=headers, json=payload, timeout=20, stream=True) as response:
            response.raise_for_status()
            response_data = None
            for line in response.iter_lines():
                if line and line.decode('utf-8').startswith('data:'):
                    json_part = line.decode('utf-8')[len('data:'):].strip()
                    if json_part:
                        response_data = json.loads(json_part)
                        break
            
            if response_data is None: raise RuntimeError("No JSON data in event stream.")
            if "error" in response_data: raise RuntimeError(f"SQL Error: {response_data['error'].get('message', 'Unknown')}")

            ascii_table = response_data['result']['content'][0]['text']
            predicted_rows = parse_duckdb_ascii_table(ascii_table)
            print("\nParsed Result from Server:")
            print(json.dumps(predicted_rows, indent=2))

    except Exception as e:
        print(f"\nAN ERROR OCCURRED during MCP call: {e}")

# --- 6. FINAL COMPARISON ---
print("\n" + "="*20)
print("COMPARISON")
print("="*20)

if not predicted_rows:
    print("Skipping comparison: no rows returned from query or an error occurred.")
else:
    gt_values = sorted([sorted(map(str, row.values())) for row in GROUND_TRUTH_ROWS])
    predicted_values = sorted([sorted(map(str, row.values())) for row in predicted_rows])

    if gt_values == predicted_values:
        print("\n✅ GOOD RESULT: The base model generated SQL that produced the correct data.\n")
    else:
        print("\n❌ BAD RESULT: The base model's SQL produced different data than expected.\n")
        print("This is often the intended outcome when testing a base model, as it highlights what fine-tuning needs to correct.")
```

```text  theme={null}
    Successfully loaded row 0 from 'data/final_rft_sql_train_data.jsonl'.
    
    {'messages': [{'role': 'system', 'content': "You are an expert SQL data analyst.\nYour task is to write a single, valid DuckDB SQL query to answer the user's question, based on the provided database schema.\nWrite only the raw SQL query text and nothing else (i.e., no markdown formatting); your output should be a directly executable valid SQL query.\nMake sure your queries do not return duplicate rows (i.e., GROUP BY all columns that are not aggregate functions).\nEnsure the generated SQL is valid for DuckDB.\n\n**Database Schema:**\n| database              | schema   | name      | column_names                                                               | column_types                                                          | temporary   |\n|:----------------------|:---------|:----------|:---------------------------------------------------------------------------|:----------------------------------------------------------------------|:------------|\n| synthetic_openflights | main     | airlines  | ['airline_id' 'name' 'alias' 'iata' 'icao' 'callsign' 'country' 'active']  | ['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' | False       |\n|                       |          |           |                                                                            |  'VARCHAR']                                                           |             |\n| synthetic_openflights | main     | airports  | ['airport_id' 'name' 'city' 'country' 'iata' 'icao' 'latitude' 'longitude' | ['BIGINT' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'DOUBLE'  | False       |\n|                       |          |           |  'altitude' 'timezone' 'dst' 'tz_db' 'type' 'source']                      |  'DOUBLE' 'BIGINT' 'DOUBLE' 'VARCHAR' 'VARCHAR' 'VARCHAR' 'VARCHAR']  |             |\n| synthetic_openflights | main     | countries | ['name' 'iso_code' 'dafif_code']                                           | ['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False       |\n| synthetic_openflights | main     | planes    | ['name' 'iata' 'icao']                                                     | ['VARCHAR' 'VARCHAR' 'VARCHAR']                                       | False       |\n| synthetic_openflights | main     | routes    | ['airline' 'airline_id' 'source_airport' 'source_airport_id'               | ['VARCHAR' 'BIGINT' 'VARCHAR' 'BIGINT' 'VARCHAR' 'BIGINT' 'VARCHAR'   | False       |\n|                       |          |           |  'destination_airport' 'destination_airport_id' 'codeshare' 'stops'        |  'BIGINT' 'VARCHAR']                                                  |             |\n|                       |          |           |  'equipment']                                                              |                                                                       |             |"}, {'role': 'user', 'content': 'Which active airlines in India have the most routes, and how many routes does each operate?'}, {'role': 'assistant', 'content': "SELECT a.name AS airline_name, COUNT(r.airline_id) AS route_count FROM airlines a JOIN routes r ON a.airline_id = r.airline_id WHERE a.active = 'Y' AND a.country = 'India' GROUP BY a.name ORDER BY route_count DESC, airline_name"}], 'ground_truth': [{'airline_name': 'Alliance Air', 'route_count': 50}, {'airline_name': 'IndiGo Airlines', 'route_count': 50}, {'airline_name': 'Air India', 'route_count': 29}, {'airline_name': 'Crimson Air', 'route_count': 1}, {'airline_name': 'SkyLark Airways', 'route_count': 1}]}
    
    ====================
    LLM QUERY GENERATION
    ====================
    User prompt: Which active airlines in India have the most routes, and how many routes does each operate?
    Ground truth: [{'airline_name': 'Alliance Air', 'route_count': 50}, {'airline_name': 'IndiGo Airlines', 'route_count': 50}, {'airline_name': 'Air India', 'route_count': 29}, {'airline_name': 'Crimson Air', 'route_count': 1}, {'airline_name': 'SkyLark Airways', 'route_count': 1}]
    Calling model 'accounts/fireworks/models/llama-v3p1-8b-instruct' to generate SQL query...
    
    Model Generated SQL Query:
    SELECT T1.name, COUNT(T2.airline_id) FROM airlines AS T1 INNER JOIN routes AS T2 ON T1.airline_id = T2.airline_id WHERE T1.country = 'India' AND T1.active = 1 GROUP BY T1.name ORDER BY COUNT(T2.airline_id) DESC LIMIT 1
    
    ====================
    MCP SERVER EXECUTION
    ====================
    Sending query to MCP server...
    
    Parsed Result from Server:
    [
      {}
    ]
    
    ====================
    COMPARISON
    ====================
    
    ❌ BAD RESULT: The base model's SQL produced different data than expected.
    
    This is often the intended outcome when testing a base model, as it highlights what fine-tuning needs to correct.
```

### 14. 🚀 Launch the Fine-Tuning Job & Deploy via the UI

Now we'll use the Fireworks AI web interface to take our prepared dataset and fine-tune a model. This process uses your custom `evaluate` function to teach a base model how to generate SQL correctly.

#### RFT vs Traditional Fine-Tuning:

Traditional supervised fine-tuning (SFT) would:

* Require thousands of examples
* Teach the model to mimic exact SQL syntax
* Often overfit to specific query patterns

Reinforcement fine-tuning (RFT) instead:

* Works with just hundreds of examples
* Rewards correct results regardless of SQL syntax
* Discovers novel solutions through exploration
* Generalizes better to unseen queries

> **Real World 🌍**\
> This is the core of the RFT process. You're teaching a general-purpose model a very specific and valuable new skill using a powerful, UI-driven workflow. You may follow along as described below

As described in the [Fireworks RFT documentation](https://fireworks.ai/docs/fine-tuning/reinforcement-fine-tuning-models), the process involves uploading your data, creating an evaluator, running the job, and deploying.

**14. a) Upload Your Dataset**

1. Navigate to the **Datasets** tab in your [https://app.fireworks.ai](https://app.fireworks.ai) dashboard.
2. Click **"Create Dataset"**.
3. Upload your training file: `data/final_rft_sql_train_data.jsonl`.
4. Give it a memorable name, like `rft-sql-train-data-v1`, and save it.

**14. b) Create the Evaluator**

1. Navigate to the **Evaluations** tab in the dashboard.
2. Click **"Create Evaluator"**. This will open the web IDE.
3. In the editor on the left, replace the template code with your full `evaluate` function from step 12 above. This function already contains the logic to connect to your MCP server and compare the results. You just need to add your MCP server URL to the MCP\_SERVER\_URL line.
4. Save the evaluator with a name like `rft-sql-mcp-evaluator-v1`.

**14. c) Launch the Fine-Tuning Job**

1. Navigate to the **Fine-Tuning** tab.
2. Click **"Fine-Tune a Model"** and select **Reinforcement**.
3. Configure the job:
   * **Model Selection:** Select a model, for example `qwen2p5-7b` (may appear as `Qwen2.5 7B`).
   * **Dataset:** Select the `rft-sql-train-data-v1` you uploaded.
   * **Evaluator:** Select the `rft-sql-mcp-evaluator-v1` you just created.
   * **Rollout:** You can leave these as the default values.
   * **Optional Settings:** You can leave the Model Output Name blank and get the default name, or enter a name of your choosing.
4. You can leave most other hyperparameters as their defaults, though fine-tuning for 32 epochs (i.e., setting `Epochs` to `32`) is recommended due to the complexity of the task.
5. Click **"Create Job"**.

**14. d) Monitor and Deploy**

1. You can monitor the progress of your job in the **Fine-Tuning** tab. In this example, we trained for 32 epochs and got the following plot:
   <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a407b8e0dc88181a2678bdf61e9f2444" alt="RFT Training Progress" data-og-width="1648" width="1648" data-og-height="914" height="914" data-path="examples/assets/rft-sql-training.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a0af5936493d30c7473f711e1a59bbf3 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=c90f2795e9228b5cd26c1cab1eb7ed5f 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=09bdbb68073d786de76a20b9fec7cd81 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=3142e20c4ed6d362cc29965d5942ef91 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=87e9ee35eb86cc472c353d5955fec1b8 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/examples/assets/rft-sql-training.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=af04ad9f047bf0e100ab8aaafaddd72f 2500w" />
2. Once the job status is `Completed`, you can deploy your model. To deploy, click "Deploy" on the top right of your fine-tuning job's page and then "Deploy LoRA Model". Please note:
   * The Model under "Select base model\*" should be the one from your Reinforcement Fine-Tuning job (this should be populated automatically)
   * Speculative decoding is an advanced technique that can improve latency, but is not needed for this use-case
   * Feel free to make the other selections (Performance, Scaling, and Metadata) as needed; enabling autoscaling is recommended to reduce costs
3. Find this new model and click the **Deploy** button to create an API endpoint.

**14. e) Test Your New Model!**
Once deployed, copy your new model's ID and paste it into the `LLM_MODEL` variable in the testing cell (step #13) to make sure it works as expected, along with your MCP server URL (i.e., `LLM_MODEL = "accounts/<your-account-id>/models/<your-model-id>"` and `MCP_SERVER_URL = "<your-mcp-server-url>"`).

### 15. ⚖️ Evaluate Model Performance

Now for the moment of truth. We will systematically compare the performance of the original base model against our newly fine-tuned model, as well as a much larger base model, to quantify the improvement and general accuracy.

We'll run both models against every entry in our test dataset (final\_rft\_sql\_test\_data.jsonl). For each entry, we will:

1. Provide the same system and user prompt to both the base model and the fine-tuned model.
2. Capture the SQL query generated by each.
3. Execute each query against our live MCP server.
4. Compare the query result to the ground\_truth from our dataset.
5. Keep a running score for each model.

This process will give us a clear, data-driven view of how much more accurate our model became after reinforcement fine-tuning.

> **Real World 🌍**
> This is a critical step in any MLOps loop. Evaluating a model on a consistent test set is the only way to prove that your efforts have resulted in a tangible improvement. In production, you'd also want to:
>
> * Track latency and cost metrics
> * Monitor for drift over time
> * A/B test against your current solution
> * Collect user feedback on query quality

```python  theme={null}
import requests
import json
import os
import time
from fireworks import LLM
from tqdm.auto import tqdm
from dotenv import load_dotenv

load_dotenv()

# --- 1. SETUP: Define the models to compare, server URL, and dataset path ---

# IMPORTANT: Make sure your FIREWORKS_API_KEY is set as an environment variable.
if "FIREWORKS_API_KEY" not in os.environ:
    print("FATAL: FIREWORKS_API_KEY environment variable not set.")

# The base model you used for the fine-tuning job.
BASE_MODEL_ID = "accounts/fireworks/models/qwen2p5-7b"  # <--- Replace if you used a different base model
LARGE_BASE_MODEL_ID = "accounts/fireworks/models/qwen3-coder-480b-a35b-instruct"

# IMPORTANT: Replace this with the model ID of your new fine-tuned model.
#FINE_TUNED_MODEL_ID = "accounts/<your-account-id>/models/<your-base-model-id>"  # <--- Replace with your fine-tuned model ID
FINE_TUNED_MODEL_ID = "accounts/<your-account-id>/models/<your-base-model-id>"

MCP_SERVER_URL = None  # <--- PUT MCP SERVER URL HERE without the /mcp/ suffix at the end
DATASET_FILE_PATH = "data/final_rft_sql_test_data.jsonl"

# --- 2. Create LLM Objects ---
base_model_llm = None
large_base_model_llm = None
fine_tuned_model_llm = None
try:
    base_model_llm = LLM(model=BASE_MODEL_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    large_base_model_llm = LLM(model=LARGE_BASE_MODEL_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    fine_tuned_model_llm = LLM(model=FINE_TUNED_MODEL_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    print("LLM objects for all three models created successfully.")
except Exception as e:
    print(f"FATAL: Could not create LLM objects. Error: {e}")

# --- 3. Load Dataset ---
dataset = []
if all([base_model_llm, large_base_model_llm, fine_tuned_model_llm]):
    try:
        with open(DATASET_FILE_PATH, 'r') as f:
            dataset = [json.loads(line) for line in f]
        print(f"Loaded {len(dataset)} evaluation examples from '{DATASET_FILE_PATH}'.")
    except Exception as e:
        print(f"FATAL: Could not load dataset. Error: {e}")
        dataset = []

# --- 4. HELPER AND EVALUATION FUNCTIONS ---

def parse_duckdb_ascii_table(table_string: str) -> list[dict]:
    """
    Parses a DuckDB-style ASCII table string into a list of dictionaries.
    This version robustly handles 'NULL' values and empty strings.
    """
    lines = table_string.strip().split('\n')
    content_lines = [line for line in lines if line.strip() and not line.startswith('+')]
    if len(content_lines) < 2:
        return []
    
    header_raw = [h.strip() for h in content_lines[0].split('|')[1:-1]]
    data_lines = content_lines[1:]
    
    if len(data_lines) > 0:
        try:
            first_data_values = [v.strip() for v in data_lines[0].split('|')[1:-1]]
            if len(first_data_values) == len(header_raw) and all(v.isupper() for v in first_data_values):
                data_lines = data_lines[1:]
        except IndexError:
            pass

    rows = []
    for line in data_lines:
        try:
            values_raw = [v.strip() for v in line.split('|')[1:-1]]
            if len(values_raw) == len(header_raw):
                row_dict = {}
                for i, header in enumerate(header_raw):
                    value_str = values_raw[i]
                    if value_str.upper() == 'NULL' or value_str == '':
                        row_dict[header] = None
                        continue
                    
                    try:
                        if '.' in value_str:
                            row_dict[header] = float(value_str)
                        else:
                            row_dict[header] = int(value_str)
                    except (ValueError, TypeError):
                        row_dict[header] = value_str
                rows.append(row_dict)
        except IndexError:
            continue
    return rows

def are_results_equal(predicted_rows: list[dict], ground_truth_rows: list[dict]) -> bool:
    """
    Compares datasets by converting all values to strings and sorting them,
    which ignores row order, column order, and data types (e.g., int vs float).
    """
    try:
        gt_values = sorted([sorted(map(str, row.values())) for row in ground_truth_rows])
        predicted_values = sorted([sorted(map(str, row.values())) for row in predicted_rows])
        return gt_values == predicted_values
    except Exception:
        return False

def get_sql_and_evaluate(llm_obj, system_prompt: str, user_prompt: str, ground_truth: list[dict]) -> int:
    """
    Calls a pre-configured LLM object to get a SQL query, executes it, and compares to ground truth.
    Returns 1 for a correct result, 0 for an incorrect one.
    """
    try:
        # Step 1: Get SQL from the model
        messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
        response = llm_obj.chat.completions.create(messages=messages, temperature=0.0)
        sql_query = response.choices[0].message.content.strip()

        # Step 2: Execute SQL on MCP server
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        payload = {"id": "eval-query-1", "jsonrpc": "2.0", "method": "tools/call", "params": {"session": {"id": "full-eval-session"}, "name": "query", "arguments": {"query": sql_query}}}

        response_data = None
        with requests.post(f"{MCP_SERVER_URL}/mcp/", headers=headers, json=payload, timeout=30, stream=True) as mcp_response:
            mcp_response.raise_for_status()
            for line in mcp_response.iter_lines():
                if line and line.decode('utf-8').startswith('data:'):
                    json_part = line.decode('utf-8')[len('data:'):].strip()
                    if json_part:
                        response_data = json.loads(json_part)
                        break

        if response_data is None or "error" in response_data:
            return 0

        # Step 3: Parse and compare results
        ascii_table = response_data['result']['content'][0]['text']
        predicted_rows = parse_duckdb_ascii_table(ascii_table)

        return 1 if are_results_equal(predicted_rows, ground_truth) else 0
    except Exception as e:
        print(f"--> Error during evaluation for model {llm_obj.model}: {e}")
        return 0

# --- 5. RUN THE FULL EVALUATION ---

base_model_score = 0
large_base_model_score = 0
fine_tuned_model_score = 0

if dataset:
    print("\nStarting evaluation...")
    for item in tqdm(dataset, desc="Evaluating models"):
        system_prompt = item["messages"][0]["content"]
        user_prompt = item["messages"][1]["content"]
        ground_truth = item["ground_truth"]

        # Evaluate base model
        base_model_score += get_sql_and_evaluate(base_model_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)  # Be nice to the API

        # Evaluate large base model
        large_base_model_score += get_sql_and_evaluate(large_base_model_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)

        # Evaluate fine-tuned model
        fine_tuned_model_score += get_sql_and_evaluate(fine_tuned_model_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)

# --- 6. REPORT RESULTS ---

if dataset:
    total = len(dataset)
    base_accuracy = (base_model_score / total) * 100
    large_base_accuracy = (large_base_model_score / total) * 100
    tuned_accuracy = (fine_tuned_model_score / total) * 100

    print("\n" + "="*25)
    print("  EVALUATION COMPLETE")
    print("="*25)
    print(f"Total Examples: {total}\n")
    print("--- BASE MODEL ---")
    print(f"Model ID: {BASE_MODEL_ID}")
    print(f"Correct: {base_model_score}/{total}")
    print(f"Accuracy: {base_accuracy:.2f}%\n")

    print("--- LARGE BASE MODEL ---")
    print(f"Model ID: {LARGE_BASE_MODEL_ID}")
    print(f"Correct: {large_base_model_score}/{total}")
    print(f"Accuracy: {large_base_accuracy:.2f}%\n")

    print("--- FINE-TUNED MODEL ---")
    print(f"Model ID: {FINE_TUNED_MODEL_ID}")
    print(f"Correct: {fine_tuned_model_score}/{total}")
    print(f"Accuracy: {tuned_accuracy:.2f}%\n")
    
    print("="*25)
    print("  PERFORMANCE LIFT")
    print("="*25)
    print(f"Fine-Tuned vs. Base: {tuned_accuracy - base_accuracy:+.2f}%")
    print(f"Fine-Tuned vs. Large Base: {tuned_accuracy - large_base_accuracy:+.2f}%")

else:
    print("Evaluation skipped because the dataset or LLM objects could not be loaded.")
```

```text  theme={null}
    LLM objects for all three models created successfully.
    Loaded 92 evaluation examples from 'data/final_rft_sql_test_data.jsonl'.
    
    Starting evaluation...


    Evaluating models:   0%|          | 0/92 [00:00<?, ?it/s]
      result = func(*args, **kwargs)
    Evaluating models: 100%|██████████| 92/92 [14:41<00:00,  9.59s/it]  

    
    =========================
      EVALUATION COMPLETE
    =========================
    Total Examples: 92
    
    --- BASE MODEL ---
    Model ID: accounts/fireworks/models/qwen2p5-7b
    Correct: 22/92
    Accuracy: 23.91%
    
    --- LARGE BASE MODEL ---
    Model ID: accounts/fireworks/models/qwen3-coder-480b-a35b-instruct
    Correct: 32/92
    Accuracy: 34.78%
    
    --- FINE-TUNED MODEL ---
    Model ID: accounts/<account-id>/models/<base-model-id>
    Correct: 52/92
    Accuracy: 56.52%
    
    =========================
      PERFORMANCE LIFT
    =========================
    Fine-Tuned vs. Base: +32.61%
    Fine-Tuned vs. Large Base: +21.74%
```

### 16. ✨ Cleanup & Conclusion

Congratulations! You've successfully completed the entire Reinforcement Fine-Tuning loop. You started with just a database schema and ended with a highly specialized, performant, and data-aware AI model.

#### Cleanup

Cloud resources and model deployments can incur costs, so it's good practice to clean up any resources you no longer need.

* **Check your Deployments:** Navigate to the [Deployments tab](https://app.fireworks.ai/dashboard/deployments) in your Fireworks AI dashboard. Here you can monitor and manage all your deployed models.
* **Delete Unneeded Models:** Feel free to delete any deployments you no longer need. For example, you might have deployed the base or large-base models during the evaluation step to compare against your fine-tuned model. These can now be safely removed to save costs.
* **Delete Cloud Run service and container image:** Feel free to delete your MCP server Cloud Run service and container image to avoid stray storage costs.

You can, of course, continue using your new fine-tuned SQL generation model for any application you see fit!

#### Conclusions

The evaluation results from the previous step highlight the power of this approach.

* **Performance on par with massive models:** Our fine-tuned 7B parameter model performs better than a much larger model like `qwen3-coder-480b-a35b-instruct` on this specific dataset. This is because it has been fine-tuned to understand the data schema via real query generation and execution.
* **Efficiency Gains:** A 7B model is significantly faster and cheaper to run than a 480B one, offering production-grade performance at a fraction of the cost and latency.
* **High-Level Capability on Complex Tasks:** The queries in this dataset are relatively complex, which is reflected in the final accuracy score of around 57%. This is a strong result, demonstrating that for a specialized domain, a smaller model can be tuned to achieve a level of performance that exceeds larger models like `qwen3-coder-480b-a35b-instruct`. Specifically, the final accuracy scores we measured for this dataset were:
  * Qwen2.5 7B (base): **23.91%** accuracy (**22/92** correct on the held-out test set)
  * Qwen3 Coder 480B A35B Instruct (base): **34.78%** accuracy (**32/92** correct on the held-out test set)
  * Qwen2.5 7B (RFT tuned): **56.52%** accuracy (**52/92** correct on the held-out test set)

***

Throughout this tutorial, we demonstrated a complete, end-to-end workflow for creating a fine-tuned text-to-SQL model. We began with the absolute minimum requirement, a database schema, and used a series of LLM-driven steps to generate a safe, synthetic data sandbox. From there, we generated a rich dataset of queries and answers, which we used to fine-tune a model using the Fireworks RFT platform. The final result is a small, efficient model that can accurately query data it has never seen, a task that was previously only possible with vastly larger and more expensive models.

This pattern of **schema → synthetic data → RFT** is a secure, effective, and repeatable methodology for teaching language models to become expert users of your private data and custom APIs, without ever exposing the underlying sensitive information.

### Appendix

#### Testing more open models on Fireworks

```python  theme={null}
import requests
import json
import os
import time
import datetime
from fireworks import LLM
from tqdm.auto import tqdm
from dotenv import load_dotenv

load_dotenv()

# --- 1. SETUP: Define the models to compare, server URL, and dataset path ---

# IMPORTANT: Make sure your FIREWORKS_API_KEY is set as an environment variable.
if "FIREWORKS_API_KEY" not in os.environ:
    print("FATAL: FIREWORKS_API_KEY environment variable not set.")

# IMPORTANT: Replace these with the model IDs of the models you want to evaluate.
MODEL_1_ID = "accounts/fireworks/models/qwen3-coder-480b-a35b-instruct"  # <--- Replace with your model ID
MODEL_2_ID = "accounts/fireworks/models/kimi-k2-instruct" # <--- Replace with your model ID
MODEL_3_ID = "accounts/fireworks/models/deepseek-v3" # <--- Replace with your model ID

MCP_SERVER_URL = None  # <--- PUT MCP SERVER URL HERE without the /mcp/ suffix at the end
DATASET_FILE_PATH = "data/final_rft_sql_test_data.jsonl"

# --- 2. Create LLM Objects ---
model_1_llm = None
model_2_llm = None
model_3_llm = None
try:
    model_1_llm = LLM(model=MODEL_1_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    model_2_llm = LLM(model=MODEL_2_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    model_3_llm = LLM(model=MODEL_3_ID, deployment_type="auto", api_key=os.getenv("FIREWORKS_API_KEY"))
    print("LLM objects for all three models created successfully.")
except Exception as e:
    print(f"FATAL: Could not create LLM objects. Error: {e}")

# --- 3. Load Dataset ---
dataset = []
if all([model_1_llm, model_2_llm, model_3_llm]):
    try:
        with open(DATASET_FILE_PATH, 'r') as f:
            dataset = [json.loads(line) for line in f]
        print(f"Loaded {len(dataset)} evaluation examples from '{DATASET_FILE_PATH}'.")
    except Exception as e:
        print(f"FATAL: Could not load dataset. Error: {e}")
        dataset = []

# --- 4. SETUP for Manual Logging ---
MANUAL_LOG_FILE = "evaluation_manual_open.log"

# Initialize the log file by clearing it and writing a header
with open(MANUAL_LOG_FILE, 'w', encoding='utf-8') as f:
    f.write(f"--- Evaluation Log ---\n")
    f.write(f"Log started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

def write_to_log(message: str):
    """Appends a timestamped message to the manual log file."""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
    try:
        with open(MANUAL_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} - {message}\n")
    except Exception as e:
        # If logging fails, print an error to the console
        print(f"CRITICAL: Failed to write to log file '{MANUAL_LOG_FILE}'. Error: {e}")

print(f"Manual logging configured. Log file is '{MANUAL_LOG_FILE}'.")


# --- 5. HELPER AND EVALUATION FUNCTIONS ---

def parse_duckdb_ascii_table(table_string: str) -> list[dict]:
    """
    Parses a DuckDB-style ASCII table string into a list of dictionaries.
    This version robustly handles 'NULL' values and empty strings.
    """
    lines = table_string.strip().split('\n')
    content_lines = [line for line in lines if line.strip() and not line.startswith('+')]
    if len(content_lines) < 2:
        return []
    
    header_raw = [h.strip() for h in content_lines[0].split('|')[1:-1]]
    data_lines = content_lines[1:]
    
    if len(data_lines) > 0:
        try:
            first_data_values = [v.strip() for v in data_lines[0].split('|')[1:-1]]
            if len(first_data_values) == len(header_raw) and all(v.isupper() for v in first_data_values):
                data_lines = data_lines[1:]
        except IndexError:
            pass

    rows = []
    for line in data_lines:
        try:
            values_raw = [v.strip() for v in line.split('|')[1:-1]]
            if len(values_raw) == len(header_raw):
                row_dict = {}
                for i, header in enumerate(header_raw):
                    value_str = values_raw[i]
                    if value_str.upper() == 'NULL' or value_str == '':
                        row_dict[header] = None
                        continue
                    
                    try:
                        if '.' in value_str:
                            row_dict[header] = float(value_str)
                        else:
                            row_dict[header] = int(value_str)
                    except (ValueError, TypeError):
                        row_dict[header] = value_str
                rows.append(row_dict)
        except IndexError:
            continue
    return rows

def are_results_equal(predicted_rows: list[dict], ground_truth_rows: list[dict]) -> bool:
    """
    Compares datasets by converting all values to strings and sorting them,
    which ignores row order, column order, and data types (e.g., int vs float).
    """
    try:
        gt_values = sorted([sorted(map(str, row.values())) for row in ground_truth_rows])
        predicted_values = sorted([sorted(map(str, row.values())) for row in predicted_rows])
        return gt_values == predicted_values
    except Exception:
        return False


def get_sql_and_evaluate(llm_obj, system_prompt: str, user_prompt: str, ground_truth: list[dict]) -> int:
    """
    Calls a pre-configured LLM object to get a SQL query, executes it, logs the process,
    and compares to ground truth. Returns 1 for a correct result, 0 for an incorrect one.
    """
    model_id = llm_obj.model
    write_to_log(f"--- Fireworks Evaluation Start: Model {model_id} ---")
    write_to_log(f"System Prompt: {system_prompt}")
    write_to_log(f"User Prompt: {user_prompt}")
    try:
        # Step 1: Get SQL from the model
        messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
        response = llm_obj.chat.completions.create(messages=messages, temperature=0.0)
        raw_output = response.choices[0].message.content.strip()
        sql_query = raw_output
        write_to_log(f"Raw LLM Output: {raw_output}")
        write_to_log(f"Extracted SQL: {sql_query}")

        # Step 2: Execute SQL on MCP server
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        payload = {"id": "eval-query-1", "jsonrpc": "2.0", "method": "tools/call", "params": {"session": {"id": "full-eval-session"}, "name": "query", "arguments": {"query": sql_query}}}

        response_data = None
        with requests.post(f"{MCP_SERVER_URL}/mcp/", headers=headers, json=payload, timeout=30, stream=True) as mcp_response:
            mcp_response.raise_for_status()
            for line in mcp_response.iter_lines():
                if line and line.decode('utf-8').startswith('data:'):
                    json_part = line.decode('utf-8')[len('data:'):].strip()
                    if json_part:
                        response_data = json.loads(json_part)
                        break

        if response_data is None or "error" in response_data:
            error_message = response_data.get('error', 'No response data') if response_data else 'No response data'
            write_to_log(f"ERROR: Failed to execute query. Response: {error_message}")
            write_to_log("Result: Incorrect (Query Execution Failed)")
            write_to_log(f"--- Fireworks Evaluation End: Model {model_id} ---\n")
            return 0

        # Step 3: Parse and compare results
        ascii_table = response_data['result']['content'][0]['text']
        predicted_rows = parse_duckdb_ascii_table(ascii_table)
        write_to_log(f"Execution Result (predicted): {predicted_rows}")
        write_to_log(f"Ground Truth: {ground_truth}")

        is_correct = are_results_equal(predicted_rows, ground_truth)
        write_to_log(f"Result: {'Correct' if is_correct else 'Incorrect'}")
        write_to_log(f"--- Fireworks Evaluation End: Model {model_id} ---\n")
        return 1 if is_correct else 0
    except Exception as e:
        error_msg = f"ERROR: Exception during evaluation for model {model_id}: {e}"
        print(f"--> {error_msg}")
        write_to_log(error_msg)
        write_to_log(f"--- Fireworks Evaluation End: Model {model_id} ---\n")
        return 0

# --- 6. RUN THE FULL EVALUATION ---

model_1_score = 0
model_2_score = 0
model_3_score = 0

if dataset:
    msg = "\nStarting evaluation..."
    print(msg)
    write_to_log(msg.strip())
    for item in tqdm(dataset, desc="Evaluating models"):
        system_prompt = item["messages"][0]["content"]
        user_prompt = item["messages"][1]["content"]
        ground_truth = item["ground_truth"]

        # Evaluate model 1
        model_1_score += get_sql_and_evaluate(model_1_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)  # Be nice to the API

        # Evaluate model 2
        model_2_score += get_sql_and_evaluate(model_2_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)

        # Evaluate model 3
        model_3_score += get_sql_and_evaluate(model_3_llm, system_prompt, user_prompt, ground_truth)
        time.sleep(1)


---

**Navigation:** [← Previous](./02-with-display-name-and-description.md) | [Index](./index.md) | [Next →](./04-7-report-results.md)
