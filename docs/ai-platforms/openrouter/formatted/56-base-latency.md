---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Base Latency

Under typical production conditions, OpenRouter adds approximately 15ms of latency to your requests. This minimal overhead is achieved through:

* Edge computing using Cloudflare Workers to stay as close as possible to your application
* Efficient caching of user and API key data at the edge
* Optimized routing logic that minimizes processing time

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
