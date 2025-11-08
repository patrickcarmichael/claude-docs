---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The `@reward_function` Decorator

The `@reward_function` decorator is the core mechanism that transforms a regular Python function into a reward function that can be used for evaluation and deployment.
```python
from reward_kit import reward_function, EvaluateResult, MetricResult

@reward_function
def my_reward_function(messages, original_messages=None, **kwargs):
    # Your evaluation logic here

    score = 0.75 # Example score

    reason = "Overall evaluation reason for my_reward_function"
    metrics_dict = {"example_metric": MetricResult(score=score, success=True, reason="Metric reason")}
    return EvaluateResult(score=score, reason=reason, metrics=metrics_dict)
```

### What the Decorator Does

The `@reward_function` decorator performs several important functions:

1. **Input Validation**: Ensures the function receives the expected parameters
2. **Output Standardization**: Ensures the function returns a properly formatted `EvaluateResult` object
3. **Deployment Capability**: Adds a `.deploy()` method to the function for easy deployment
4. **Backward Compatibility**: Handles legacy return formats (tuples of score and metrics)

### Under the Hood

Internally, the decorator wraps your function with logic that:

1. Processes the input parameters
2. Calls your function with the standardized inputs
3. Handles any exceptions that occur during execution
4. Formats the output as an `EvaluateResult` object
5. Provides deployment capabilities through the `.deploy()` method

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
