---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed a document

text = "This is a test document."
query_result = embeddings.embed_query(text)
print(query_result[:5], "...")
doc_result = embeddings.embed_documents([text])
print(doc_result[0][:5], "...")
```
To use these embeddings with Cohere's RAG functionality, you will need to use one of the vector DBs [from this list](https://python.langchain.com/docs/integrations/vectorstores). In this example we use chroma, so in order to run it you will need to install chroma using `pip install chromadb`.
```python PYTHON
from langchain_cohere import (
    ChatCohere,
    CohereEmbeddings,
    CohereRerank,
    CohereRagRetriever,
)
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader

user_query = "what is Cohere Toolkit?"

llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

embeddings = CohereEmbeddings(
    cohere_api_key="COHERE_API_KEY", model="embed-v4.0"
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
