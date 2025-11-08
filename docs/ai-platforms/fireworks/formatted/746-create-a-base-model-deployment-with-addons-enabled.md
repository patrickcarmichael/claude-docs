---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a base model deployment with addons enabled

base_model = LLM(
    model="accounts/fireworks/models/base-model-id",
    deployment_type="on-demand",
    id="shared-base-deployment",  # Simple string identifier

    enable_addons=True
)
base_model.apply()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
