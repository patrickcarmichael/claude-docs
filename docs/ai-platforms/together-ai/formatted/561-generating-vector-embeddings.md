---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating vector embeddings

Use our [embedding models](/docs/serverless-models#embedding-models) to generate an embedding for some text input:
```python
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.embeddings.create(
      model="togethercomputer/m2-bert-80M-8k-retrieval",
      input="Our solar system orbits the Milky Way galaxy at about 515,000 mph",
  )

  print(response.data[0].embedding)
```
```typescript
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await client.embeddings.create({
    model: 'togethercomputer/m2-bert-80M-32k-retrieval',
    input: 'Our solar system orbits the Milky Way galaxy at about 515,000 mph',
  });

  console.log(response.data[0].embedding);
```

Output
```text
[0.2633975, 0.13856211, 0.14047204,... ]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
