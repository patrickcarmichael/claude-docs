---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Client-side performance optimization

Source: https://docs.fireworks.ai/deployments/client-side-performance-optimization

Optimize your client code for maximum performance with dedicated deployments

When using a dedicated deployment, it is important to optimize the client-side
HTTP connection pooling for maximum performance. We recommend using our [Python
SDK](/tools-sdks/python-client/sdk-introduction) as it has good defaults for
connection pooling and utilizes
[aiohttp](https://docs.aiohttp.org/en/stable/index.html) for optimal performance
with Python's `asyncio` library. It also includes retry logic for handling `429`
errors that Fireworks returns when the server is overloaded. We have run
benchmarks that demonstrate the performance benefits.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
