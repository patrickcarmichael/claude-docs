---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Evaluation Output Types

### `EvaluateResult` Class

```python
from reward_kit import EvaluateResult, MetricResult

result = EvaluateResult(
    score=0.75,  # Overall score between 0.0 and 1.0

    reason="The response meets quality requirements",  # Optional explanation

    metrics={    # Component metrics dictionary

        "clarity": MetricResult(
            success=True,
            score=0.8,
            reason="The response is clear and concise"
        ),
        "accuracy": MetricResult(
            score=0.7,
            reason="Contains one minor factual error",
            success=True
        )
    }
)
```
The `EvaluateResult` class represents the complete result of a reward function evaluation, containing:

* An overall score (typically 0.0 to 1.0)
* An optional reason/explanation for the overall score
* A dictionary of component metrics
* An optional error field for handling evaluation failures

### `MetricResult` Class

```python
from reward_kit import MetricResult

metric = MetricResult(
    score=0.8,  # Score for this specific metric

    reason="Explanation for why this score was assigned",  # Description

    success=True  # Indicates if the metric condition was met (e.g., pass/fail)

)
```
The `MetricResult` class represents a single component metric in the evaluation, containing:

* A score value (typically 0.0 to 1.0)
* A reason/explanation for the score
* A `success: bool` flag indicating if the metric condition was met (e.g., pass/fail).

### Removed Output Types (Legacy)

The `RewardOutput` and `MetricRewardOutput` classes were used in older versions but have now been fully removed. All reward functions should now use `EvaluateResult` and `MetricResult`.

If you are migrating from an older version that used `RewardOutput`, please refer to the "Migration from RewardOutput to EvaluateResult" section below.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
