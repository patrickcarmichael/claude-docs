---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How requests get assigned tiers

When handling a request, Anthropic decides to assign a request to Priority Tier in the following scenarios:

* Your organization has sufficient priority tier capacity **input** tokens per minute
* Your organization has sufficient priority tier capacity **output** tokens per minute

Anthropic counts usage against Priority Tier capacity as follows:

**Input Tokens**

* Cache reads as 0.1 tokens per token read from the cache
* Cache writes as 1.25 tokens per token written to the cache with a 5 minute TTL
* Cache writes as 2.00 tokens per token written to the cache with a 1 hour TTL
* For [long-context](/en/docs/build-with-claude/context-windows) (>200k input tokens) requests, input tokens are 2 tokens per token
* All other input tokens are 1 token per token

**Output Tokens**

* For [long-context](/en/docs/build-with-claude/context-windows) (>200k input tokens) requests, output tokens are 1.5 tokens per token
* All other output tokens are 1 token per token

Otherwise, requests proceed at standard tier.

>   **📝 Note**
>
> Requests assigned Priority Tier pull from both the Priority Tier capacity and the regular rate limits.
  If servicing the request would exceed the rate limits, the request is declined.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
