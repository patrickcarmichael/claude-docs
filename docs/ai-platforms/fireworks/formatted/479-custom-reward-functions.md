---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Custom Reward Functions

You can create custom reward functions for domain-specific evaluation:
```python
@reward_function
def domain_specific_reward(response: str, expected_response: str) -> float:
    # Custom logic for your domain

    score = 0.0

    # Example: Check for specific keywords

    if "important_keyword" in response.lower():
        score += 0.5

    # Example: Length consideration

    if 50 <= len(response) <= 200:
        score += 0.3

    # Example: Accuracy component

    if response.strip() == expected_response.strip():
        score += 0.2

    return min(score, 1.0)  # Cap at 1.0

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
