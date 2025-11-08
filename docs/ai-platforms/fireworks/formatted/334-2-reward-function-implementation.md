---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Reward Function Implementation

Create your reward function using the `@reward_function` decorator or by structuring your evaluation logic within a script that can be called by an evaluation configuration.

### Example: Basic Reward Function

```python
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def helpfulness_reward(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    """Evaluate the helpfulness of a response."""
    # Get the assistant's response

    response_content = messages[-1].get("content", "").lower()

    # Define helpful keywords

    helpful_keywords = ["help", "assist", "solve", "solution", "answer", "explain"]

    # Count helpful keywords

    keyword_count = sum(1 for keyword in helpful_keywords if keyword in response_content)

    # Calculate score based on keyword presence (simple example)

    score = min(keyword_count / 3.0, 1.0)  # Cap at 1.0

    success = keyword_count > 0 # Example success condition

    return EvaluateResult(
        score=score,
        reason=f"Helpfulness evaluation based on {keyword_count} keywords.",
        metrics={
            "helpfulness": MetricResult(
                score=score,
                success=success,
                reason=f"Found {keyword_count} helpful keywords"
            )
        }
    )
```
This function can then be referenced in your evaluation configuration.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
