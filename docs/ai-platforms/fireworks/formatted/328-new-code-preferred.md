---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## New code (preferred)

@reward_function
def my_reward(messages, **kwargs):
    # ...

    return EvaluateResult(
        score=0.75,
        reason="Overall assessment",  # Add an overall reason

        metrics={
            "clarity": MetricResult(
                score=0.8,
                reason="Clear explanation",
                success=True  # Add success flag if applicable

            )
        }
    )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
