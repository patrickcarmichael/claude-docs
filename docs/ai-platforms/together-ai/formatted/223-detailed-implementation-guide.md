---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Detailed Implementation Guide

**Step 1: Prepare Your Training Data**

Ensure your training data is formatted correctly and uploaded to the Together platform. Refer to [our data preparation guide](./fine-tuning-data-preparation.mdx) for detailed instructions on supported formats.

**Step 2: Start Fine-Tuning**

Launch your fine-tuning job with your custom model:
```python
job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    training_file="your-file-id",
    # Recommended training parameters

    n_epochs=3,
    learning_rate=1e-5,
    batch_size=4,
    # Optional parameters

    suffix="custom-v1",  # Helps track different versions

    wandb_api_key="...",  # For training metrics monitoring

    # Add other training parameters for your training

)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
