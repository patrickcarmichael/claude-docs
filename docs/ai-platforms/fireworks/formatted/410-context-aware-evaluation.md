---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Context-Aware Evaluation

Consider context when evaluating responses:
```python
@reward_function
def context_aware_reward(response: str, expected_response: str, context: dict = None) -> float:
    """
    Reward function that considers context information.
    """
    base_score = accuracy(response, expected_response)

    if context:
        # Adjust score based on difficulty

        difficulty = context.get('difficulty', 'medium')
        if difficulty == 'hard' and base_score > 0.8:
            base_score *= 1.2  # Bonus for hard questions

        elif difficulty == 'easy' and base_score < 0.5:
            base_score *= 0.8  # Penalty for easy questions

        # Consider response time if available

        response_time = context.get('response_time_seconds', 0)
        if response_time > 0:
            # Slight bonus for quick accurate responses

            time_bonus = max(0, (10 - response_time) / 100)
            base_score += time_bonus

    return min(base_score, 1.0)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
