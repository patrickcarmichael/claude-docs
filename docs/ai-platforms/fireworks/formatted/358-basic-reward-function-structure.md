---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Reward Function Structure

Here's a simple reward function that evaluates responses based on word count:
```python
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def word_count_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    """
    Evaluate a response based on its word count.

    Args:
        messages: List of conversation messages
        original_messages: Original messages (usually without the response being evaluated)
        **kwargs: Additional parameters

    Returns:
        EvaluateResult with score and metrics information
    """
    # Get the assistant's response (last message)

    if not messages or messages[-1].get("role") != "assistant":
        return EvaluateResult(
            score=0.0,
            reason="No assistant response found in messages.",
            metrics={"error": MetricResult(score=0.0, success=False, reason="No assistant response found")}
        )

    response = messages[-1].get("content", "")

    # Count words and calculate score

    word_count = len(response.split())
    score = min(word_count / 100.0, 1.0)  # Cap at 1.0

    success = word_count > 10 # Example: success if more than 10 words

    return EvaluateResult(
        score=score,
        reason=f"Overall word count evaluation: {word_count} words.",
        metrics={
            "word_count": MetricResult(
                score=score,
                success=success,
                reason=f"Word count: {word_count}"
            )
        }
    )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
