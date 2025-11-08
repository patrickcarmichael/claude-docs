---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Customizing how the model responds

While you can query a model just by providing a user message, typically you'll want to give your model some context for how you'd like it to respond. For example, if you're building a chatbot to help your customers with travel plans, you might want to tell your model that it should act like a helpful travel guide.

To do this, provide an initial message that uses the "system" role:
```python
  import os
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {"role": "system", "content": "You are a helpful travel guide."},
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          },
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
      {"role": "system", "content": "You are a helpful travel guide."},
      { role: "user", content: "What are some fun things to do in New York?" },
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
       		{"role": "system", "content": "You are a helpful travel guide."},
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	]
       }'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
