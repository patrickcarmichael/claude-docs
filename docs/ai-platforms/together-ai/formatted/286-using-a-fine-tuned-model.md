---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using a Fine-tuned Model

Once your fine-tuning job completes, your model will be available for use:

**Option 1: Serverless LoRA Inference**

If you used LoRA fine-tuning and the model supports serverless LoRA inference, you can immediately use your model without deployment. We can call it just like any other model on the Together AI platform, by providing the unique fine-tuned model `output_name` from our fine-tuning job.

<Icon icon="link" iconType="solid" /> See the list of all models that support [LoRA
Inference](/docs/lora-inference).
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
