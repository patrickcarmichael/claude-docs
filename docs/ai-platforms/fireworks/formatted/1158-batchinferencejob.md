---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## BatchInferenceJob

The `BatchInferenceJob` class provides a convenient way to manage batch inference jobs on Fireworks. It allows you to perform bulk asynchronous inference on large datasets, reducing costs by up to 50%.
```python
class BatchInferenceJob()
```
**Properties:**

* `name` *str* - The full name of the batch inference job (e.g., `accounts/my-account/batchInferenceJobs/test-job-123`)
* `id` *str* - The job identifier (e.g., `test-job-123`)
* `model` *str* - The model used for inference
* `input_dataset_id` *str* - The input dataset identifier
* `output_dataset_id` *str* - The output dataset identifier
* `state` *str* - The current state of the job
* `created_by` *str* - Email of the user who created the job
* `create_time` *str* - Creation timestamp
* `update_time` *str* - Last update timestamp

### `create()`

```python
@staticmethod
create(
    model: str,
    input_dataset_id: str,
    output_dataset_id: Optional[str] = None,
    job_id: Optional[str] = None,
    display_name: Optional[str] = None,
    inference_parameters: Optional[dict] = None,
    api_key: Optional[str] = None,
) -> BatchInferenceJob
```
Creates a new batch inference job.

**Arguments:**

* `model` *str* - The model to use for inference (e.g., `llama-v3p1-8b-instruct` or `accounts/fireworks/models/llama-v3p1-8b-instruct`)
* `input_dataset_id` *str* - The input dataset ID containing JSONL formatted requests
* `output_dataset_id` *str, optional* - The output dataset ID. If not provided, one will be auto-generated
* `job_id` *str, optional* - The job ID. If not provided, one will be auto-generated
* `display_name` *str, optional* - Display name for the job
* `inference_parameters` *dict, optional* - Dict of inference parameters:
  * `max_tokens` *int* - Maximum number of tokens to generate
  * `temperature` *float* - Sampling temperature (0-2)
  * `top_p` *float* - Top-p sampling parameter
  * `top_k` *int* - Top-k sampling parameter
  * `n` *int* - Number of completions per request
  * `extra_body` *str* - Additional parameters as JSON string
* `api_key` *str, optional* - The API key to use

**Returns:**

* A `BatchInferenceJob` object
```python
from fireworks import BatchInferenceJob

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
