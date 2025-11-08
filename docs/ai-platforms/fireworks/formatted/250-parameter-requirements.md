---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parameter Requirements

Functions decorated with `@reward_function` should accept the following parameters:

* **`messages`** (`List[Dict[str, str]]`): Required. List of conversation messages, with the last message typically being the one evaluated.

* **`original_messages`** (`Optional[List[Dict[str, str]]]`): Optional. The conversation context, without the message being evaluated.

* **`**kwargs`**: Optional. Additional parameters (like metadata) that can be passed to the function.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
