---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Methods

### `__call__`

Call the reward function with the provided messages.
```python
__call__(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult
```

#### Parameters

* **`messages`** (`List[Dict[str, str]]`): List of conversation messages, each with 'role' and 'content' keys.

* **`original_messages`** (`Optional[List[Dict[str, str]]]`): Original conversation messages (for context).
  Defaults to all messages except the last one if not provided.

* **`**kwargs`**: Additional keyword arguments to pass to the function.

#### Returns

* **`EvaluateResult`**: Object with score and metrics.

#### Exceptions

* **`ValueError`**: Raised if no function or endpoint is provided for the selected mode.
* **`TypeError`**: Raised if the function returns an invalid type.
* **`requests.exceptions.RequestException`**: Raised if there is an error calling the remote endpoint.

### `get_trl_adapter`

Create an adapter function for use with the TRL (Transformer Reinforcement Learning) library.
```python
get_trl_adapter() -> Callable
```

#### Returns

* **`Callable`**: A function that takes batch inputs and returns a batch of reward values, compatible with TRL.

#### Adapter Behavior

The returned adapter function:

1. Handles batch inputs (list of message lists or list of strings)
2. Returns a list of reward scores (one for each input)
3. Handles exceptions gracefully, returning 0.0 for any errors

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
