---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## ReinforcementStep

The `ReinforcementStep` class represents a reinforcement learning training step.
It provides methods to monitor and manage the training process.
```python
class ReinforcementStep()
```
**Properties:**

* `state` *str* - The current state of the training job (e.g., "JOB\_STATE\_RUNNING", "JOB\_STATE\_COMPLETED")
* `output_model` *str* - The identifier of the output model (e.g., `accounts/my-account/models/my-improved-model`)
* `is_completed` *bool* - Whether the training job has completed successfully

### `get()`

Retrieves the current state of the training job from the server.

**Returns:**

* A `ReinforcementStep` object with updated state, or `None` if the job no longer exists
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
