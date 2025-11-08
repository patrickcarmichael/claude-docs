---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Request size limits

The API enforces request size limits to ensure optimal performance:

| Endpoint Type                                            | Maximum Request Size |
| :------------------------------------------------------- | :------------------- |
| Messages API                                             | 32 MB                |
| Token Counting API                                       | 32 MB                |
| [Batch API](/en/docs/build-with-claude/batch-processing) | 256 MB               |
| [Files API](/en/docs/build-with-claude/files)            | 500 MB               |

If you exceed these limits, you'll receive a 413 `request_too_large` error. The error is returned from Cloudflare before the request reaches our API servers.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
