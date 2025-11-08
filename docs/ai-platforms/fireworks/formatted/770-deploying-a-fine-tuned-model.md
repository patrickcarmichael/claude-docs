---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploying a fine-tuned model

After fine-tuning completes, deploy your model to make it available for inference:
```bash
firectl create deployment <FINE_TUNED_MODEL_ID>
```
This creates a dedicated deployment with performance matching the base model.

<Tip>
  For more details on deploying fine-tuned models, including multi-LoRA and serverless deployments, see the [Deploying LoRAs guide](/fine-tuning/deploying-loras).
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
