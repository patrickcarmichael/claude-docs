---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 1: Fine-tune Mistral 7B variant

client.fine_tuning.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",  # Base template

    from_hf_model="mistralai/Mistral-7B-Instruct-v0.3",  # Newer version

    training_file="file-id",
    n_epochs=3,
    batch_size=4,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
