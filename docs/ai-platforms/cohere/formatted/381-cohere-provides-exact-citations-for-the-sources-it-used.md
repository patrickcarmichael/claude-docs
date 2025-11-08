---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere provides exact citations for the sources it used

print(response.get("citations"))
```

### Cohere Chat and RAG with LangChain

To use Cohere's [retrieval augmented generation (RAG)](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) functionality with LangChain, create a [CohereRagRetriever](https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/retrievers/cohere_rag_retriever.py) object. Then there are a few RAG uses, discussed in the next few sections.

#### Using LangChain's Retrievers

In this example, we use the [wikipedia retriever](https://python.langchain.com/docs/integrations/retrievers/wikipedia) but any [retriever supported by LangChain](https://python.langchain.com/docs/integrations/retrievers) can be used here.  In order to set up the wikipedia retriever you need to install the wikipedia python package using `%pip install --upgrade --quiet  wikipedia`. With that done, you can execute this code to see how a retriever works:
```python PYTHON
from langchain_cohere import CohereRagRetriever
from langchain.retrievers import WikipediaRetriever
from langchain_cohere import ChatCohere

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
