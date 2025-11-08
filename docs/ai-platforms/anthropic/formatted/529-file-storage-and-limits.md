---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## File storage and limits

### Storage limits

* **Maximum file size:** 500 MB per file
* **Total storage:** 100 GB per organization

### File lifecycle

* Files are scoped to the workspace of the API key. Other API keys can use files created by any other API key associated with the same workspace
* Files persist until you delete them
* Deleted files cannot be recovered
* Files are inaccessible via the API shortly after deletion, but they may persist in active `Messages` API calls and associated tool uses
* Files that users delete will be deleted in accordance with our [data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data).

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
