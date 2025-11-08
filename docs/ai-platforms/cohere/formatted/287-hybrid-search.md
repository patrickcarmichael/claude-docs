---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hybrid Search

After the dataset has been enriched with the embeddings, you can query the data using hybrid search.

Pass a semantic query, and provide the query text and the model you have used to create the embeddings.
```python PYTHON 
query = "When were the semi-finals of the 2022 FIFA world cup played?"

response = client.search(
    index="cohere-wiki-embeddings",
    size=100,
    query={
        "bool": {
            "must": {
                "multi_match": {
                "query": "When were the semi-finals of the 2022 FIFA world cup played?",
                "fields": ["text", "title"]
        }
            },
            "should": {
                "semantic": {
                    "query": "When were the semi-finals of the 2022 FIFA world cup played?",
                     "field": "text_semantic"
                }
            },
        }
    }

)

raw_documents = response["hits"]["hits"]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
