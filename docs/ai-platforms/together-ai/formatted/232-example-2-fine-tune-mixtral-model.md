---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 2: Fine-tune Mixtral model

client.fine_tuning.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    from_hf_model="mistralai/Mixtral-8x22B-Instruct-v0.1",  # Larger variant

    training_file="large-dataset-id",
    batch_size=1,  # Very large model, small batch

    learning_rate=1e-6,
)
```

**Gemma Family Models**
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
