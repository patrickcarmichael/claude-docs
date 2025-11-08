---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating a completion

Use `client.completions.create` to create a completion for a code or language models:
```py
  import os
  from together import Together

  client = Together()

  response = client.completions.create(
      model="meta-llama/Llama-2-70b-hf",
      prompt="def fibonacci(n): ",
      stream=True,
  )

  for chunk in response:
      print(chunk.choices[0].text or "", end="", flush=True)
```
```typescript
  import Together from 'together-ai';

  const together = new Together();

  const response = await together.completions.create({
    model: "meta-llama/Llama-2-70b-hf",
    prompt: 'def bubbleSort(): ',
    stream: true
  });

  for chunk in response:
      console.log(chunk.choices[0].text)
```


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
