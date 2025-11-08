---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Allowing Only Specific Providers

You can allow only specific providers for a request by setting the `only` field in the `provider` object.

| Field  | Type      | Default | Description                                       |
| ------ | --------- | ------- | ------------------------------------------------- |
| `only` | string\[] | -       | List of provider slugs to allow for this request. |

>   **⚠️ Warning**
>
> Only allowing some providers may significantly reduce fallback options and
  limit request recovery.

<Tip title="Account-Wide Allowed Providers">
  You can allow providers for all account requests by configuring your [preferences](/settings/preferences). This configuration applies to all API requests and chatroom messages.

  Note that when you allow providers for a specific request, the list of allowed providers is merged with your account-wide allowed providers.
</Tip>

### Example: Allowing Azure for a request calling GPT-4 Omni

Here's an example that will only use Azure for a request calling GPT-4 Omni:
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const completion = await openRouter.chat.send({
    model: 'openai/gpt-4o',
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      only: ['azure'],
    },
    stream: false,
  });
```
```typescript title="TypeScript (fetch)"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer <OPENROUTER_API_KEY>',
      'HTTP-Referer': '<YOUR_SITE_URL>',
      'X-Title': '<YOUR_SITE_NAME>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [{ role: 'user', content: 'Hello' }],
      provider: {
        only: ['azure'],
      },
    }),
  });
```
```python title="Python"
  import requests

  headers = {
    'Authorization': 'Bearer <OPENROUTER_API_KEY>',
    'HTTP-Referer': '<YOUR_SITE_URL>',
    'X-Title': '<YOUR_SITE_NAME>',
    'Content-Type': 'application/json',
  }

  response = requests.post('https://openrouter.ai/api/v1/chat/completions', headers=headers, json={
    'model': 'openai/gpt-4o',
    'messages': [{ 'role': 'user', 'content': 'Hello' }],
    'provider': {
      'only': ['azure'],
    },
  })
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
