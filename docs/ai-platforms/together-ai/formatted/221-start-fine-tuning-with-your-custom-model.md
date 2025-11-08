---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Start fine-tuning with your custom model

job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",  # Base model family for configuration

    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # Your custom model from HF

    training_file="file-id-from-upload",
    # Optional: for private repositories

    hf_api_token="hf_xxxxxxxxxxxx",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
