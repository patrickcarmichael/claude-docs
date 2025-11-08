---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Return Value

The reward function returns an `EvaluateResult` object with:

* `score`: A float between 0.0 and 1.0 indicating how well the code performed.
* `reason`: An overall explanation for the evaluation.
* `metrics`: A dictionary of `MetricResult` objects with detailed information about the execution.
* `error` (optional): A string describing any error during evaluation.

Key metrics include:

* `extracted_code`: The code that was extracted and executed
* `expected_output`: The expected output (if provided or extracted)
* `execution_result`: Details about the execution (success or failure)
* `output_match`: Comparison between actual and expected outputs

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
