---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool call ID

* v1: Tool calls do not emit tool call IDs
* v2: Tool calls emit tool call IDs. This will help the model match tool results to the right tool call.

**v1**
```python PYTHON
tool_results = [
    {
        "call": {
            "name": "<tool name>",
            "parameters": {"<param name>": "<param value>"},
        },
        "outputs": [{"<key>": "<value>"}],
    },
]
```
**v2**
```python PYTHON
messages = [
    {
        "role": "tool",
        "tool_call_id": "123",
        "content": [
            {
                "type": "document",
                "document": {
                    "id": "123",
                    "data": {"<key>": "<value>"},
                },
            }
        ],
    }
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
