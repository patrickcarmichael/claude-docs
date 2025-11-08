---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## documents that should be included in the final RAG step

for query in queries:
    ret_nodes = retrieve(query)
    documents.extend(format_for_cohere_client(ret_nodes))

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
