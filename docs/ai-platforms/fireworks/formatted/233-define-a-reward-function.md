---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define a reward function

def my_reward_fn(messages, **kwargs):
    response = messages[-1].get("content", "")
    response_len = len(response)
    score = min(response_len / 100.0, 1.0)  # Simple score based on length

    success = response_len > 10 # Example success condition: length greater than 10

    return EvaluateResult(
        score=score,
        reason=f"Evaluation based on response length ({response_len} characters).",
        metrics={"length": MetricResult(score=score, success=success, reason=f"Length: {response_len}")}
    )

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
