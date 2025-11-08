---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Combining Rewards

You can combine multiple reward functions:
```python
@reward_function
def combined_reward(response: str, expected_response: str) -> float:
    acc_score = accuracy(response, expected_response)
    len_score = length_penalty(response, min_length=10, max_length=100)

    return 0.8 * acc_score + 0.2 * len_score
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
