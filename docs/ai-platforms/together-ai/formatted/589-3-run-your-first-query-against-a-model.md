---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Run your first query against a model

Choose a model to query. In this example, we'll choose GPT OSS 20B with streaming:
```python
  from together import Together

  client = Together()

  stream = client.chat.completions.create(
      model="openai/gpt-oss-20b",
      messages=[
          {
              "role": "user",
              "content": "What are the top 3 things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
```
```ts
  import Together from "together-ai"

  async function main() {
    const together = new Together()
    const stream = await together.chat.completions.create({
      model: "openai/gpt-oss-20b",
      messages: [
        { role: "user", content: "What are the top 3 things to do in New York?" },
      ],
      stream: true,
    })

    for await (const chunk of stream) {
      process.stdout.write(chunk.choices[0]?.delta?.content || "")
    }
  }

  main()
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
       	"messages": [
            {"role": "user", "content": "What are the top 3 things to do in New York?"}
       	]
       }'
```

Congratulations –you've just made your first query to Together AI!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
