---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Force a specific tool

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2-instruct-0905",
    messages=[{"role": "user", "content": "What's the weather?"}],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "get_weather"}},
    temperature=0.1
)
```
>   **📝 Note**
>
> Some models support parallel tool calling, where multiple tools can be called in a single response. Check the model's capabilities before relying on this feature.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
