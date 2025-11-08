---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Combine the lists using RRF

hybrid_top_k = reciprocal_rank_fusion(vector_top_k, bm25_top_k)
hybrid_top_k[1]

hybrid_top_k_docs = [contextual_chunks[index] for index in hybrid_top_k[1]]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
