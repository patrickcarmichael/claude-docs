---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Ignoring Providers

You can ignore providers for a request by setting the `ignore` field in the `provider` object.

| Field    | Type      | Default | Description                                      |
| -------- | --------- | ------- | ------------------------------------------------ |
| `ignore` | string\[] | -       | List of provider slugs to skip for this request. |

>   **⚠️ Warning**
>
> Ignoring multiple providers may significantly reduce fallback options and
  limit request recovery.

<Tip title="Account-Wide Ignored Providers">
  You can ignore providers for all account requests by configuring your [preferences](/settings/preferences). This configuration applies to all API requests and chatroom messages.

  Note that when you ignore providers for a specific request, the list of ignored providers is merged with your account-wide ignored providers.
</Tip>

### Example: Ignoring DeepInfra for a request calling Llama 3.3 70b

Here's an example that will ignore DeepInfra for a request calling Llama 3.3 70b:
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const completion = await openRouter.chat.send({
    model: 'meta-llama/llama-3.3-70b-instruct',
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      ignore: ['deepinfra'],
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
      model: 'meta-llama/llama-3.3-70b-instruct',
      messages: [{ role: 'user', content: 'Hello' }],
      provider: {
        ignore: ['deepinfra'],
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
    'model': 'meta-llama/llama-3.3-70b-instruct',
    'messages': [{ 'role': 'user', 'content': 'Hello' }],
    'provider': {
      'ignore': ['deepinfra'],
    },
  })
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
