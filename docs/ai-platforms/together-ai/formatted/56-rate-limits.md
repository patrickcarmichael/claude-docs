---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rate limits

Batch API rate limits are separate from existing per-model rate limits. The Batch API has specific rate limits:

* **Max Token limits**: A maximum of 30B tokens can be ***enqueued per model***
* **Per-batch limits**: A single batch may include up to 50,000 requests
* **Batch file size**: Maximum 100MB per batch input file
* **Separate pool**: Batch API usage doesn't consume tokens from standard rate limits

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
