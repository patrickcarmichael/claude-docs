---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## {'llm': {'replies': [' Paris is the capital of France. It is known for its history, culture, and many iconic landmarks, such as the Eiffel Tower and Notre-Dame Cathedral. '], 'meta': [{'finish_reason': 'COMPLETE'}]}}

```

### Cohere Embeddings with Haystack

You can use Cohere’s embedding models within your Haystack RAG pipelines. The list of all supported models can be found in Cohere’s [model documentation](/docs/models#representation). Set an environment variable for your `COHERE_API_KEY` before running the code samples below.

Although these examples use an `InMemoryDocumentStore` to keep things simple, Haystack supports [a variety](https://haystack.deepset.ai/integrations?type=Document+Store) of vector database and document store options.

#### Index Documents with Haystack and Cohere Embeddings

```python PYTHON
from haystack import Pipeline
from haystack import Document
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.components.writers import DocumentWriter
from haystack_integrations.components.embedders.cohere import (
    CohereDocumentEmbedder,
)
from haystack.utils import Secret
import os

COHERE_API_KEY = os.environ.get("COHERE_API_KEY")
token = Secret.from_token(COHERE_API_KEY)

document_store = InMemoryDocumentStore(
    embedding_similarity_function="cosine"
)

documents = [
    Document(content="My name is Wolfgang and I live in Berlin"),
    Document(content="I saw a black horse running"),
    Document(content="Germany has many big cities"),
]

indexing_pipeline = Pipeline()
indexing_pipeline.add_component(
    "embedder", CohereDocumentEmbedder(token)
)
indexing_pipeline.add_component(
    "writer", DocumentWriter(document_store=document_store)
)
indexing_pipeline.connect("embedder", "writer")

indexing_pipeline.run({"embedder": {"documents": documents}})
print(document_store.filter_documents())

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
