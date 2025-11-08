---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## SupervisedFineTuningJob

The `SupervisedFineTuningJob` class manages fine-tuning jobs on Fireworks. It provides a convenient interface for creating, monitoring, and managing fine-tuning jobs.
```python
class SupervisedFineTuningJob()
```
**Properties:**

* `output_model` *str* - The identifier of the output model (e.g., `accounts/my-account/models/my-finetuned-model`)
* `output_llm` *LLM* - An LLM instance associated with the output model
* `id` *str* - The job ID
* `display_name` *str* - The display name of the job
* `name` *str* - The full name of the job
* `url` *str* - The URL to view the job in the Fireworks dashboard

### Instantiation

You do not need to directly instantiate a `SupervisedFineTuningJob` object. Instead, you should use the `.create_supervised_fine_tuning_job()` method on the `LLM` object and pass in the following required and optional arguments.

#### Required Arguments

* `display_name` *str* - A unique name for the fine-tuning job. Must only contain lowercase a-z, 0-9, and hyphen (-).
* `dataset_or_id` *Union\[Dataset, str]* - The dataset to use for fine-tuning, either as a Dataset object or dataset ID

#### Optional Arguments

**Training Configuration**

* `epochs` *int, optional* - Number of training epochs
* `learning_rate` *float, optional* - Learning rate for training
* `lora_rank` *int, optional* - Rank for LoRA fine-tuning
* `jinja_template` *str, optional* - Template for formatting training examples
* `early_stop` *bool, optional* - Whether to enable early stopping
* `max_context_length` *int, optional* - Maximum context length for the model
* `base_model_weight_precision` *str, optional* - Precision for base model weights
* `batch_size` *int, optional* - Batch size for training

**Hardware Configuration**

* `accelerator_type` *str, optional* - Type of GPU accelerator to use
* `accelerator_count` *int, optional* - Number of accelerators to use
* `is_turbo` *bool, optional* - Whether to use turbo mode for faster training
* `region` *str, optional* - Region for deployment
* `nodes` *int, optional* - Number of nodes to use

**Evaluation & Monitoring**

* `evaluation_dataset` *str, optional* - Dataset ID to use for evaluation
* `eval_auto_carveout` *bool, optional* - Whether to automatically carve out evaluation data
* `wandb_config` *WandbConfig, optional* - Configuration for Weights & Biases integration

**Job Management**

* `output_model` *str, optional* - The name of the output model to create. If not provided, it will be the same as the display\_name argument.

### `sync()`

Creates the job if it doesn't exist, otherwise returns the existing job. If previous job failed, deletes it and creates a new one.

**Returns:**

* *SupervisedFineTuningJob* - The synced job object
```python
job = job.sync()
```

### `wait_for_completion()`

Polls the job status until it is complete and returns the job object.

**Returns:**

* *SupervisedFineTuningJob* - The completed job object
```python
job = job.wait_for_completion()
```

### `await_for_completion()`

Asynchronously polls the job status until it is complete and returns the job object.

**Returns:**

* *SupervisedFineTuningJob* - The completed job object
```python
job = await job.await_for_completion()
```

### `delete()`

Deletes the job.
```python
job.delete()
```

### `adelete()`

Asynchronously deletes the job.
```python
await job.adelete()
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
