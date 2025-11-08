---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a new LLM with performance metrics enabled

llm_with_metrics = llm.with_perf_metrics_in_response(True)
```

### `scale_to_zero()`

Sends a request to scale the deployment to 0 replicas but does not wait for it to complete.

**Returns:**

* The deployment object, or None if no deployment exists
```python
deployment = llm.scale_to_zero()
```

### `scale_to_1_replica()`

Scales the deployment to at least 1 replica.
```python
llm.scale_to_1_replica()
```

### `get_deployment()`

Returns the deployment associated with this LLM instance, or None if no deployment exists.

**Returns:**

* The deployment object, or None if no deployment exists
```python
deployment = llm.get_deployment()
```

### `is_peft_addon()`

Checks if this LLM is a PEFT (Parameter-Efficient Fine-Tuning) addon.

**Returns:**

* True if this LLM is a PEFT addon, False otherwise
```python
is_peft = llm.is_peft_addon()
```

### `list_models()`

Lists all models available to your account.

**Returns:**

* A list of model objects
```python
models = llm.list_models()
```

### `get_model()`

Gets the model object for this LLM's model.

**Returns:**

* The model object, or None if the model doesn't exist
```python
model = llm.get_model()
```

### `is_available_on_serverless()`

Checks if the model is available on serverless infrastructure.

**Returns:**

* True if the model is available on serverless, False otherwise
```python
is_serverless = llm.is_available_on_serverless()
```

### `model_id()`

Returns the model ID, which is the model name plus the deployment name if it exists. This is used for the "model" arg when calling the model.

**Returns:**

* The model ID string
```python
model_id = llm.model_id()
```

### `supports_serverless_lora()`

Checks if the model supports serverless LoRA deployment.

**Returns:**

* True if the model supports serverless LoRA, False otherwise
```python
supports_lora = llm.supports_serverless_lora()
```

### `list_fireworks_models()`

Lists all models available on the Fireworks account.

**Returns:**

* A list of model objects from the Fireworks account
```python
fireworks_models = llm.list_fireworks_models()
```

### `is_model_on_fireworks_account()`

Checks if the model is on the Fireworks account.

**Arguments:**

* `model` *str* - The model identifier to check

**Returns:**

* The model object if it exists on the Fireworks account, None otherwise
```python
model_obj = llm.is_model_on_fireworks_account("accounts/fireworks/models/llama-v3p2-3b-instruct")
```

### `is_model_available_on_serverless()`

Checks if a specific model is available on serverless infrastructure.

**Arguments:**

* `model` *str* - The model identifier to check

**Returns:**

* True if the model is available on serverless, False otherwise
```python
is_serverless = llm.is_model_available_on_serverless("accounts/fireworks/models/llama-v3p2-3b-instruct")
```

### `is_model_deployed_on_serverless_account()`

Checks if a model is deployed on a serverless-enabled account.

**Arguments:**

* `model` *SyncModel* - The model object to check

**Returns:**

* True if the model is deployed on a supported serverless account, False otherwise
```python
model_obj = llm.get_model()
if model_obj:
    is_deployed = llm.is_model_deployed_on_serverless_account(model_obj)
```typescript

### `completions.create()` and `completions.acreate()`

Creates a text completion using the LLM. These methods are OpenAI compatible and follow the same interface as described in the [OpenAI Completions API](https://platform.openai.com/docs/api-reference/completions/create). Use `create()` for synchronous calls and `acreate()` for asynchronous calls.

**Arguments:**

* `prompt` *str* - The prompt to complete
* `stream` *bool, optional* - Whether to stream the response. Defaults to False
* `images` *list\[str], optional* - List of image URLs for multimodal models
* `max_tokens` *int, optional* - The maximum number of tokens to generate
* `logprobs` *int, optional* - Number of log probabilities to return
* `echo` *bool, optional* - Whether to echo the prompt in the response
* `temperature` *float, optional* - Sampling temperature between 0 and 2. If not provided, uses the LLM's default temperature
* `top_p` *float, optional* - Nucleus sampling parameter
* `top_k` *int, optional* - Top-k sampling parameter (must be between 0 and 100)
* `frequency_penalty` *float, optional* - Frequency penalty for repetition
* `presence_penalty` *float, optional* - Presence penalty for repetition
* `repetition_penalty` *float, optional* - Repetition penalty
* `reasoning_effort` *str, optional* - How much effort the model should put into reasoning
* `mirostat_lr` *float, optional* - Mirostat learning rate
* `mirostat_target` *float, optional* - Mirostat target entropy
* `n` *int, optional* - Number of completions to generate
* `ignore_eos` *bool, optional* - Whether to ignore end-of-sequence tokens
* `stop` *str or list\[str], optional* - Stop sequences
* `response_format` *dict, optional* - An object specifying the format that the model must output
* `context_length_exceeded_behavior` *str, optional* - How to handle context length exceeded
* `user` *str, optional* - User identifier
* `extra_headers` *dict, optional* - Additional headers to include in the request
* `**kwargs` - Additional parameters supported by the OpenAI API

**Returns:**

* `Completion` when `stream=False` (default)
* `Generator[Completion, None, None]` when `stream=True` (sync version)
* `AsyncGenerator[Completion, None]` when `stream=True` (async version)
```python
import asyncio
from fireworks import LLM

llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
