---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to use Kimi K2

Get started with this model in 10 lines of code! The model ID is `moonshotai/Kimi-K2-Instruct-0905` and the pricing is \$1.00 per 1M input tokens and \$3.00 per 1M output tokens.
```python
  from together import Together

  client = Together()
  resp = client.chat.completions.create(
      model="moonshotai/Kimi-K2-Instruct-0905",
      messages=[{"role": "user", "content": "Code a hacker news clone"}],
      stream=True,
  )
  for tok in resp:
      print(tok.choices[0].delta.content, end="", flush=True)
```
```typescript
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [{ role: 'user', content: 'Code a hackernews clone' }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
