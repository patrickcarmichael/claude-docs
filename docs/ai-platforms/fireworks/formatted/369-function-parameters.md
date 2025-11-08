---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Function Parameters

A standard reward function has these parameters:
```python
from typing import List, Dict, Optional
from reward_kit import EvaluateResult

def reward_function(
    messages: List[Dict[str, str]],
    original_messages: Optional[List[Dict[str, str]]] = None,
    **kwargs
) -> EvaluateResult:
    # ...

    pass
```

### Required Parameters

* **`messages`**: A list of message dictionaries in the conversation, where each message has at least `"role"` and `"content"` keys. The last message is typically the one being evaluated.

### Optional Parameters

* **`original_messages`**: The conversation context, usually messages before the response being evaluated. If not provided, it defaults to `messages[:-1]`.
* **`**kwargs`**: Additional parameters that can be used to customize the evaluation.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
