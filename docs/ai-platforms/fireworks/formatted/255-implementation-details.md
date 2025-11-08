---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Implementation Details

### Validation Logic

The decorator performs the following validations:

1. Ensures the decorated function has the expected parameters
2. Validates that the return value is an `EvaluateResult` or a compatible tuple
3. Handles exceptions that occur during function execution

### Backward Compatibility

For backward compatibility, the decorator supports the legacy tuple return format:
```python
return score, component_scores_dict
```
This gets automatically converted to an `EvaluateResult` object.

### Deployment Process

When `.deploy()` is called, the decorator:

1. Extracts the function's source code
2. Creates a wrapper that handles the Fireworks evaluation format
3. Creates a temporary directory with the wrapped function
4. Uploads and registers the function with the Fireworks API

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
