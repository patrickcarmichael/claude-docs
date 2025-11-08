---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The new model is now available at job.output_model

```

### `delete_deployment(ignore_checks: bool = False, wait: bool = True)`

Deletes the deployment associated with this LLM instance if one exists.

**Arguments:**

* `ignore_checks` *bool, optional* - Whether to ignore safety checks. Defaults to False.
* `wait` *bool, optional* - Whether to wait for deletion to complete. Defaults to True.
```python
llm.delete_deployment(ignore_checks=True)
```

### `get_time_to_last_token_mean()`

Returns the mean time to last token for non-streaming requests. If no metrics are available, returns None.

**Returns:**

* A float representing the mean time to last token, or None if no metrics are available.
```python
time_to_last_token_mean = llm.get_time_to_last_token_mean()
```

### `with_deployment_type()`

Returns a new LLM instance with the specified deployment type.

**Arguments:**

* `deployment_type` *str* - The deployment type to use ("serverless", "on-demand", "auto", or "on-demand-lora")

**Returns:**

* A new `LLM` instance with the specified deployment type
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
