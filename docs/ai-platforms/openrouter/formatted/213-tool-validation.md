---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool Validation

Ensure tool calls have proper structure:
```json
{
  "type": "function_call",
  "id": "fc_abc123",
  "call_id": "call_xyz789",
  "name": "get_weather",
  "arguments": "{\"location\":\"Seattle, WA\"}"
}
```
Required fields:

* `type`: Always "function\_call"
* `id`: Unique identifier for the function call object
* `name`: Function name matching tool definition
* `arguments`: Valid JSON string with function parameters
* `call_id`: Unique identifier for the call

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
