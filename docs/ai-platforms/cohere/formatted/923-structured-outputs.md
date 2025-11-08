---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Structured outputs

The Structured Outputs feature allows you to specify the schema of the model response. It guarantees that the response will strictly follow the schema.

To use it, set the `response_format` parameter to the JSON Schema of the desired output.

<Tabs>
  <Tab title="Python">
```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    completion = client.beta.chat.completions.parse(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": "Generate a JSON describing a book.",
            }
        ],
        response_format={
            "type": "json_object",
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "author": {"type": "string"},
                    "publication_year": {"type": "integer"},
                },
                "required": ["title", "author", "publication_year"],
            },
        },
    )

    print(completion.choices[0].message.content)
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
                content: "Generate a JSON describing a book.",
            }
        ],
        response_format: {
            type: "json_object",
            schema: {
                type: "object",
                properties: {
                    title: {type: "string"},
                    author: {type: "string"},
                    publication_year: {type: "integer"},
                },
                required: ["title", "author", "publication_year"],
            },
        }
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
            "content": "Generate a JSON describing a book."
        }
        ],
        "response_format": {
        "type": "json_object",
        "schema": {
            "type": "object",
            "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "publication_year": {"type": "integer"}
            },
            "required": ["title", "author", "publication_year"]
        }
        }
    }'
```
  </Tab>
</Tabs>

Example response (via the Python SDK):
```
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publication_year": 1925
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
