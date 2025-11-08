---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Response generation

* Tool execution: Chat history management
  * v1: Append `call` and `outputs` to the chat history
  * v2: Append `tool_call_id` and `tool_content` to `messages` to the chat history

* Tool execution: Tool results
  * v1: Passed as `tool_results` parameter
  * v2: Incorporated into the `messages` list as tool responses

* User message
  * v1: Set as empty (`""`)
  * v2: No action required

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

res_v1 = co_v1.chat(
    model="command-a-03-2025",
    message="",
    tools=tools_v1,
    tool_results=tool_content_v1,
    chat_history=res_v1.chat_history,
)

print(res_v1.text)
```
```
It is currently 20°C in Toronto.
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

res_v2 = co_v2.chat(
    model="command-a-03-2025", messages=messages, tools=tools_v2
)

print(res_v2.message.content[0].text)
```
```
It's 20°C in Toronto.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
