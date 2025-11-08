---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Apply base deployment configuration to Fireworks

base_model.apply()

fine_tuned_with_lora = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand-lora",
    base_id=base_model.deployment_id
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
