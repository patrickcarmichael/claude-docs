---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic chat completions

Here’s a basic example of using the Chat Completions API.

<Tabs>
  <Tab title="Python">
```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    completion = client.chat.completions.create(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming.",
            },
        ],
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
                role: "user",
                content: "Write a haiku about recursion in programming.",
            },
        ]
    });

    console.log(completion.choices[0].message);
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
            "role": "user", 
            "content": "Write a haiku about recursion in programming."
        }
        ]
    }'
```
  </Tab>
</Tabs>

Example response (via the Python SDK):
```mdx
ChatCompletionMessage(content="Recursive loops,\nUnraveling code's depths,\nEndless, yet complete.", refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
