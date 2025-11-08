---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Assume base_score and metrics are calculated based on messages

def calculate_base_score_and_metrics(response_content: str, min_length: int) -> tuple[float, dict]:
    # Dummy implementation

    current_length = len(response_content)
    score = 1.0 if current_length >= min_length else 0.5
    return score, {"length_check": MetricResult(score=score, success=current_length >= min_length, reason=f"Length {current_length} vs min {min_length}")}

@reward_function
def configurable_evaluation(
    messages: List[Dict[str, str]], # Added type hints

    original_messages: Optional[List[Dict[str, str]]] = None, # Added type hints

    metadata: Optional[Dict[str, Any]] = None,
    **kwargs
) -> EvaluateResult:
    """Reward function that supports configuration via metadata."""
    metadata = metadata or {}
    response_content = messages[-1].get("content", "")

    # Get configurable thresholds from metadata

    min_length = metadata.get("min_length", 50)
    max_score_cap = metadata.get("max_score_cap", 1.0) # Renamed to avoid conflict with 'score'

    weight_factor = metadata.get("weight_factor", 1.0)

    # Use these parameters in your evaluation

    base_score, metrics = calculate_base_score_and_metrics(response_content, min_length)

    # Apply any metadata-based adjustments to the final score

    final_score = base_score * weight_factor
    final_score = min(final_score, max_score_cap) # Cap the score

    return EvaluateResult(score=final_score, reason="Configurable evaluation complete.", metrics=metrics)
```
When calling the function, you can pass this metadata:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
