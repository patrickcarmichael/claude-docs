---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate search queries (if any)

response = co_v2.chat(
    model=model, messages=messages, tools=web_search_tool
)

search_queries = []

while response.message.tool_calls:

    print("Tool plan:")
    print(response.message.tool_plan, "\n")
    print("Tool calls:")
    for tc in response.message.tool_calls:
        print(
            f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
        )
    print("=" * 50)

    messages.append(
        {
            "role": "assistant",
            "tool_calls": response.message.tool_calls,
            "tool_plan": response.message.tool_plan,
        }
    )

    # Step 3: Get tool results

    for idx, tc in enumerate(response.message.tool_calls):
        tool_result = web_search(**json.loads(tc.function.arguments))
        tool_content = []
        for data in tool_result:
            tool_content.append(
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
                "content": tool_content,
            }
        )

    # Step 4: Generate response and citations

    response = co_v2.chat(
        model=model, messages=messages, tools=web_search_tool
    )

print(response.message.content[0].text)
```
```
Tool plan:
I will search for 'who won euro 2024' to find out who won the competition. 

Tool calls:
Tool name: web_search | Parameters: {"queries":["who won euro 2024"]}
==================================================
Spain won the 2024 European Championship. They beat England in the final, with substitute Mikel Oyarzabal scoring the winning goal.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
