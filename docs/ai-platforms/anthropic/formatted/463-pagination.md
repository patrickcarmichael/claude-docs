---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pagination

The API supports cursor-based pagination for organizations with large numbers of users:

1. Make your initial request with optional `limit` parameter
2. If `has_more` is `true` in the response, use the `next_page` value in your next request
3. Continue until `has_more` is `false`

The cursor encodes the position of the last record and ensures stable pagination even as new data arrives. Each pagination session maintains a consistent data boundary to ensure you don't miss or duplicate records.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
