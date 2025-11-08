---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Targeting Specific Provider Endpoints

Each provider on OpenRouter may host multiple endpoints for the same model, such as a default endpoint and a specialized "turbo" endpoint. To target a specific endpoint, you can use the copy button next to the provider name on the model detail page to obtain the exact provider slug.

For example, DeepInfra offers DeepSeek R1 through multiple endpoints:

* Default endpoint with slug `deepinfra`
* Turbo endpoint with slug `deepinfra/turbo`

By copying the exact provider slug and using it in your request's `order` array, you can ensure your request is routed to the specific endpoint you want:
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const completion = await openRouter.chat.send({
    model: 'deepseek/deepseek-r1',
    messages: [{ role: 'user', content: 'Hello' }],
    provider: {
      order: ['deepinfra/turbo'],
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
      model: 'deepseek/deepseek-r1',
      messages: [{ role: 'user', content: 'Hello' }],
      provider: {
        order: ['deepinfra/turbo'],
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
    'model': 'deepseek/deepseek-r1',
    'messages': [{ 'role': 'user', 'content': 'Hello' }],
    'provider': {
      'order': ['deepinfra/turbo'],
      'allow_fallbacks': False,
    },
  })
```

This approach is especially useful when you want to consistently use a specific variant of a model from a particular provider.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
