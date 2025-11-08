---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Serverless deployment

For quick experimentation and prototyping, you can deploy your fine-tuned model to shared serverless infrastructure without managing GPUs.

>   **📝 Note**
>
> Not all base models support serverless addons. Check the [list of models that support serverless with LoRA](https://app.fireworks.ai/models?filter=LLM\&serverlessWithLoRA=true) to confirm your base model is supported.

### Deploy to serverless

Load your fine-tuned model into a serverless deployment:
```bash
firectl load-lora <FINE_TUNED_MODEL_ID>
```typescript

### Key considerations

* **No hosting costs**: Deploying to serverless is free—you only pay per-token usage costs
* **Rate limits**: Same rate limits apply as serverless base models
* **Performance**: Lower performance than on-demand deployments and the base model
* **Automatic unloading**: Unused addons may be automatically unloaded after a week
* **Limit**: Deploy up to 100 fine-tuned models to serverless

<Tip>
  For production workloads requiring consistent performance, use [on-demand deployments](#single-lora-deployment) instead.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
