---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data privacy

Serverless deployments maintain separate caches for each Fireworks account to prevent data leakage and timing attacks.

Dedicated deployments by default share a single cache across all requests.
Because prompt caching doesn't change the outputs, privacy is preserved even
if the deployment powers a multi-tenant application. It does open a minor risk
of a timing attack: potentially, an adversary can learn that a particular prompt
is cached by observing the response time. To ensure full isolation, you can pass
the `x-prompt-cache-isolation-key` header or the `prompt_cache_isolation_key`
field in the body of the request. It can contain an arbitrary string that acts
as an additional cache key, i.e., no sharing will occur between requests with
different IDs.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
