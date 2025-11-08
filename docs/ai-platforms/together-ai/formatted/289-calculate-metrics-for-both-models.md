---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Calculate metrics for both models

em_base, f1_base = get_metrics(base_answers)
em_ft, f1_ft = get_metrics(finetuned_answers)

print(f"Base Model - EM: {em_base:.2f}, F1: {f1_base:.2f}")
print(f"Fine-tuned Model - EM: {em_ft:.2f}, F1: {f1_ft:.2f}")
```

You should get figures similar to the table below:

| Llama 3.1 8B | EM   | F1   |
| ------------ | ---- | ---- |
| Original     | 0.01 | 0.18 |
| Fine-tuned   | 0.32 | 0.41 |

We can see that the fine-tuned model performs significantly better on the test set, with a large improvement in both Exact Match and F1 scores.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
