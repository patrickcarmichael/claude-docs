---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Single-LoRA deployment

Deploy your LoRA fine-tuned model with a single command that delivers performance matching the base model. This streamlined approach, called live merge, eliminates the previous two-step process and provides better performance compared to multi-LoRA deployments.

### Quick deployment

Deploy your LoRA fine-tuned model with one simple command:
```bash
firectl create deployment "accounts/fireworks/models/<MODEL_ID of lora model>"
```
<Check>
  Your deployment will be ready to use once it completes, with performance that matches the base model.
</Check>

### Deployment with the Build SDK

You can also deploy your LoRA fine-tuned model using the Build SDK:
```python
from fireworks import LLM

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
