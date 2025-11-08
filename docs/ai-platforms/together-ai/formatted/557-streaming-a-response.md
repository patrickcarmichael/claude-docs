---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming a response

You can also use OpenAI's streaming capabilities to stream back your response:
```python
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  stream = client.chat.completions.create(
      model="Qwen/Qwen3-Next-80B-A3B-Instruct",
      messages=[
          {
              "role": "system",
              "content": "You are a travel agent. Be descriptive and helpful.",
          },
          {"role": "user", "content": "Tell me about San Francisco"},
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
```
```typescript
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  async function run() {
    const stream = await client.chat.completions.create({
      model: 'Qwen/Qwen3-Next-80B-A3B-Instruct',
      messages: [
        { role: 'system', content: 'You are an AI assistant' },
        { role: 'user', content: 'Who won the world series in 2020?' },
      ],
      stream: true,
    });

    for await (const chunk of stream) {
      // use process.stdout.write instead of console.log to avoid newlines
      process.stdout.write(chunk.choices[0]?.delta?.content || '');
    }
  }

  run();
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
