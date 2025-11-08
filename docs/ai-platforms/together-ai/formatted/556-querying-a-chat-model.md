---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Querying a chat model

Now that your OpenAI client is configured to point to Together, you can start using one of our open-source models for your inference queries.

For example, you can query one of our [chat models](/docs/serverless-models#chat-models), like Llama 3.1 8B:
```python
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
          {
              "role": "system",
              "content": "You are a travel agent. Be descriptive and helpful.",
          },
          {
              "role": "user",
              "content": "Tell me the top 3 things to do in San Francisco",
          },
      ],
  )

  print(response.choices[0].message.content)
```
```typescript
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await client.chat.completions.create({
    model: 'openai/gpt-oss-20b',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
  });

  console.log(response.choices[0].message.content);
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
