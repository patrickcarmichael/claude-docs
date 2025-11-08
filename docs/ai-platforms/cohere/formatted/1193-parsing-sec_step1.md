---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parsing \[#sec\_step1]

To improve RAG performance on PDFs with mixed types (text and tables), we investigated a number of parsing and chunking strategies from various libraries:

* [PyPDFLoader (LC)](https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.pdf.PyPDFLoader.html)
* [LlamaParse](https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/) (Llama-Index)
* [Unstructured](https://unstructured.io/)

We have found that the best option for parsing is unstructured.io since the parser can:

* separate tables from text
* automatically chunk the tables and text by title during the parsing step so that similar elements are grouped
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
