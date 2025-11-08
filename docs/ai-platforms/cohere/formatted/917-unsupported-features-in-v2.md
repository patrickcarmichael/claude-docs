---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Unsupported features in v2

The following v1 features are not supported in v2:

* General chat
  * `conversation_id` parameter (chat history is now managed by the developer via the `messages` parameter)
* RAG
  * `search_queries_only` parameter
  * `connectors` parameter
  * `prompt_truncation` parameter
* Tool use
  * `force_single_step` parameter (all tool calls are now multi-step by default)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
