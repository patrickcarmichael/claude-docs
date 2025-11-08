---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using the Exacto Variant

Add `:exacto` to the end of any supported model slug. The curated allowlist is enforced before provider sorting, fallback, or load balancing — no extra provider preference config is required.
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: process.env.OPENROUTER_API_KEY,
  });

  const completion = await openRouter.chat.send({
    model: "moonshotai/kimi-k2-0905:exacto",
    messages: [
      {
        role: "user",
        content: "Draft a concise changelog entry for the Exacto launch.",
      },
    ],
    stream: false,
  });

  console.log(completion.choices[0].message.content);
```
```typescript title="TypeScript (OpenAI SDK)"
  import OpenAI from "openai";

  const client = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    apiKey: process.env.OPENROUTER_API_KEY,
  });

  const completion = await client.chat.completions.create({
    model: "moonshotai/kimi-k2-0905:exacto",
    messages: [
      {
        role: "user",
        content: "Draft a concise changelog entry for the Exacto launch.",
      },
    ],
  });
```
```shell title="cURL"
  curl https://openrouter.ai/api/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -d '{
    "model": "moonshotai/kimi-k2-0905:exacto",
    "messages": [
      {
        "role": "user",
        "content": "Summarize the latest release notes for me."
      }
    ]
  }'
```

<Tip>
  You can still supply fallback models with the `models` array. Any model that
  carries the `:exacto` suffix will enforce the curated provider list when it is
  selected.
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
