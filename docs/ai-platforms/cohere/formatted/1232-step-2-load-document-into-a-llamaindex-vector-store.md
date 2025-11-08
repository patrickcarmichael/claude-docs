---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## **Step 2: Load document into a LlamaIndex vector store**

Loading the document into a LlamaIndex vector store will allow us to use the Cohere embedding model and rerank model to retrieve the relevant parts of the form to pass into Command.
```python PYTHON
from llama_index.core import Settings, VectorStoreIndex

from llama_index.postprocessor.cohere_rerank import CohereRerank

from llama_index.embeddings.cohere import CohereEmbedding

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
