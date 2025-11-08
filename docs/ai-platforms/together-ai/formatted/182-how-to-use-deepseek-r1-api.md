---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use DeepSeek-R1 API

Since these models produce longer responses we'll stream in tokens instead of waiting for the whole response to complete.
```python
  from together import Together

  client = Together()  # pass in API key to api_key or set a env variable

  stream = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=[
          {
              "role": "user",
              "content": "Which number is bigger 9.9 or 9.11?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
```
```typescript
  import Together from "together-ai";
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: "deepseek-ai/DeepSeek-R1",
    messages: [{ role: "user", content: "Which number is bigger 9.9 or 9.11?" }],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || "");
  }
```
```bash
  curl -X POST "https://api.together.xyz/v1/chat/completions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
       	"model": "deepseek-ai/DeepSeek-R1",
       	"messages": [
            {"role": "user", "content": "Which number is bigger 9.9 or 9.11?"}
       	]
       }'
```

This will produce an output that contains both the Chain-of-thought tokens and the answer:
```plain
<think>
Okay, the user is asking which number is bigger between 9.9 and 9.11.

Let me think about how to approach this.
...
</think>

**Answer:** 9.9 is bigger.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
