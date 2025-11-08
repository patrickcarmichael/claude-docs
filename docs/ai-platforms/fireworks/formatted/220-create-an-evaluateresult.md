---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an EvaluateResult

eval_result = EvaluateResult(
    score=0.75,
    reason="Overall good response with some minor issues",
    metrics={
        "clarity": MetricResult(score=0.8, reason="Clear and concise explanation", success=True),
        "accuracy": MetricResult(score=0.7, reason="Contains one minor factual error", success=True),
        "relevance": MetricResult(score=0.75, reason="Mostly relevant to the query", success=True)
    }
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
