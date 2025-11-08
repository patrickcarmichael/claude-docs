---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Zero data retention

Fireworks has Zero Data Retention by default. Specifically, this means

* Fireworks does not log or store prompt or generation data for any open models, without explicit user opt-in.
  * More technically: prompt and generation data exist only in volatile memory for the duration of the request. If [prompt caching](https://docs.fireworks.ai/guides/prompt-caching#data-privacy) is active, some prompt data (and associated KV caches) can be stored in volatile memory for several minutes. In either case, prompt and generation data are not logged into any persistent storage.
* Fireworks logs metadata (e.g. number of tokens in a request) as required to deliver the service.
* Users can explicitly opt-in to log prompt and generation data for certain advanced features (e.g. FireOptimizer).
* For proprietary Fireworks models (e.g. f1, FireFunction), prompt and generation data may be logged to enable bulk analytics to improve the model.
  * In this case, the model description will contain an explicit message about logging.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
