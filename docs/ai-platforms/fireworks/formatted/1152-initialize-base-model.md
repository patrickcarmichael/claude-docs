---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Initialize base model

base_model = LLM(
    model="qwen2p5-7b-instruct",
    deployment_type="on-demand",
    id="my-base-deployment",
    enable_addons=True  # Enable LoRA addons to only use one deployment for all steps

)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
