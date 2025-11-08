---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Delete a batch inference job

BatchInferenceJob.delete(
    job_id="my-batch-job",
    account="my-account"
)
```

### `to_dict()`

```python
@staticmethod
to_dict(proto: BatchInferenceJob) -> dict
```
Converts a batch inference job proto to a friendly dictionary representation.

**Arguments:**

* `proto` *BatchInferenceJob* - The batch inference job proto object

**Returns:**

* A dictionary with human-readable field values
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
