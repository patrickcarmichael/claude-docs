---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-LoRA deployment

If you have multiple fine-tuned versions of the same base model (e.g., you've fine-tuned the same model for different use cases, applications, or prototyping), you can share a single base model deployment across these LoRA models to achieve higher utilization.

>   **⚠️ Warning**
>
> Multi-LoRA deployment comes with performance tradeoffs. We recommend using it only if you need to serve multiple fine-tunes of the same base model and are willing to trade performance for higher deployment utilization.

### Deploy with CLI

<Steps>
  <Step title="Create base model deployment">
    Deploy the base model with addons enabled:
```bash
    firectl create deployment "accounts/fireworks/models/<MODEL_ID of base model>" --enable-addons
```
  </Step>

  <Step title="Load LoRA addons">
    Once the deployment is ready, load your LoRA models onto the deployment:
```bash
    firectl load-lora <FINE_TUNED_MODEL_ID> --deployment <DEPLOYMENT_ID>
```
    You can load multiple LoRA models onto the same deployment by repeating this command with different model IDs.
  </Step>
</Steps>

### Deploy with the Build SDK

You can also use multi-LoRA deployment with the Build SDK:
```python
from fireworks import LLM

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
