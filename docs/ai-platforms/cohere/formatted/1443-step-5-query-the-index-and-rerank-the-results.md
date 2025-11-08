---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 5: Query the index and rerank the results

```python PYTHON
query = "What was the first youtube video about?"

query_emb=co.embed(
    texts=[query], model="embed-english-v3.0", input_type="search_query"
        ).embeddings

doc_index = index.knn_query(query_emb, k=10)[0][0]

docs_to_rerank = []
for index in doc_index:
  docs_to_rerank.append(texts[index])

final_result = co.rerank(
    query= query,
    documents=docs_to_rerank,
    model="rerank-english-v2.0",
    top_n=3)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
