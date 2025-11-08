---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming

* Event containing content:
  * v1: `chunk.event_type == "text-generation"`
  * v2: `chunk.type == "content-delta"`

* Accessing response content:
  * v1: `chunk.text`
  * v2: `chunk.delta.message.content.text`

* Events containing citations:
  * v1: `chunk.event_type == "citation-generation"`
  * v2: `chunk.type == "citation-start"`

* Accessing citations:
  * v1: `chunk.citations`
  * v2: `chunk.delta.message.citations`

**v1**
```python PYTHON
tool_content_v1 = []
if res_v1.tool_calls:
    for tc in res_v1.tool_calls:
        tool_call = {"name": tc.name, "parameters": tc.parameters}
        tool_result = functions_map[tc.name](**tc.parameters)
        tool_content_v1.append(
            {"call": tool_call, "outputs": [tool_result]}
        )

res_v1 = co_v1.chat_stream(
    message="",
    tools=tools_v1,
    tool_results=tool_content_v1,
    chat_history=res_v1.chat_history,
)

for chunk in res_v1:
    if chunk.event_type == "text-generation":
        print(chunk.text, end="")
    if chunk.event_type == "citation-generation":
        print(f"\n{chunk.citations}")
```
```
It's 20°C in Toronto.

[ChatCitation(start=5, end=9, text='20°C', document_ids=['get_weather:0:2:0', 'get_weather:0:4:0'])]
```
**v2**
```python PYTHON
if res_v2.message.tool_calls:
    for tc in res_v2.message.tool_calls:
        tool_result = functions_map[tc.function.name](
            **json.loads(tc.function.arguments)
        )
        tool_content_v2 = []
        for data in tool_result:
            tool_content_v2.append(
                {
                    "type": "document",
                    "document": {"data": json.dumps(data)},
                }
            )
            # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tc.id,
                "content": tool_content_v2,
            }
        )

res_v2 = co_v2.chat_stream(
    model="command-a-03-2025", messages=messages, tools=tools_v2
)

for chunk in res_v2:
    if chunk:
        if chunk.type == "content-delta":
            print(chunk.delta.message.content.text, end="")
        elif chunk.type == "citation-start":
            print(f"\n{chunk.delta.message.citations}")
```
```
It's 20°C in Toronto.

start=5 end=9 text='20°C' sources=[ToolSource(type='tool', id='get_weather_k88p0m8504w5:0', tool_output={'temperature': '20C'})]
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
