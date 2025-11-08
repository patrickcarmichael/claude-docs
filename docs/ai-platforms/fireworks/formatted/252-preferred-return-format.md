---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Preferred return format

return EvaluateResult(
    score=0.75,  # Overall score

    reason="Overall evaluation reason",
    metrics={
        "clarity": MetricResult(score=0.8, success=True, reason="Good clarity"),
        "accuracy": MetricResult(score=0.7, success=False, reason="Minor errors")
    }
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
