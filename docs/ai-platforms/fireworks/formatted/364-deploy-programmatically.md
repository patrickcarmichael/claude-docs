---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy programmatically

evaluator_id = word_count_reward.deploy(
    name="word-count-evaluator",
    description="Evaluates responses based on word count"
)
print(f"Deployed with ID: {evaluator_id}")
```
Or using the CLI:
```bash
reward-kit deploy --id word-count-evaluator --metrics-folders "word_count=./path/to/metric" --force
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
