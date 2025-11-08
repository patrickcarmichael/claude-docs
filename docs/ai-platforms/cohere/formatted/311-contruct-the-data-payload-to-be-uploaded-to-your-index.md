---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## contruct the data payload to be uploaded to your index

data = [
    {
        "url": row["url"],
        "title": row["title"],
        "text": row["text"],
        "wiki_id": row["wiki_id"],
        "paragraph_id": row["paragraph_id"],
        "id": row["id"],
        "views": row["views"],
        "langs": row["langs"],
        "embedding": v,
    }
    for row, v in zip(corpus, res)
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
