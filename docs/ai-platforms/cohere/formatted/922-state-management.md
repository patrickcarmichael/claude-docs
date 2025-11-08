---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## State management

For state management, use the `messages` parameter to build the conversation history.

You can include a system message via the `developer` role and the multiple chat turns between the `user` and `assistant`.

<Tabs>
  <Tab title="Python">
```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "developer",
                "content": "You must respond in the style of a pirate.",
            },
            {
                "role": "user",
                "content": "What's 2 + 2.",
            },
            {
                "role": "assistant",
                "content": "Arrr, matey! 2 + 2 be 4, just like a doubloon in the sea!",
            },
            {
                "role": "user",
                "content": "Add 30 to that.",
            },
        ],
        model="command-a-03-2025",
    )

    print(completion.choices[0].message)
```
  </Tab>

  <Tab title="TypeScript">
```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const completion = await openai.chat.completions.create({
        model: "command-a-03-2025",
        messages: [
            {
                role: "developer", 
                content: "You must respond in the style of a pirate."
            },
            {
                role: "user",
                content: "What's 2 + 2.",
            },
            {
                role: "assistant",
                content: "Arrr, matey! 2 + 2 be 4, just like a doubloon in the sea!",
            },
            {
                role: "user",
                content: "Add 30 to that.",
            }
        ],
        stream: true,
    });

    for await (const chunk of completion) {
        console.log(chunk.choices[0].delta.content);
    }
```
  </Tab>

  <Tab title="cURL">
```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/chat/completions \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "command-a-03-2025",
        "messages": [
        {
            "role": "developer",
            "content": "You must respond in the style of a pirate."
        },
        {
            "role": "user",
            "content": "What'\''s 2 + 2."
        },
        {
            "role": "assistant", 
            "content": "Arrr, matey! 2 + 2 be 4, just like a doubloon in the sea!"
        },
        {
            "role": "user",
            "content": "Add 30 to that."
        }
        ]
    }'
```
  </Tab>
</Tabs>

Example response (via the Python SDK):
```mdx
ChatCompletionMessage(content='Aye aye, captain! 4 + 30 be 34, a treasure to behold!', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
