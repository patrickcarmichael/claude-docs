---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embeddings

You can generate text embeddings Embeddings API by passing a list of strings as the `input` parameter. You can also specify in `encoding_format` the format of embeddings to be generated. Can be either `float` or `base64`.

<Tabs>
  <Tab title="Python">
```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key=COHERE_API_KEY,
    )

    response = client.embeddings.create(
        input=["Hello world!"],
        model="embed-v4.0",
        encoding_format="float",
    )

    print(
        response.data[0].embedding[:5]
    )  # Display the first 5 dimensions

```
  </Tab>

  <Tab title="TypeScript">
```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const response = await openai.embeddings.create({
        input: ["Hello world!"],
        model: "embed-v4.0",
        encoding_format: "float"
    });

    console.log(response.data[0].embedding.slice(0, 5)); // Display the first 5 dimensions
```
  </Tab>

  <Tab title="cURL">
```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/embeddings \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "embed-v4.0",
        "input": ["Hello world!"],
        "encoding_format": "float"
    }'
```
  </Tab>
</Tabs>

Example response (via the Python SDK):
```mdx
[0.0045051575, 0.046905518, 0.025543213, 0.009651184, -0.024993896]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
