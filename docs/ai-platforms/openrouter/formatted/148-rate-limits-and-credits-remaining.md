---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rate Limits and Credits Remaining

To check the rate limit or credits left on an API key, make a GET request to `https://openrouter.ai/api/v1/key`.

<Template data={{ API_KEY_REF }}>
```typescript title="TypeScript SDK"
    import { OpenRouter } from '@openrouter/sdk';

    const openRouter = new OpenRouter({
      apiKey: '{{API_KEY_REF}}',
    });

    const keyInfo = await openRouter.apiKeys.getCurrent();
    console.log(keyInfo);
```
```python title="Python"
    import requests
    import json

    response = requests.get(
      url="https://openrouter.ai/api/v1/key",
      headers={
        "Authorization": f"Bearer {{API_KEY_REF}}"
      }
    )

    print(json.dumps(response.json(), indent=2))
```
```typescript title="TypeScript (Raw API)"
    const response = await fetch('https://openrouter.ai/api/v1/key', {
      method: 'GET',
      headers: {
        Authorization: 'Bearer {{API_KEY_REF}}',
      },
    });

    const keyInfo = await response.json();
    console.log(keyInfo);
```
</Template>

If you submit a valid API key, you should get a response of the form:
```typescript title="TypeScript"
type Key = {
  data: {
    label: string;
    limit: number | null; // Credit limit for the key, or null if unlimited
    limit_reset: string | null; // Type of limit reset for the key, or null if never resets
    limit_remaining: number | null; // Remaining credits for the key, or null if unlimited
    include_byok_in_limit: boolean;  // Whether to include external BYOK usage in the credit limit

    usage: number; // Number of credits used (all time)
    usage_daily: number; // Number of credits used (current UTC day)
    usage_weekly: number; // ... (current UTC week, starting Monday)
    usage_monthly: number; // ... (current UTC month)

    byok_usage: number; // Same for external BYOK usage
    byok_usage_daily: number;
    byok_usage_weekly: number;
    byok_usage_monthly: number;

    is_free_tier: boolean; // Whether the user has paid for credits before
    // rate_limit: { ... } // A deprecated object in the response, safe to ignore
  };
};
```
There are a few rate limits that apply to certain types of requests, regardless of account status:

1. Free usage limits: If you're using a free model variant (with an ID ending in <code>{sep}{Variant.Free}</code>), you can make up to {FREE_MODEL_RATE_LIMIT_RPM} requests per minute. The following per-day limits apply:

* If you have purchased less than {FREE_MODEL_CREDITS_THRESHOLD} credits, you're limited to {FREE_MODEL_NO_CREDITS_RPD} <code>{sep}{Variant.Free}</code> model requests per day.

* If you purchase at least {FREE_MODEL_CREDITS_THRESHOLD} credits, your daily limit is increased to {FREE_MODEL_HAS_CREDITS_RPD} <code>{sep}{Variant.Free}</code> model requests per day.

2. **DDoS protection**: Cloudflare's DDoS protection will block requests that dramatically exceed reasonable usage.

If your account has a negative credit balance, you may see <code>{HTTPStatus.S402_Payment_Required}</code> errors, including for free models. Adding credits to put your balance above zero allows you to use those models again.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
