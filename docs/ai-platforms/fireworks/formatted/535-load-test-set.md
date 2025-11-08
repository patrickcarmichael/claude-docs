---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Load test set

df_test = pd.read_parquet("hf://datasets/openai/gsm8k/" + splits["test"])
```
```
Dataset Statistics:
  • Train size: 7473
  • Test size: 1319
  • Total: 8792
```
**Example GSM8K Problem:**
```
{
    'question': 'Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?',
    'answer': 'Natalia sold 48/2 = <<48/2=24>>24 clips in May.\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.\n#### 72',

}
```
**Why This Format Matters**: The `#### 18` format provides the ground truth answer we need for automated evaluation. We'll extract this pattern to check model correctness.

**Process Dataset for Training and Evaluation**
```python
gsm8k_train_problems = []
for idx, row in df_train.iterrows():
    answer_match = re.search(r'#### (\d+)', row['answer'])

    ground_truth = answer_match.group(1) if answer_match else None

    if ground_truth:
        gsm8k_train_problems.append({
            "question": row['question'],
            "ground_truth": ground_truth,
            "full_solution": row['answer']
        })

gsm8k_test_problems = []
for idx, row in df_test.iterrows():
    answer_match = re.search(r'#### (\d+)', row['answer'])

    ground_truth = answer_match.group(1) if answer_match else None

    if ground_truth:
        gsm8k_test_problems.append({
            "question": row['question'],
            "ground_truth": ground_truth,
            "full_solution": row['answer']
        })
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
