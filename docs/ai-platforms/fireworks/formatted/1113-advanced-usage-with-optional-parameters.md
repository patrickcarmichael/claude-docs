---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Advanced usage with optional parameters

llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="on-demand",
    id="my-custom-deployment",
    accelerator_type="NVIDIA_H100_80GB",
    min_replica_count=1,
    max_replica_count=3,
    scale_up_window=timedelta(seconds=30),
    scale_down_window=timedelta(minutes=10),
    enable_metrics=True
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
