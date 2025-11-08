---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Split the text into chunks with some overlap

chunks_ = text_splitter.create_documents([doc_content])
documents = [c.page_content for c in chunks_]

print("Source document has been broken down to {} chunks".format(len(documents)))
```
```python PYTHON
"""
Embed document chunks
"""
document_embeddings = co.embed(texts=documents, model="embed-v4.0", input_type="search_document").embeddings
```
```python PYTHON
"""
Create document index and add embedded chunks
"""

import hnswlib

index = hnswlib.Index(space='ip', dim=1536) # space: inner product

index.init_index(max_elements=len(document_embeddings), ef_construction=512, M=64)
index.add_items(document_embeddings, list(range(len(document_embeddings))))
print("Count:", index.element_count)
```
```txt title="Output"
Count: 115
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
