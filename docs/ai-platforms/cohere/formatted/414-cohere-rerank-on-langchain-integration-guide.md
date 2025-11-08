---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere Rerank on LangChain (Integration Guide)

> This page describes how to integrate Cohere's ReRank models with LangChain.

Cohere supports various integrations with LangChain, a large language model (LLM) framework which allows you to quickly create applications based on Cohere's models. This doc will guide you through how to leverage Rerank with LangChain.

### Prerequisites

Running Cohere Rerank with LangChain doesn't require many prerequisites, consult the [top-level document](/docs/cohere-and-langchain) for more information.

### Cohere ReRank with LangChain

To use Cohere's [rerank functionality ](/docs/reranking) with LangChain, start with instantiating a [CohereRerank](https://github.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/retrievers/document_compressors/cohere_rerank.py) object as follows: `cohere_rerank = CohereRerank(cohere_api_key="{API_KEY}")`.

You can then use it with LangChain retrievers, embeddings, and RAG. The example below uses the vector DB chroma, for which you will need to install `pip install chromadb`. Other vector DB's [from this list](https://python.langchain.com/docs/integrations/vectorstores) can also be used.
```python PYTHON
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereEmbeddings
from langchain_cohere import ChatCohere
from langchain_cohere import CohereRerank, CohereRagRetriever
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader

user_query = "what is Cohere Toolkit?"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
