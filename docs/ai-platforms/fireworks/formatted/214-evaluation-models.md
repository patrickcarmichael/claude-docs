---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Evaluation Models

### EvaluateResult

The `EvaluateResult` class represents the complete result of an evaluator with multiple metrics.
```python
from reward_kit import EvaluateResult, MetricResult

result = EvaluateResult(
    score=0.75,
    reason="Overall good response with minor issues",
    metrics={
        "clarity": MetricResult(score=0.8, reason="Clear and concise", success=True),
        "accuracy": MetricResult(score=0.7, reason="Contains a minor factual error", success=True)
    },
    error=None  # Optional error message

)
```

#### Attributes

* **`score`** (`float`): The overall evaluation score, typically between 0.0 and 1.0.

* **`reason`** (`Optional[str]`): Optional explanation for the overall score.

* **`metrics`** (`Dict[str, MetricResult]`): Dictionary of component metrics.

* **`error`** (`Optional[str]`): Optional error message if the evaluation encountered a problem.

### MetricResult

The `MetricResult` class represents a single metric in an evaluation.
```python
from reward_kit import MetricResult

metric = MetricResult(
    score=0.8,
    reason="The response provides a clear explanation with appropriate examples",
    success=True
)
```

#### Attributes

* **`score`** (`float`): The score for this specific metric, typically between 0.0 and 1.0.

* **`reason`** (`str`): Explanation for why this score was assigned.

* **`success`** (`bool`): Indicates whether the metric condition was met (e.g., pass/fail).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
