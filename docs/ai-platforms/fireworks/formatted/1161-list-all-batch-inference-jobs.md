---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## List all batch inference jobs

jobs = BatchInferenceJob.list(account="my-account")

for job in jobs:
    print(f"Job: {job.id}, State: {job.state}, Model: {job.model}")
```

### `delete()`

```python
@staticmethod
delete(job_id: str, account: str, api_key: Optional[str] = None) -> None
```
Deletes a batch inference job.

**Arguments:**

* `job_id` *str* - The job ID or full resource name
* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
