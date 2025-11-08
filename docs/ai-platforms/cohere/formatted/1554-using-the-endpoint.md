---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using the Endpoint

In the following cell we will call rerank to rank `docs` based on how relevant they are with `query`.
```python PYTHON
results = co.rerank(query=query, model=MODEL_NAME, documents=docs, top_n=3) # Change top_n to change the number of results returned. If top_n is not passed, all results will be returned.

for idx, r in enumerate(results):
  print(f"Document Rank: {idx + 1}, Document Index: {r.index}")
  print(f"Document: {r.document['text']}")
  print(f"Relevance Score: {r.relevance_score:.2f}")
  print("\n")
```
```txt title="Output"
Document Rank: 1, Document Index: 3
Document: Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district. The President of the USA and many major national government offices are in the territory. This makes it the political center of the United States of America.
Relevance Score: 1.00


Document Rank: 2, Document Index: 5
Document: Capital punishment has existed in the United States since before the United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states. The federal government (including the United States military) also uses capital punishment.
Relevance Score: 0.75


Document Rank: 3, Document Index: 1
Document: The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean that are a political division controlled by the United States. Its capital is Saipan.
Relevance Score: 0.09
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
