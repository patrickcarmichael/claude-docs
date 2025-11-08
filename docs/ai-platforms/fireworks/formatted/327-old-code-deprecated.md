---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Old code (deprecated)

@reward_function
def my_reward(messages, **kwargs):
    # ...

    return RewardOutput(
        score=0.75,
        metrics={
            "clarity": MetricRewardOutput(score=0.8, reason="Clear explanation")
        }
    )

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
