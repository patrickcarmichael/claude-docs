---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prompt caching

Source: https://docs.fireworks.ai/guides/prompt-caching


Prompt caching is a performance optimization feature that allows Fireworks to
respond faster to requests with prompts that share common prefixes. In many
situations, it can reduce time to first token (TTFT) by as much as 80%.

Prompt caching is enabled by default for all Fireworks models and deployments.

For dedicated deployments, prompt caching frees up resources, leading to higher
throughput on the same hardware. Dedicated deployments on the Enterprise plan allow
additional configuration options to further optimize cache performance.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
