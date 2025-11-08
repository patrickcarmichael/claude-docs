---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage

```python
@reward_function
def my_reward_function(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    # Your evaluation logic here

    score = 0.75  # Example score

    return EvaluateResult(
        score=score,
        reason="Overall evaluation reason",
        metrics={"example_metric": MetricResult(score=score, success=True, reason="Metric reason")}
    )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
