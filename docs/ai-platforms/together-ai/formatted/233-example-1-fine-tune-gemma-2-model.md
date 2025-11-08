---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 1: Fine-tune Gemma 2 model

client.fine_tuning.create(
    model="google/gemma-2-9b-it",  # Base template

    from_hf_model="google/gemma-2-2b-it",  # Smaller Gemma variant

    training_file="file-id",
    n_epochs=4,
    learning_rate=2e-5,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
