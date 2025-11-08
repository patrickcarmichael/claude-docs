---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get updated job status

updated_job = job.get()
if updated_job is None:
    print("Job was deleted")
else:
    print(f"Job state: {updated_job.state}")
```

### `raise_if_bad_state()`

Raises a `RuntimeError` if the job is in a failed, cancelled, or otherwise bad state. This is useful for error handling during training.

**Raises:**

* `RuntimeError` - If the job is in a bad state (failed, cancelled, expired, etc.)
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
