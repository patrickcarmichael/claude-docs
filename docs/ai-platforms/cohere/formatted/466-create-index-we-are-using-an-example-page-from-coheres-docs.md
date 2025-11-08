---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## create index (we are using an example page from Cohere's docs)

documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://docs.cohere.com/v2/docs/cohere-embed"]
)  # you can replace this with any other reader or documents

index = VectorStoreIndex.from_documents(documents=documents)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
