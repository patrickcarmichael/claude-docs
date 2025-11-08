---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Perform a reinforcement learning step

job = llm.reinforcement_step(
    dataset=dataset,
    output_model="my-improved-model-v1",
    epochs=1,
    learning_rate=1e-5,
    accelerator_count=2,
    accelerator_type="NVIDIA_H100_80GB"
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
