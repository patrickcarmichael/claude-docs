---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Detecting Low Balance

While it is possible to simply run down the balance until your app starts receiving 402 error codes for insufficient credits, this gap in service while topping up might not be desirable.

To avoid this, you can periodically call the `GET /api/v1/credits` endpoint to check your available credits.
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: '<OPENROUTER_API_KEY>',
  });

  const credits = await openRouter.credits.get();
  console.log('Available credits:', credits.totalCredits - credits.totalUsage);
```
```typescript title="TypeScript (fetch)"
  const response = await fetch('https://openrouter.ai/api/v1/credits', {
    method: 'GET',
    headers: { Authorization: 'Bearer <OPENROUTER_API_KEY>' },
  });
  const { data } = await response.json();
```

The response includes your total credits purchased and usage, where your current balance is the difference between the two:
```json
{
  "data": {
    "total_credits": 50.0,
    "total_usage": 42.0
  }
}
```
Note that these values are cached, and may be up to 60 seconds stale.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
