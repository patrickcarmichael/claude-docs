---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Ordering Specific Providers

You can set the providers that OpenRouter will prioritize for your request using the `order` field.

| Field   | Type      | Default | Description                                                              |
| ------- | --------- | ------- | ------------------------------------------------------------------------ |
| `order` | string\[] | -       | List of provider slugs to try in order (e.g. `["anthropic", "openai"]`). |

The router will prioritize providers in this list, and in this order, for the model you're using. If you don't set this field, the router will [load balance](#price-based-load-balancing-default-strategy) across the top providers to maximize uptime.

<Tip>
  You can use the copy button next to provider names on model pages to get the exact provider slug,
  including any variants like "/turbo". See [Targeting Specific Provider Endpoints](#targeting-specific-provider-endpoints) for details.
</Tip>

OpenRouter will try them one at a time and proceed to other providers if none are operational. If you don't want to allow any other providers, you should [disable fallbacks](#disabling-fallbacks) as well.

### Example: Specifying providers with fallbacks

This example skips over OpenAI (which doesn't host Mixtral), tries Together, and then falls back to the normal list of providers on OpenRouter:
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const completion = await openRouter.chat.send({
    model: 'mistralai/mixtral-8x7b-instruct',
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      order: ['openai', 'together'],
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
      model: 'mistralai/mixtral-8x7b-instruct',
      messages: [{ role: 'user', content: 'Hello' }],
      provider: {
        order: ['openai', 'together'],
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
    'model': 'mistralai/mixtral-8x7b-instruct',
    'messages': [{ 'role': 'user', 'content': 'Hello' }],
    'provider': {
      'order': ['openai', 'together'],
    },
  })
```

### Example: Specifying providers with fallbacks disabled

Here's an example with `allow_fallbacks` set to `false` that skips over OpenAI (which doesn't host Mixtral), tries Together, and then fails if Together fails:
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const completion = await openRouter.chat.send({
    model: 'mistralai/mixtral-8x7b-instruct',
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      order: ['openai', 'together'],
      allowFallbacks: false,
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
      model: 'mistralai/mixtral-8x7b-instruct',
      messages: [{ role: 'user', content: 'Hello' }],
      provider: {
        order: ['openai', 'together'],
        allow_fallbacks: false,
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
    'model': 'mistralai/mixtral-8x7b-instruct',
    'messages': [{ 'role': 'user', 'content': 'Hello' }],
    'provider': {
      'order': ['openai', 'together'],
      'allow_fallbacks': False,
    },
  })
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
