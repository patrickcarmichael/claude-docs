---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a message with tool calls

tool_call_message = Message(
    role="assistant",
    content=None,
    tool_calls=[{
        "id": "call_123",
        "type": "function",
        "function": {
            "name": "get_weather",
            "arguments": '{"location": "San Francisco", "unit": "celsius"}'
        }
    }]
)
```

### Working with EvaluateResult

```python
from reward_kit import EvaluateResult, MetricResult

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
