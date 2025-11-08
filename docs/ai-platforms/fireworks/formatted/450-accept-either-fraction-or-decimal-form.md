---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Accept either fraction or decimal form

result = math_reward(
    messages=messages,
    expected_answer=["5/12", "0.41666"], # Accept either form

    tolerance=0.001  # Small tolerance for decimal approximation

)
```

### Original Messages as Reference

If the correct answer is in the original messages, you can extract it automatically:
```python
from reward_kit.rewards.math import math_reward

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
