---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## To view the source documents

from llama_index.core.response.pprint_utils import pprint_response

pprint_response(response, show_source=True)
```

### Cohere RAG with LlamaIndex

The following example uses Cohere's chat model, embeddings and rerank functionality to generate a response based on your data.
```python PYTHON
from llama_index.llms.cohere import Cohere
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.readers.web import (
    SimpleWebPageReader,
)  # first, run `pip install llama-index-readers-web`

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
