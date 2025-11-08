---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 1: Fine-tune Qwen2.5 model

client.fine_tuning.create(
    model="Qwen/Qwen3-4B",  # Base template

    from_hf_model="Qwen/Qwen2.5-7B-Instruct",  # Custom Qwen model

    training_file="file-id",
    learning_rate=5e-6,  # Lower LR for larger models

    n_epochs=3,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
