---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Evaluate with custom extraction patterns

result = math_reward(
    messages=messages,
    expected_answer="28.27 cm^2",
    extract_boxed_only=True,  # Only look for answers in \boxed{} environments

    ignore_units=False,       # Consider units in the comparison

    tolerance=0.01            # Allow for slight differences in rounding

)
```

### Multiple Valid Answers

Sometimes, multiple forms of the same answer are acceptable. You can evaluate against multiple correct answers:
```python
from reward_kit.rewards.math import math_reward

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
