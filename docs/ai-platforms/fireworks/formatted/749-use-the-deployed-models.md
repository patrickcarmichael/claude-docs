---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use the deployed models

response_1 = fine_tuned_model_1.chat.completions.create(
    messages=[{"role": "user", "content": "Hello from model 1!"}]
)

response_2 = fine_tuned_model_2.chat.completions.create(
    messages=[{"role": "user", "content": "Hello from model 2!"}]
)
```
>   **📝 Note**
>
> When using `deployment_type="on-demand-lora"`, you need to provide the `base_id` parameter that references the deployment ID of your base model deployment.

### When to use multi-LoRA deployment

Use multi-LoRA deployment when you:

* Need to serve multiple fine-tuned models based on the same base model
* Want to maximize deployment utilization
* Can accept some performance tradeoff compared to single-LoRA deployment
* Are managing multiple variants or experiments of the same model

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
