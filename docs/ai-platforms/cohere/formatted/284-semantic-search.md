---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Semantic Search

After the dataset has been enriched with the embeddings, you can query the data using the semantic query provided by Elasticsearch. `semantic_text` in Elasticsearch simplifies the semantic search significantly. Learn more about how [semantic text](https://www.google.com/url?q=https%3A%2F%2Fwww.elastic.co%2Fsearch-labs%2Fblog%2Fsemantic-search-simplified-semantic-text) in Elasticsearch allows you to focus on your model and results instead of on the technical details.
```python PYTHON 
query = "When were the semi-finals of the 2022 FIFA world cup played?"

response = client.search(
    index="cohere-wiki-embeddings",
    size=100,
    query = {
        "semantic": {
                    "query": "When were the semi-finals of the 2022 FIFA world cup played?",
                     "field": "text_semantic"
        }
    }
)

raw_documents = response["hits"]["hits"]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
