---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best Practices for Data Types

1. **Use EvaluateResult**: Always return EvaluateResult from your reward functions
2. **Use Type Hints**: Include proper type annotations in your functions
3. **Provide Reasons**: Include clear reason strings for both overall score and individual metrics
4. **Use `success`**: Set the `success: bool` flag in `MetricResult` to indicate pass/fail or whether a specific condition for that metric was met.
5. **Default Values**: Provide defaults for optional parameters
6. **Validation**: Validate input data before processing
7. **Error Handling**: Handle missing or malformed data gracefully
8. **Documentation**: Document the expected format for your inputs and outputs

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
