---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Store the embeddings in a vector database

ids = []
for i in range(0, len(input_array)):
    ids.append(str(i))

chroma_client = chromadb.Client()
collection = chroma_client.create_collection("pdf_pages")
collection.add(
    embeddings=embeddings,
    ids=ids,
)
```
Finally, provide a query and run a search over the documents. This will return a list of sorted IDs representing the most similar pages to the query.
```python PYTHON
query = "Do the speakers come with an optical cable?"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
