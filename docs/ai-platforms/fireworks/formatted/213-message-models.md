---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Message Models

### Message

The `Message` class represents a single message in a conversation.
```python
from reward_kit import Message

message = Message(
    role="assistant",
    content="This is the response content",
    name=None,  # Optional

    tool_call_id=None,  # Optional

    tool_calls=None,  # Optional

    function_call=None  # Optional

)
```

#### Attributes

* **`role`** (`str`): The role of the message sender. Typically one of:
  * `"user"`: Message from the user
  * `"assistant"`: Message from the assistant
  * `"system"`: System message providing context/instructions

* **`content`** (`str`): The text content of the message.

* **`name`** (`Optional[str]`): Optional name of the sender (for named system messages).

* **`tool_call_id`** (`Optional[str]`): Optional ID for a tool call (used in tool calling).

* **`tool_calls`** (`Optional[List[Dict[str, Any]]]`): Optional list of tool calls in the message.

* **`function_call`** (`Optional[Dict[str, Any]]`): Optional function call information (legacy format).

#### Compatibility

The `Message` class is compatible with OpenAI's `ChatCompletionMessageParam` interface, allowing for easy integration with OpenAI-compatible APIs.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
