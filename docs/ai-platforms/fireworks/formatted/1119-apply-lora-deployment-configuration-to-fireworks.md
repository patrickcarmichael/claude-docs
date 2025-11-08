---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Apply LoRA deployment configuration to Fireworks

fine_tuned_with_lora.apply()
```

#### Required Arguments

* `model` *str* - The model identifier to use (e.g., `accounts/fireworks/models/llama-v3p2-3b-instruct`)
* `deployment_type` *str* - The type of deployment to use. Must be one of:
  * `"serverless"`: Uses Fireworks' shared serverless infrastructure
  * `"on-demand"`: Uses dedicated resources for your deployment
  * `"auto"`: Automatically selects the most cost-effective option (recommended for experimentation)
  * `"on-demand-lora"`: For LoRA addons that require dedicated resources

#### Optional Arguments

**Deployment Configuration**

* `id` *str, optional* - Deployment ID to identify the deployment. Required when deployment\_type is "on-demand". Can be any simple string (e.g., `"my-deployment"`) - does not need to follow the format `"accounts/account_id/deployments/model_id"`.
* `deployment_display_name` *str, optional* - Display name for the deployment. Defaults to the filename where the LLM was instantiated. If a deployment with the same display name and model already exists, the SDK will try and re-use it.
* `base_id` *str, optional* - Base deployment ID for LoRA addons. Required when deployment\_type is "on-demand-lora".

**Authentication & API**

* `api_key` *str, optional* - Your Fireworks API key
* `base_url` *str, optional* - Base URL for API calls. Defaults to "[https://api.fireworks.ai/inference/v1](https://api.fireworks.ai/inference/v1)"
* `max_retries` *int, optional* - Maximum number of retry attempts. Defaults to 10

**Scaling Configuration**

* `scale_up_window` *timedelta, optional* - Time to wait before scaling up after increased load. Defaults to 1 second
* `scale_down_window` *timedelta, optional* - Time to wait before scaling down after decreased load. Defaults to 1 minute
* `scale_to_zero_window` *timedelta, optional* - Time of inactivity before scaling to zero. Defaults to 5 minutes

**Hardware & Performance**

* `accelerator_type` *str, optional* - Type of GPU accelerator to use
* `region` *str, optional* - Region for deployment
* `multi_region` *str, optional* - Multi-region configuration
* `min_replica_count` *int, optional* - Minimum number of replicas
* `max_replica_count` *int, optional* - Maximum number of replicas
* `replica_count` *int, optional* - Fixed number of replicas
* `accelerator_count` *int, optional* - Number of accelerators per replica
* `precision` *str, optional* - Model precision (e.g., "FP16", "FP8")
* `world_size` *int, optional* - World size for distributed training
* `generator_count` *int, optional* - Number of generators
* `disaggregated_prefill_count` *int, optional* - Number of disaggregated prefill instances
* `disaggregated_prefill_world_size` *int, optional* - World size for disaggregated prefill
* `max_batch_size` *int, optional* - Maximum batch size for inference
* `max_peft_batch_size` *int, optional* - Maximum batch size for PEFT operations
* `kv_cache_memory_pct` *int, optional* - Percentage of memory for KV cache

**Advanced Features**

* `enable_addons` *bool, optional* - Enable LoRA addons support
* `live_merge` *bool, optional* - Enable live merging
* `draft_token_count` *int, optional* - Number of tokens to generate per step for speculative decoding
* `draft_model` *str, optional* - Model to use for speculative decoding
* `ngram_speculation_length` *int, optional* - Length of previous input sequence for N-gram speculation
* `long_prompt_optimized` *bool, optional* - Optimize for long prompts
* `temperature` *float, optional* - Sampling temperature for generation
* `num_peft_device_cached` *int, optional* - Number of PEFT devices to cache

**Monitoring & Metrics**

* `enable_metrics` *bool, optional* - Enable metrics collection. Currently supports time to last token for non-streaming requests.
* `perf_metrics_in_response` *bool, optional* - Include performance metrics in API responses

**Additional Configuration**

* `description` *str, optional* - Description of the deployment
* `annotations` *dict\[str, str], optional* - Annotations for the deployment
* `cluster` *str, optional* - Cluster identifier
* `enable_session_affinity` *bool, optional* - Enable session affinity
* `direct_route_api_keys` *list\[str], optional* - List of API keys for direct routing
* `direct_route_type` *str, optional* - Type of direct routing
* `direct_route_handle` *str, optional* - Direct route handle

### `apply(wait: bool = True)`

Ensures the deployment is ready and returns the deployment. Like Terraform apply, this will ensure the deployment is ready.
```python
llm.apply(wait=True)
```

### `create_supervised_fine_tuning_job()`

Creates a new supervised fine-tuning job and blocks until it is ready. See the [SupervisedFineTuningJob](#supervisedfinetuningjob) section for details on the parameters.

**Returns:**

* An instance of `SupervisedFineTuningJob`.
```python
job = llm.create_supervised_fine_tuning_job(
    display_name="my-fine-tuning-job",
    dataset_or_id=dataset,
    epochs=3,
    learning_rate=1e-5
)
```

### `reinforcement_step()`

Performs a reinforcement learning step for training. This method creates a new model checkpoint by fine-tuning the current model on the provided dataset with reinforcement learning.

**Arguments:**

* `dataset` *Dataset* - The dataset containing training examples with rewards
* `output_model` *str* - The name of the output model to create
* `lora_rank` *int, optional* - Rank for LoRA fine-tuning. Defaults to 16
* `learning_rate` *float, optional* - Learning rate for training. Defaults to 0.0001
* `max_context_length` *int, optional* - Maximum context length for the model. Defaults to 8192
* `epochs` *int, optional* - Number of training epochs. Defaults to 1
* `batch_size` *int, optional* - Batch size for training. Defaults to 32768
* `accelerator_count` *int, optional* - Number of accelerators to use for training. Defaults to 1
* `accelerator_type` *str, optional* - Type of GPU accelerator to use for training. Supported values: `"NVIDIA_A100_80GB"`, `"NVIDIA_H100_80GB"`, `"NVIDIA_H200_141GB"`. Defaults to `"NVIDIA_A100_80GB"`

>   **📝 Note**
>
> When running on a trained LoRA (i.e., when using a model that is already a LoRA fine-tuned checkpoint), the training parameters (`lora_rank`, `learning_rate`, `max_context_length`, `epochs`, `batch_size`) must always be the same as those used in the original LoRA training. Changing these parameters when continuing training from a LoRA checkpoint is not supported and will result in an error.

**Returns:**

* An instance of [`ReinforcementStep`](/tools-sdks/python-client/sdk-reference#reinforcementstep) representing the training job

**Note:** The output model name must not already exist. If a model with the same name exists, a `ValueError` will be raised.
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
