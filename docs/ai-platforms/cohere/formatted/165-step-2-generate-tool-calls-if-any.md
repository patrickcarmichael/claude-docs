---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Generate tool calls (if any)

model = "command-a-03-2025"
response = co.chat(
    model=model, messages=messages, tools=tools, temperature=0.3
)

while response.message.tool_calls:
    print("TOOL PLAN:")
    print(response.message.tool_plan, "\n")
    print("TOOL CALLS:")
    for tc in response.message.tool_calls:
        print(
            f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
        )
    print("=" * 50)

    messages.append(
        {
            "role": "assistant",
            "tool_plan": response.message.tool_plan,
            "tool_calls": response.message.tool_calls,
        }
    )

    # Step 3: Get tool results

    print("TOOL RESULT:")
    for tc in response.message.tool_calls:
        tool_result = functions_map[tc.function.name](
            **json.loads(tc.function.arguments)
        )
        tool_content = []
        print(tool_result)
        for data in tool_result:
            # Optional: the "document" object can take an "id" field for use in citations, otherwise auto-generated

            tool_content.append(
                {
                    "type": "document",
                    "document": {"data": json.dumps(data)},
                }
            )
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tc.id,
                "content": tool_content,
            }
        )

    # Step 4: Generate response and citations

    response = co.chat(
        model=model,
        messages=messages,
        tools=tools,
        temperature=0.1,
    )

messages.append(
    {
        "role": "assistant",
        "content": response.message.content[0].text,
    }
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
