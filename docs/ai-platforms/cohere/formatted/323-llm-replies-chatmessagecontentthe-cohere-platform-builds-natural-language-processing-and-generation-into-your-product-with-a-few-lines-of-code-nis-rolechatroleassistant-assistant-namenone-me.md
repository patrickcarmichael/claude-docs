---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## {'llm': {'replies': [ChatMessage(content='The Cohere platform builds natural language processing and generation into your product with a few lines of code... \nIs', role=<ChatRole.ASSISTANT: 'assistant'>, name=None, meta={'model': 'command', 'usage': {'prompt_tokens': 273, 'response_tokens': 165, 'total_tokens': 438, 'billed_tokens': 430}, 'index': 0, 'finish_reason': None, 'documents': None, 'citations': None})]}}

```

### Use Cohere Models in Haystack RAG Pipelines

RAG provides an LLM with context allowing it to generate better answers. You can use any of [Cohere’s models](/docs/models) in a [Haystack RAG pipeline](https://docs.haystack.deepset.ai/v2.0/docs/creating-pipelines) with the `CohereGenerator`.

The code sample below adds a set of documents to an `InMemoryDocumentStore`, then uses those documents to answer a question. You’ll need your Cohere API key to run it.

Although these examples use an `InMemoryDocumentStore` to keep things simple, Haystack supports [a variety](https://haystack.deepset.ai/integrations?type=Document+Store) of vector database and document store options. You can use any of them in combination with Cohere models.
```python PYTHON
from haystack import Pipeline
from haystack.components.retrievers.in_memory import (
    InMemoryBM25Retriever,
)
from haystack.components.builders.prompt_builder import PromptBuilder
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack_integrations.components.generators.cohere import (
    CohereGenerator,
)
from haystack import Document
from haystack.utils import Secret

import os

COHERE_API_KEY = os.environ.get("COHERE_API_KEY")

docstore = InMemoryDocumentStore()
docstore.write_documents(
    [
        Document(content="Rome is the capital of Italy"),
        Document(content="Paris is the capital of France"),
    ]
)

query = "What is the capital of France?"

template = """
Given the following information, answer the question.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{ query }}?
"""
pipe = Pipeline()

pipe.add_component(
    "retriever", InMemoryBM25Retriever(document_store=docstore)
)
pipe.add_component("prompt_builder", PromptBuilder(template=template))
pipe.add_component(
    "llm", CohereGenerator(Secret.from_token(COHERE_API_KEY))
)
pipe.connect("retriever", "prompt_builder.documents")
pipe.connect("prompt_builder", "llm")

res = pipe.run(
    {
        "prompt_builder": {"query": query},
        "retriever": {"query": query},
    }
)

print(res)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
