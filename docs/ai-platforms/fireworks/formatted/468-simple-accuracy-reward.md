---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Simple Accuracy Reward

```python
from reward_kit import reward_function

@reward_function
def simple_accuracy(response: str, expected_response: str) -> float:
    """
    A basic accuracy reward that returns 1.0 for exact matches, 0.0 otherwise.
    """
    return 1.0 if response.strip().lower() == expected_response.strip().lower() else 0.0
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
