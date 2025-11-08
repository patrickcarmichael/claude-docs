---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hybrid Thinking

Here's how to enable thinking in DeepSeek V3.1.
```python
  from together import Together
  client = Together()

  stream = client.chat.completions.create(
  model="deepseek-ai/DeepSeek-V3.1",
  messages=[
  {"role": "user", "content": "What are some fun things to do in New York?"}
  ],
  reasoning={"enabled": True},
  stream=True,
  )

  for chunk in stream:
  delta = chunk.choices[0].delta

    # Show reasoning tokens if present

    if hasattr(delta, "reasoning") and delta.reasoning:
        print(delta.reasoning, end="", flush=True)

    # Show content tokens if present

    if hasattr(delta, "content") and delta.content:
        print(delta.content, end="", flush=True)
```
```typescript
  import Together from 'together-ai';

  import type { ChatCompletionChunk } from "together-ai/resources/chat/completions";

  const together = new Together();

  async function main() {
    const stream = await together.chat.completions.stream({
      model: "deepseek-ai/DeepSeek-V3.1",
      messages: [
        { role: "user", content: "What are some fun things to do in New York?" },
      ],
      reasoning: {
        enabled: true,
      },
    } as any);

    for await (const chunk of stream) {
      const delta = chunk.choices[0]
            ?.delta as ChatCompletionChunk.Choice.Delta & { reasoning?: string };

      // Show reasoning tokens if present
      if (delta?.reasoning) process.stdout.write(delta.reasoning);

      // Show content tokens if present
      if (delta?.content) process.stdout.write(delta.content);
    }
  }

  main();
```

>   **⚠️ Warning**
>
> For TypeScript users, you need to cast the parameters as `any` because `reasoning.enabled: true` is not yet recognized by the SDK. Additionally, the delta object requires a custom type to include the `reasoning` property.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
