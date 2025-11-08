---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Tool execution

for tc in response.message.tool_calls:
    tool_result = functions_map[tc.function.name](
        **json.loads(tc.function.arguments)
    )
    tool_content = []
    for data in tool_result:
        tool_content.append(
            {
                "type": "document",
                "document": {"data": json.dumps(data)},
            }
        )
        # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated

    # Append tool results to the chat history

    messages.append(
        {
            "role": "tool",
            "tool_call_id": tc.id,
            "content": tool_content,
        }
    )

    print("Tool results:")
    for result in tool_content:
        print(result)
```
```
Tool results:
{'type': 'document', 'document': {'data': '{"from": "it@co1t.com", "to": "david@co1t.com", "date": "2024-06-24", "subject": "Setting Up Your IT Needs", "text": "Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts."}'}}
{'type': 'document', 'document': {'data': '{"from": "john@co1t.com", "to": "david@co1t.com", "date": "2024-06-24", "subject": "First Week Check-In", "text": "Hello! I hope you\'re settling in well. Let\'s connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon\\u2014it\'s a great opportunity to get to know your colleagues!"}'}}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
