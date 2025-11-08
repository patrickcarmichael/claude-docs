---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Added Methods

### `.deploy()`

The decorator adds a `.deploy()` method to the function, allowing it to be deployed to Fireworks.
```python
evaluation_id = my_reward_function.deploy(
    name="my-evaluator",
    description="Evaluates responses based on clarity and accuracy",
    account_id=None,  # Optional, defaults to configured account

    auth_token=None,  # Optional, defaults to configured token

    force=False,  # Set to True to overwrite if it already exists

    providers=None  # Optional model providers configuration

)
```

#### Parameters

* **`name`** (`str`): Required. ID for the deployed evaluator.

* **`description`** (`str`): Optional. Human-readable description of the evaluator.

* **`account_id`** (`Optional[str]`): Optional. Fireworks account ID. If not provided, will be read from config or environment.

* **`auth_token`** (`Optional[str]`): Optional. Authentication token. If not provided, will be read from config or environment.

* **`force`** (`bool`): Optional. Whether to overwrite an existing evaluator with the same name. Default is False.

* **`providers`** (`Optional[List[Dict[str, str]]]`): Optional. List of provider configurations. If not provided, uses a default provider.

#### Returns

* **`str`**: The evaluation ID that can be used in RL training.

#### Exceptions

* **`ValueError`**: Raised if authentication fails or required parameters are missing.
* **`requests.exceptions.HTTPError`**: Raised if the API request fails.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
