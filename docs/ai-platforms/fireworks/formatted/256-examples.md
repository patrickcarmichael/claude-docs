---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

### Basic Usage

```python
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def word_count_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    """Evaluate response based on word count."""
    response = messages[-1].get("content", "")
    word_count = len(response.split())
    score = min(word_count / 100.0, 1.0)
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

### Using Metadata

```python
@reward_function
def configurable_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    metadata: Optional[Dict[str, any]] = None,
    **kwargs
) -> EvaluateResult:
    """Reward function that accepts configuration via metadata."""
    metadata = metadata or {}

    # Get threshold from metadata or use default

    threshold = metadata.get("threshold", 50)

    response = messages[-1].get("content", "")
    word_count = len(response.split())
    score = min(word_count / float(threshold), 1.0)
    success = word_count >= threshold # Example: success if count meets or exceeds threshold

    return EvaluateResult(
        score=score,
        reason=f"Configurable word count. Threshold: {threshold}, Count: {word_count}.",
        metrics={
            "configured_word_count": MetricResult(
                score=score,
                success=success,
                reason=f"Word count: {word_count}, threshold: {threshold}"
            )
        }
    )
```

### Deploying a Reward Function

```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
