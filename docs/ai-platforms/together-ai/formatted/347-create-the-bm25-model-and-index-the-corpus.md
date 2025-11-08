---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the BM25 model and index the corpus

retriever = bm25s.BM25(corpus=contextual_chunks)
retriever.index(bm25s.tokenize(contextual_chunks))
```

Which can be queried as follows:
```py

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
