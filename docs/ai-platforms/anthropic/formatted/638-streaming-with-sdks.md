---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming with SDKs

Our [Python](https://github.com/anthropics/anthropic-sdk-python) and [TypeScript](https://github.com/anthropics/anthropic-sdk-typescript) SDKs offer multiple ways of streaming. The Python SDK allows both sync and async streams. See the documentation in each SDK for details.
```Python
  import anthropic

  client = anthropic.Anthropic()

  with client.messages.stream(
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello"}],
      model="claude-sonnet-4-5",
  ) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```
```TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const client = new Anthropic();

  await client.messages.stream({
      messages: [{role: 'user', content: "Hello"}],
      model: 'claude-sonnet-4-5',
      max_tokens: 1024,
  }).on('text', (text) => {
      console.log(text);
  });
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
