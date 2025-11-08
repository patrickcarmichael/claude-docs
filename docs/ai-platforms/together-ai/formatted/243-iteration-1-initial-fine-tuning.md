---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Iteration 1: Initial fine-tuning

initial_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="huggingface/CodeBERTa-small-v1",  # Starting model

    training_file="initial-dataset-id",
    suffix="v1",
    n_epochs=3,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
