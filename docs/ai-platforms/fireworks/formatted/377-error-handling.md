---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Error Handling

Robust reward functions include proper error handling:
```python
from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional

@reward_function
def safe_evaluation(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    try:
        # Ensure we have a valid response to evaluate

        if not messages or messages[-1].get("role") != "assistant":
            return EvaluateResult(
                score=0.0,
                reason="No assistant response found.",
                metrics={"error": MetricResult(
                    score=0.0,
                    success=False,
                    reason="No assistant response found"
                )}
            )

        # Your evaluation logic here

        # ...

        # For example:

        calculated_score = 0.0 # Placeholder for actual logic

        if calculated_score == 0 : raise ValueError("Simulated error")
        return EvaluateResult(score=1.0, reason="Successful evaluation", metrics={})


    except Exception as e:
        # Handle any unexpected errors

        return EvaluateResult(
            score=0.0,
            reason=f"Evaluation error: {str(e)}",
            metrics={"error": MetricResult(
                score=0.0,
                success=False,
                reason=f"Evaluation error: {str(e)}"
            )}
        )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
