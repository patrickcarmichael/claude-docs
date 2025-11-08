---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating multiple embeddings

You can also pass an array of input strings to the `input` option:
```py
  from together import Together

  client = Together()

  response = client.embeddings.create(
      model="BAAI/bge-base-en-v1.5",
      input=[
          "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
          "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
      ],
  )
```
```typescript
  import Together from "together-ai";

  const client = new Together();

  const response = await client.embeddings.create({
    model: "BAAI/bge-base-en-v1.5",
    input: [
      "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
      "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years.",
    ],
  });
```
```bash
  curl -X POST https://api.together.xyz/v1/embeddings \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
           "model": "BAAI/bge-base-en-v1.5",
           "input": [
              "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
              "Jupiter'\''s Great Red Spot is a storm that has been raging for at least 350 years."
           ]
          }'
```

The `response.data` key will contain an array of objects for each input string you provide:
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
    {
      index: 1,
      object: 'embedding',
      embedding: [-0.14496337, 0.21044481, ..., -0.16187587]
    },
  ],
};
```


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
