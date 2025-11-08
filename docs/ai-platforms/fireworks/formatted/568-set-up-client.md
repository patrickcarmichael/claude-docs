---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Set Up Client

llm = LLM(
  model="llama-v3p1-8b-instruct",
  id="my-deployment-id",
  deployment_type="on-demand", # Can only fine-tune a dedicated deployment

  precision="FP8",
  accelerator_type="NVIDIA_H100_80GB",
) 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
