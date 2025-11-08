---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Custom Configurations

You can customize the reward function with various parameters:
```python
from reward_kit.rewards.accuracy_length import cosine_scaled_accuracy_length_reward

result = cosine_scaled_accuracy_length_reward(
    messages=messages,
    ground_truth="Expected answer",
    max_length=500,                # Maximum ideal length

    correctness_weight=0.7,        # Weight for accuracy component

    length_weight=0.3,             # Weight for length component

    min_value_correct=0.5,         # Minimum score for correct answers

    max_value_correct=1.0,         # Maximum score for correct answers

    min_value_wrong=0.0,           # Minimum score for wrong answers

    max_value_wrong=0.3,           # Maximum score for wrong answers

    token_method="whitespace"      # Method to count tokens

)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
