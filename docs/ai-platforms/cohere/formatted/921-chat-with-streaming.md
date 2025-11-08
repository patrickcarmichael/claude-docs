---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Chat with streaming

To stream the response, set the `stream` parameter to `True`.

<Tabs>
  <Tab title="Python">
```python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    stream = client.chat.completions.create(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming.",
            },
        ],
        stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
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
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
        ],
        "stream": true
    }'
```
  </Tab>
</Tabs>

Example response (via the Python SDK):
```mdx
Recursive call,
Unraveling, line by line,
Solving, then again.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
