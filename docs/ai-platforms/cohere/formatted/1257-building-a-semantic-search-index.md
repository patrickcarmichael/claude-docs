---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building a semantic search index

For nearest-neighbor search, we can use the open-source Annoy library. Let's create a semantic search index and feed it all the embeddings.
```python PYTHON
search_index = AnnoyIndex(embeds.shape[1], 'angular')
for i in range(len(embeds)):
    search_index.add_item(i, embeds[i])

search_index.build(10) # 10 trees

search_index.save('askhn.ann')
```
```
True
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
