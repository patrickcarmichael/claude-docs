---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## General optimization recommendations

Based on our benchmarks, we recommend the following:

1. Use a client library optimized for high concurrency, such as
   [aiohttp](https://docs.aiohttp.org/en/stable/index.html) in Python or
   [http.Agent](https://nodejs.org/api/http.html#class-httpagent) in Node.js.
2. Keep the [`connection pool size`](https://docs.aiohttp.org/en/stable/client_advanced.html#limiting-connection-pool-size) high (1000+).
3. Increase concurrency until performance stops improving or you observe too many `429` errors.
4. Use [direct routing](/deployments/direct-routing) to avoid the global API load balancer and route requests directly to your deployment.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
