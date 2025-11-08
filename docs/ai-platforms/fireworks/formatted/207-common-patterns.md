---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common Patterns

### Creating a Basic Reward Function

```python
from reward_kit import reward_function, EvaluateResult, MetricResult

@reward_function
def my_reward_function(messages, original_messages=None, **kwargs):
    # Your evaluation logic here

    response = messages[-1].get("content", "")
    # Assume calculate_score returns a float between 0.0 and 1.0

    # and calculate_success returns a boolean

    score = calculate_score(response)
    success = calculate_success(response) # Assume calculate_success is defined

    return EvaluateResult(
        score=score,
        reason="Overall evaluation reason for my_reward_function", # Added top-level reason

        metrics={
            "my_metric": MetricResult(
                score=score,
                success=success, # Added success field

                reason="Explanation for the metric score"
            )
        }
    )
```

### Using a Deployed Reward Function

```python
from reward_kit import RewardFunction

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
