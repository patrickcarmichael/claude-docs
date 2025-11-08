---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running a single query

Use `chat.completions.create` to send a single query to a chat model:
```python
  from together import Together

  client = Together()

  response = client.chat.completions.create(
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
  )

  print(response.choices[0].message.content)
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  const response = await together.chat.completions.create({
    model: "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages: [{ role: "user", content: "What are some fun things to do in New York?" }],
  });

  console.log(response.choices[0].message.content)
```
```shell
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
       		{"role": "user", "content": "What are some fun things to do in New York?"}
       	]
       }'
```

The `create` method takes in a model name and a `messages` array. Each `message` is an object that has the content of the query, as well as a role for the message's author.

In the example above, you can see that we're using "user" for the role. The "user" role tells the model that this message comes from the end user of our system – for example, a customer using your chatbot app.

The other two roles are "assistant" and "system", which we'll talk about next.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
