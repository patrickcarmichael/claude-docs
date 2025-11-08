---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool calling

* Response handling
  * v1: Tool calls accessed through `response.tool_calls`
  * v2: Tool calls accessed through `response.message.tool_calls`

* Chat history management
  * v1: Tool calls stored in the response's `chat_history`
  * v2: Append the tool call details (`tool_calls` and `tool_plan`) to the `messages` list

**v1**
```python PYTHON
message = "What's the weather in Toronto?"

res_v1 = co_v1.chat(
    model="command-a-03-2025", message=message, tools=tools_v1
)

print(res_v1.tool_calls)
```
```
[ToolCall(name='get_weather', parameters={'location': 'Toronto'})]
```
**v2**
```python PYTHON
messages = [
    {"role": "user", "content": "What's the weather in Toronto?"}
]

res_v2 = co_v2.chat(
    model="command-a-03-2025", messages=messages, tools=tools_v2
)

if res_v2.message.tool_calls:
    messages.append(
        {
            "role": "assistant",
            "tool_calls": res_v2.message.tool_calls,
            "tool_plan": res_v2.message.tool_plan,
        }
    )

    print(res_v2.message.tool_calls)
```
```
[ToolCallV2(id='get_weather_k88p0m8504w5', type='function', function=ToolCallV2Function(name='get_weather', arguments='{"location":"Toronto"}'))]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
