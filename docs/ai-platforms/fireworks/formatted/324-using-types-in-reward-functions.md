---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using Types in Reward Functions

Here's how to use these types properly in your reward functions:
```python
from reward_kit import reward_function, EvaluateResult, MetricResult, Message
from typing import List, Optional, Dict, Any

@reward_function
def my_reward_function(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    **kwargs
) -> EvaluateResult:
    """
    Example reward function with proper type annotations.
    """
    # Default values

    metadata = metadata or {}

    # Get the assistant's response

    response = messages[-1].get("content", "")

    # Evaluate the response

    clarity_score = evaluate_clarity(response)

    # Create metrics

    metrics = {
        "clarity": MetricResult(
            score=clarity_score,
            reason=f"Clarity score: {clarity_score:.2f}",
            success=clarity_score >= 0.7
        )
    }

    return EvaluateResult(
        score=clarity_score,
        reason=f"Overall quality assessment: {clarity_score:.2f}",
        metrics=metrics
    )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
