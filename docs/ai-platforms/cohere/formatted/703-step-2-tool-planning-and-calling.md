---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Tool planning and calling

response = co.chat(
    model="command-a-03-2025", messages=messages, tools=tools
)

if response.message.tool_calls:
    print("Tool plan:")
    print(response.message.tool_plan, "\n")
    print("Tool calls:")
    for tc in response.message.tool_calls:
        print(
            f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
        )

    # Append tool calling details to the chat history

    messages.append(
        {
            "role": "assistant",
            "tool_calls": response.message.tool_calls,
            "tool_plan": response.message.tool_plan,
        }
    )
```
```
Tool plan:
I will search the user's emails for any messages about getting set up with IT. 

Tool calls:
Tool name: search_emails | Parameters: {"query":"IT setup"}
```
Given three tools to choose from, the model is able to pick the right tool (in this case, `search_emails`) based on what the user is asking for.

Also, notice that the model first generates a plan about what it should do ("I will do ...") before actually generating the tool call(s).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
