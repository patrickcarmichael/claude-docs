---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a new collection named "Legal_Docs" in the Weaviate database

client.collections.create(
    name="Legal_Docs_RAG",
    properties=[
        # Define a property named "title" with data type TEXT

        Property(name="title", data_type=DataType.TEXT),
    ],
    # Configure the vectorizer to use Cohere's text2vec model

    vectorizer_config=Configure.Vectorizer.text2vec_cohere(
        model="embed-english-v3.0"  # Specify the Cohere model to use for vectorization

    ),
    # Configure the reranker to use Cohere's rerank model

    reranker_config=Configure.Reranker.cohere(
        model="rerank-english-v3.0"  # Specify the Cohere model to use for reranking

    ),
    # Configure the generative model to use Cohere's command r plus model

    generative_config=Configure.Generative.cohere(
        model="command-r-plus"
    ),
)
```
You should see something like that:
```
<weaviate.collections.collection.sync.Collection at 0x7f48afc06410>
```
This retrieves `"Legal_Docs_RAG"` from Weaviate:
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
