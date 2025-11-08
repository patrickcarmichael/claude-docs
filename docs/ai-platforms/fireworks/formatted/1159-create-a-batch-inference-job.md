---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a batch inference job

job = BatchInferenceJob.create(
    model="llama-v3p1-8b-instruct",
    input_dataset_id="my-input-dataset",
    output_dataset_id="my-output-dataset",
    job_id="my-batch-job",
    display_name="My Batch Processing Job",
    inference_parameters={
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9
    }
)
```

### `get()`

```python
@staticmethod
get(job_id: str, account: str, api_key: Optional[str] = None) -> Optional[BatchInferenceJob]
```
Retrieves a batch inference job by its ID.

**Arguments:**

* `job_id` *str* - The job ID or full resource name
* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use

**Returns:**

* A `BatchInferenceJob` object if found, `None` otherwise
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
