---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print the final citations

citations = docs[-1].metadata["citations"]
print("Citations:")
print(docs[-1].__dict__)
```

#### Using Documents

In this example, we take documents (which might be generated in other parts of your application) and pass them into the [CohereRagRetriever](https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/retrievers/cohere_rag_retriever.py) object:
```python PYTHON
from langchain_cohere import CohereRagRetriever
from langchain_cohere import ChatCohere
from langchain_core.documents import Document

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
