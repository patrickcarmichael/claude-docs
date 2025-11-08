---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the Cohere rag retriever using the chat model

rag = CohereRagRetriever(llm=llm, connectors=[])
docs = rag.invoke(
    "Does LangChain support cohere RAG?",
    documents=[
        Document(
            page_content="LangChain supports cohere RAG!",
            metadata={"id": "id-1"},
        ),
        Document(
            page_content="The sky is blue!", metadata={"id": "id-2"}
        ),
    ],
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
