---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hybrid search

After the dataset has been enriched with the embeddings, you can query the data using hybrid search.

Pass a `query_vector_builder` to the k-nearest neighbor (kNN) vector search API, and provide the query text and the model you have used to create the embeddings.
```python PYTHON
query = "When were the semi-finals of the 2022 FIFA world cup played?"

response = client.search(
    index="cohere-wiki-embeddings",
    size=100,
    knn={
        "field": "text_embedding",
        "query_vector_builder": {
            "text_embedding": {
                "model_id": "cohere_embeddings",
                "model_text": query,
            }
        },
        "k": 10,
        "num_candidates": 50,
    },
    query={
      "multi_match": {
          "query": query,
          "fields": ["text", "title"]
        }
      }
)

raw_documents = response["hits"]["hits"]

for document in raw_documents[0:10]:
  print(f'Title: {document["_source"]["title"]}\nText: {document["_source"]["text"]}\n')

documents = []
for hit in response["hits"]["hits"]:
    documents.append(hit["_source"]["text"])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
