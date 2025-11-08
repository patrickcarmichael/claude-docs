---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a search index

index = hnswlib.Index(space="ip", dim=1536)
index.init_index(
    max_elements=len(doc_embs), ef_construction=512, M=64
)
index.add_items(doc_embs, list(range(len(doc_embs))))
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
