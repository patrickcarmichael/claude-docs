---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Having a long-running conversation

Every query to a chat model is self-contained. This means that new queries won't automatically have access to any queries that may have come before them. This is exactly why the "assistant" role exists.

The "assistant" role is used to provide historical context for how a model has responded to prior queries. This makes it perfect for building apps that have long-running conversations, like chatbots.

To provide a chat history for a new query, pass the previous messages to the `messages` array, denoting the user-provided queries with the "user" role, and the model's responses with the "assistant" role:
```python
  import os
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          },
          {
              "role": "assistant",
              "content": "You could go to the Empire State Building!",
          },
          {"role": "user", "content": "That sounds fun! Where is it?"},
      ],
  )

  print(response.choices[0].message.content)
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [
      { role: "user", content: "What are some fun things to do in New York?" },
      { role: "assistant", content: "You could go to the Empire State Building!"},
      { role: "user", content: "That sounds fun! Where is it?" },
    ],
  });

  console.log(response.choices[0].message.content);
```
```shell
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
          {"role": "user", "content": "What are some fun things to do in New York?"},
          {"role": "assistant", "content": "You could go to the Empire State Building!"},
          {"role": "user", "content": "That sounds fun! Where is it?" }
       	]
       }'
```

How your app stores historical messages is up to you.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
