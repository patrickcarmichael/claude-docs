---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Structure

Every reward function follows this pattern:
```python
from reward_kit import reward_function

@reward_function
def my_reward(response: str, expected_response: str, **kwargs) -> float:
    # Your evaluation logic here

    return score
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
