---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the Cohere rag retriever using the chat model with the web search connector

rag = CohereRagRetriever(llm=llm, connectors=[{"id": "web-search"}])
docs = rag.invoke("Who founded Cohere?")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
