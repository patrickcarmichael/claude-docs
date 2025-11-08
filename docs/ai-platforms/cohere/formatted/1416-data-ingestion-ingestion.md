---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data Ingestion \[#ingestion]

In order to set up our RAG implementation, we need to separate the parsed text into chunks and load the chunks to an index. The index will allow us to retrieve relevant passages from the document for different queries. Here, we use a simple implementation of indexing using the `hnswlib` library. Note that there are many different indexing solutions that are appropriate for specific production use cases.
```python PYTHON
"""
Read parsed document content and chunk data
"""

import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = []

with open("{}/{}-parsed-fda-approved-drug.txt".format(data_dir, source), "r") as doc:
    doc_content = doc.read()

"""
Personal notes on chunking
https://medium.com/@ayhamboucher/llm-based-context-splitter-for-large-documents-445d3f02b01b
"""


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
