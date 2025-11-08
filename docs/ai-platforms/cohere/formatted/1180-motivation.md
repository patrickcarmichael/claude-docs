---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Motivation

Retrieval-augmented generation (RAG) allows language models to generate grounded answers to questions about documents. However, the complexity of the documents can significantly influence overall RAG performance. For instance, the documents may be PDFs that contain a mix of text and tables.

More broadly, the implementation of a RAG pipeline - including parsing and chunking of documents, along with the embedding and retrieval of the chunks - is critical to the accuracy of grounded answers. Additionally, it is sometimes not sufficient to merely retrieve the answers; a user may want further postprocessing performed on the output. This use case would benefit from giving the model access to tools.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
