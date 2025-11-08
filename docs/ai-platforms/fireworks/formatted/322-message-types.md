---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Message Types

### The `Message` Class

```python
from reward_kit import Message

message = Message(
    role="assistant",
    content="This is the response content",
    name=None,  # Optional

    tool_call_id=None,  # Optional, for tool calling

    tool_calls=None,  # Optional, for tool calling

    function_call=None  # Optional, for function calling

)
```
The `Message` class represents a single message in a conversation and is compatible with the OpenAI message format.

### Message Dictionary Format

When working with reward functions, messages are often passed as dictionaries:
```python
message_dict = {
    "role": "assistant",
    "content": "This is the response content"
}
```
The minimum required fields are:

* `role`: The sender of the message (`"user"`, `"assistant"`, or `"system"`)
* `content`: The text content of the message

Additional fields for function/tool calling may include:

* `name`: Name of the sender (for named system messages)
* `tool_calls`: Tool call information
* `function_call`: Function call information (legacy format)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
