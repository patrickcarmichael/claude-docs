---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Anatomy of an evaluator

Every evaluator has three core components:

### 1. Input data

The prompt and any ground truth data needed for evaluation:
```python
{
  "messages": [
    {"role": "system", "content": "You are a math tutor."},
    {"role": "user", "content": "What is 15 * 23?"}
  ],
  "ground_truth": "345"  # Optional additional data

}
```

### 2. Model output

The assistant's response to evaluate:
```python
{
  "role": "assistant",
  "content": "Let me calculate that step by step:\n15 * 23 = 345"
}
```

### 3. Scoring logic

Code that compares the output to your criteria:
```python
def evaluate(model_output: str, ground_truth: str) -> float:
    # Extract answer from model's response

    predicted = extract_number(model_output)
    
    # Score it

    if predicted == int(ground_truth):
        return 1.0  # Perfect

    else:
        return 0.0  # Wrong

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
