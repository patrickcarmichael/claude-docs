---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 4: Start fine-tuning

job = client.fine_tuning.create(
    model="microsoft/phi-3-medium-4k-instruct",  # Base model

    from_hf_model=target_model,  # Your custom model

    training_file=file_upload.id,
    suffix="legal-specialist-v1",
    n_epochs=3,
    learning_rate=1e-5,
    wandb_api_key="your-wandb-key",  # Optional: for monitoring

)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
