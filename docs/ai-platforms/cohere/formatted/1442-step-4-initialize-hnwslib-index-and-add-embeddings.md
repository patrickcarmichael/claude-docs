---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 4: Initialize Hnwslib index and add embeddings

```python PYTHON
index = hnswlib.Index(space='ip', dim=1024)
index.init_index(max_elements=len(embeddings), ef_construction=512, M=64)
index.add_items(embeddings,list(range(len(embeddings))))
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
