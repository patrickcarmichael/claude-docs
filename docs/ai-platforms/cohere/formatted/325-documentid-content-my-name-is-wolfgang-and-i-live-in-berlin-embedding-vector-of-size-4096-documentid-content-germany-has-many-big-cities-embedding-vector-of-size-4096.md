---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## [Document(id=..., content: 'My name is Wolfgang and I live in Berlin', embedding: vector of size 4096), Document(id=..., content: 'Germany has many big cities', embedding: vector of size 4096)]

```

#### Retrieving Documents with Haystack and Cohere Embeddings

After the indexing pipeline has added the embeddings to the document store, you can build a retrieval pipeline that gets the most relevant documents from your database. This can also form the basis of RAG pipelines, where a generator component can be added at the end.
```python PYTHON
from haystack import Pipeline
from haystack.components.retrievers.in_memory import (
    InMemoryEmbeddingRetriever,
)
from haystack_integrations.components.embedders.cohere import (
    CohereTextEmbedder,
)

query_pipeline = Pipeline()
query_pipeline.add_component(
    "text_embedder", CohereTextEmbedder(token)
)
query_pipeline.add_component(
    "retriever",
    InMemoryEmbeddingRetriever(document_store=document_store),
)
query_pipeline.connect(
    "text_embedder.embedding", "retriever.query_embedding"
)

query = "Who lives in Berlin?"

result = query_pipeline.run({"text_embedder": {"text": query}})

print(result["retriever"]["documents"][0])

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
