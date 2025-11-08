---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Naive fixed sized chunking with overlaps

def create_chunks(document, chunk_size=300, overlap=50):
    return [
        document[i : i + chunk_size]
        for i in range(0, len(document), chunk_size - overlap)
    ]


chunks = create_chunks(pg_essay, chunk_size=250, overlap=30)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
