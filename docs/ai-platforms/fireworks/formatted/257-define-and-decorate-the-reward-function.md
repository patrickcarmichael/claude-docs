---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define and decorate the reward function

@reward_function
def clarity_reward(messages, original_messages=None, **kwargs) -> EvaluateResult:
    # ... evaluation logic ...

    # Assume score and metric_details are calculated

    score = 0.8
    metric_details = {"clarity_metric": MetricResult(score=0.8, success=True, reason="Very clear")}
    return EvaluateResult(score=score, reason="Clarity evaluation complete.", metrics=metric_details)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
