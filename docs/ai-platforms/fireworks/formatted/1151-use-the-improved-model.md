---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use the improved model

improved_llm = LLM(
    model=job.output_model,
    deployment_type="on-demand-lora",
    base_id=llm.deployment_id
)
improved_llm.apply()
```

### Iterative Reinforcement Learning Workflow

The `reinforcement_step` method is designed to support iterative reinforcement learning workflows. Here's a complete example showing how to perform multiple reinforcement learning steps:
```python
import asyncio
import time
import random
from fireworks import LLM, Dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
