---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 2: Fine-tune specialized Qwen model

client.fine_tuning.create(
    model="Qwen/Qwen3-7B",
    from_hf_model="Qwen/Qwen2.5-Math-7B-Instruct",  # Math-specialized

    training_file="math-problems-dataset",
    suffix="math-tuned-v1",
)
```

**Mistral Family Models**
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
