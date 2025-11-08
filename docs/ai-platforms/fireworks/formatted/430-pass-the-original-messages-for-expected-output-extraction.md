---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pass the original messages for expected output extraction

result = e2b_code_execution_reward(
    messages=messages,
    original_messages=messages,
    language="python",
    api_key="your_e2b_api_key"
)
````

### Fallback to Local Execution

You can gracefully fall back to local execution when an E2B API key is not available:
```python
from reward_kit.rewards.code_execution import (
    e2b_code_execution_reward,
    local_code_execution_reward
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
