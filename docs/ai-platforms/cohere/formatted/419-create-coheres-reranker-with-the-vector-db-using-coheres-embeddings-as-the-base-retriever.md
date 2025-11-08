---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create Cohere's reranker with the vector DB using Cohere's embeddings as the base retriever

reranker = CohereRerank(
    cohere_api_key="COHERE_API_KEY", model="rerank-english-v3.0"
)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker, base_retriever=db.as_retriever()
)
compressed_docs = compression_retriever.get_relevant_documents(
    user_query
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
