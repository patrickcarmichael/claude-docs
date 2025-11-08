---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## score, clarity_score, accuracy_score would be calculated by your logic

clarity_score = 0.8
accuracy_score = 0.7
final_score = 0.75

return EvaluateResult(
    score=final_score,  # Overall score between 0.0 and 1.0

    reason="Overall evaluation based on clarity and accuracy.",
    metrics={    # Component metrics

        "clarity": MetricResult(
            score=clarity_score,
            success=clarity_score >= 0.7,
            reason="The response clearly explains the concept"
        ),
        "accuracy": MetricResult(
            score=accuracy_score,
            success=accuracy_score >= 0.6,
            reason="Contains one minor factual error"
        )
    }
)
```

### EvaluateResult Structure

* **`score`**: The final aggregate score (typically between 0.0 and 1.0).
* **`reason`**: An optional top-level explanation for the overall score.
* **`metrics`**: A dictionary of component metrics (`MetricResult` objects), each with its own score, success flag, and explanation.
* **`error`**: An optional string field to convey errors during evaluation.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
