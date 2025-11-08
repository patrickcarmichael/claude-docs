---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Limiting or turning off caching

Additionally, you can pass the `prompt_cache_max_len` field in the request body to
limit the maximum prefix of the prompt (in tokens) that is considered for
caching. It's rarely needed in real applications but can come in handy for
benchmarking the performance of dedicated deployments by passing
`"prompt_cache_max_len": 0`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
