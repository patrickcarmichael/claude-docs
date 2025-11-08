---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1-hour cache duration

If you find that 5 minutes is too short, Anthropic also offers a 1-hour cache duration [at additional cost](#pricing).

To use the extended cache, include `ttl` in the `cache_control` definition like this:
```JSON
"cache_control": {
    "type": "ephemeral",
    "ttl": "5m" | "1h"
}
```
The response will include detailed cache information like the following:
```JSON
{
    "usage": {
        "input_tokens": ...,
        "cache_read_input_tokens": ...,
        "cache_creation_input_tokens": ...,
        "output_tokens": ...,

        "cache_creation": {
            "ephemeral_5m_input_tokens": 456,
            "ephemeral_1h_input_tokens": 100,
        }
    }
}
```
Note that the current `cache_creation_input_tokens` field equals the sum of the values in the `cache_creation` object.

### When to use the 1-hour cache

If you have prompts that are used at a regular cadence (i.e., system prompts that are used more frequently than every 5 minutes), continue to use the 5-minute cache, since this will continue to be refreshed at no additional charge.

The 1-hour cache is best used in the following scenarios:

* When you have prompts that are likely used less frequently than 5 minutes, but more frequently than every hour. For example, when an agentic side-agent will take longer than 5 minutes, or when storing a long chat conversation with a user and you generally expect that user may not respond in the next 5 minutes.
* When latency is important and your follow up prompts may be sent beyond 5 minutes.
* When you want to improve your rate limit utilization, since cache hits are not deducted against your rate limit.

>   **📝 Note**
>
> The 5-minute and 1-hour cache behave the same with respect to latency. You will generally see improved time-to-first-token for long documents.

### Mixing different TTLs

You can use both 1-hour and 5-minute cache controls in the same request, but with an important constraint: Cache entries with longer TTL must appear before shorter TTLs (i.e., a 1-hour cache entry must appear before any 5-minute cache entries).

When mixing TTLs, we determine three billing locations in your prompt:

1. Position `A`: The token count at the highest cache hit (or 0 if no hits).
2. Position `B`: The token count at the highest 1-hour `cache_control` block after `A` (or equals `A` if none exist).
3. Position `C`: The token count at the last `cache_control` block.

>   **📝 Note**
>
> If `B` and/or `C` are larger than `A`, they will necessarily be cache misses, because `A` is the highest cache hit.

You'll be charged for:

1. Cache read tokens for `A`.
2. 1-hour cache write tokens for `(B - A)`.
3. 5-minute cache write tokens for `(C - B)`.

Here are 3 examples. This depicts the input tokens of 3 requests, each of which has different cache hits and cache misses. Each has a different calculated pricing, shown in the colored boxes, as a result.
<img src="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt-cache-mixed-ttl.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=10a8997695f0f78953fdac300a3373e9" alt="Mixing TTLs Diagram" data-og-width="1376" width="1376" data-og-height="976" height="976" data-path="images/prompt-cache-mixed-ttl.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt-cache-mixed-ttl.svg?w=280&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=7a8de34e52bbf67c60b2eeda57690ea3 280w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt-cache-mixed-ttl.svg?w=560&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=cdc3a1950dc88fbfb5679320df656ef2 560w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt-cache-mixed-ttl.svg?w=840&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=0df34408f5ec905ade69060ac8b5077b 840w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt-cache-mixed-ttl.svg?w=1100&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=0c434f1b04d12e6a0a20cfe58b22d4e5 1100w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt-cache-mixed-ttl.svg?w=1650&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=c800577f55f6e3383e3807644a5e0743 1650w, https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/prompt-cache-mixed-ttl.svg?w=2500&fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=7e7079d06a969ea814980f4e570d2fa2 2500w" />

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
