---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get an existing batch inference job

job = BatchInferenceJob.get(
    job_id="my-batch-job",
    account="my-account"
)

if job:
    print(f"Job state: {job.state}")
    print(f"Created by: {job.created_by}")
```

### `list()`

```python
@staticmethod
list(
    account: str,
    api_key: Optional[str] = None,
    page_size: int = 50
) -> list[BatchInferenceJob]
```
Lists batch inference jobs in an account.

**Arguments:**

* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use
* `page_size` *int, optional* - Number of jobs to return per page. Defaults to 50

**Returns:**

* A list of `BatchInferenceJob` objects
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
