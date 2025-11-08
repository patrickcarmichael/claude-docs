---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Evaluate a dataset of coding problems

results = evaluate_dataset(
    reward_function=e2b_code_execution_reward,
    dataset_path="coding_problems.jsonl",
    additional_fields=['test_cases', 'expected_output']
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
