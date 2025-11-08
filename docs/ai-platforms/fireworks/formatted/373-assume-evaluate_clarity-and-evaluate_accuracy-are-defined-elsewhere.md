---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Assume evaluate_clarity and evaluate_accuracy are defined elsewhere

def evaluate_clarity(response: str) -> float: return 0.8
def evaluate_accuracy(response: str) -> float: return 0.6


@reward_function
def comprehensive_evaluation(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    response = messages[-1]["content"]
    metrics = {}

    # Evaluate clarity

    clarity_score = evaluate_clarity(response)
    metrics["clarity"] = MetricResult(
        score=clarity_score,
        success=clarity_score >= 0.7,
        reason=f"Clarity score: {clarity_score:.2f}"
    )

    # Evaluate accuracy

    accuracy_score = evaluate_accuracy(response)
    metrics["accuracy"] = MetricResult(
        score=accuracy_score,
        success=accuracy_score >= 0.6,
        reason=f"Accuracy score: {accuracy_score:.2f}"
    )

    # Combine scores (weighted average)

    final_score = clarity_score * 0.4 + accuracy_score * 0.6

    return EvaluateResult(score=final_score, reason="Comprehensive evaluation complete.", metrics=metrics)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
