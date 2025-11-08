---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy the base model for training and inference

base_llm = LLM(
    model="qwen2p5-7b",
    id="kd-base-model",  # Unique identifier

    deployment_type="on-demand",  # Scales automatically

    min_replica_count=0,
    max_replica_count=1
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
