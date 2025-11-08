---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## set the tag filter on our existing query

query.set_filter(tag_filter)

results = index.query(query)

for doc in results:
    print(
        f"Title:{doc['title']}\nText:{doc['text']}\nDistance {doc['vector_distance']}\n"
    )
```
One feature of Redis is the ability to add [filtering](https://www.redisvl.com/api/query.html) to your queries on the fly. Here we are constructing a `tag filter` on the column `title` which was initialized in our schema with `type=tag`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
