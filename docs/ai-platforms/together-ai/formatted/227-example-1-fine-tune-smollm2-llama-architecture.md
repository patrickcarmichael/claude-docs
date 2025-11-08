---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 1: Fine-tune SmolLM2 (Llama architecture)

client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model template

    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Custom model

    training_file="file-id",
    n_epochs=3,
    learning_rate=1e-5,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
