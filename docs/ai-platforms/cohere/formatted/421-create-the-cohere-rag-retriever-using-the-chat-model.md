---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the cohere rag retriever using the chat model

rag = CohereRagRetriever(llm=llm, connectors=[])
docs = rag.get_relevant_documents(
    user_query,
    documents=compressed_docs,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
