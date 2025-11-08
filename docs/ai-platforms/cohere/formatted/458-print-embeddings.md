---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print embeddings

print(len(embeddings))
print(embeddings[:5])
```

### Cohere Rerank with LlamaIndex

To use Cohere's rerank functionality with LlamaIndex create a [ Cohere Rerank object ](https://docs.llamaindex.ai/en/latest/examples/node_postprocessor/CohereRerank.html#) and use as a [node post processor.](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/root.html)
```python PYTHON
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.readers.web import (
    SimpleWebPageReader,
)  # first, run `pip install llama-index-readers-web`

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
