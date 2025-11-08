---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Constructor

```python
RewardFunction(
    func: Optional[Callable] = None,
    func_path: Optional[str] = None,
    mode: str = "local",
    endpoint: Optional[str] = None,
    name: Optional[str] = None,
    model_id: Optional[str] = None,
    **kwargs
)
```

### Parameters

* **`func`** (`Optional[Callable]`): The local function to use (for mode="local").

* **`func_path`** (`Optional[str]`): A string path to a function (e.g., "module.submodule:function\_name").

* **`mode`** (`str`): The mode of operation. Options:
  * `"local"`: Run the function locally
  * `"remote"`: Call a remote endpoint
  * `"fireworks_hosted"`: Use a Fireworks-hosted model

* **`endpoint`** (`Optional[str]`): The URL of the remote endpoint (for mode="remote").

* **`name`** (`Optional[str]`): The name of the deployed evaluator (for mode="remote").
  If provided and endpoint is not, the endpoint will be constructed from the name.

* **`model_id`** (`Optional[str]`): The ID of the Fireworks-hosted model (for mode="fireworks\_hosted").

* **`**kwargs`**: Additional keyword arguments to pass to the function when called.

### Exceptions

* **`ValueError`**: Raised if required parameters for the specified mode are missing or if an invalid mode is provided.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
