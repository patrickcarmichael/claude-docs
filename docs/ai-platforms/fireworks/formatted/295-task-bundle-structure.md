---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Task Bundle Structure

A task bundle is a self-contained directory with all the components needed to evaluate an agent:
```
my_task/
├─ reward.py           # Reward function with @reward_function decorator

├─ tools.py            # Tool registry for this specific task

├─ seed.sql            # Initial DB state (optional)

└─ task.jsonl          # Dataset rows with task specifications

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
