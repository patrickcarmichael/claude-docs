---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use DeepSeek V3.1

Get started with this model in 10 lines of code! The model ID is `deepseek-ai/DeepSeek-V3.1` and the pricing is \$0.60 for input tokens and \$1.70 for output tokens.
```python
  from together import Together

  client = Together()
  resp = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-V3.1",
  messages=[{"role":"user","content":"What are some fun things to do in New York?"}],
  stream=True,
  )
  for tok in resp:
  print(tok.choices[0].delta.content, end="", flush=True)
```
```typescript
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'deepseek-ai/DeepSeek-V3.1',
    messages: [{ role: 'user', content: 'What are some fun things to do in New York?' }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
```

>   **⚠️ Warning**
>
>   **Current Limitations**. The following features are not yet supported, but
  will be added soon: Function calling and JSON mode.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
