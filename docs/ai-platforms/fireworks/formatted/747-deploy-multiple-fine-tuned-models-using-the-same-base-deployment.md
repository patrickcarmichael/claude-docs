---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy multiple fine-tuned models using the same base deployment

fine_tuned_model_1 = LLM(
    model="accounts/your-account/models/fine-tuned-model-1",
    deployment_type="on-demand-lora",
    base_id=base_model.deployment_id
)

fine_tuned_model_2 = LLM(
    model="accounts/your-account/models/fine-tuned-model-2", 
    deployment_type="on-demand-lora",
    base_id=base_model.deployment_id
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
