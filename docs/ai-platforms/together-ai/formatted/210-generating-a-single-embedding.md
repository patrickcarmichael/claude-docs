---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating a single embedding

Use `client.embeddings.create` to generate an embedding for some input text, passing in a model name and input string:
```py
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="BAAI/bge-base-en-v1.5",
      input="Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  )
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  const response = await client.embeddings.create({
    model: "BAAI/bge-base-en-v1.5",
    input: "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  });
```
```bash
  curl -X POST https://api.together.xyz/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "input": "Our solar system orbits the Milky Way galaxy at about 515,000 mph.",
           "model": "BAAI/bge-base-en-v1.5"
          }'
```

The response will be an object that contains the embedding under the `data` key, as well as some metadata:
```json
{
  model: 'BAAI/bge-base-en-v1.5',
  object: 'list',
  data: [
    {
      index: 0,
      object: 'embedding',
      embedding: [0.2633975, 0.13856208, ..., 0.04331574],
    },
  ],
};
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
