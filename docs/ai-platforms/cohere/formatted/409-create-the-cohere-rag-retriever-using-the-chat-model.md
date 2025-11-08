---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the cohere rag retriever using the chat model

rag = CohereRagRetriever(llm=llm)
docs = rag.invoke(
    user_query,
    documents=input_docs,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
