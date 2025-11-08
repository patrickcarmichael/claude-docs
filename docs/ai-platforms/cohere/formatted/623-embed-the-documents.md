---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed the documents

doc_emb = co.embed(
    model="embed-v4.0",
    input_type="search_document",
    texts=[doc["text"] for doc in documents],
).embeddings
```
Further reading:

* [Embed endpoint API reference](https://docs.cohere.com/reference/embed)
* [Documentation on the Embed endpoint](https://docs.cohere.com/docs/embeddings)
* [Documentation on the models available on the Embed endpoint](https://docs.cohere.com/docs/cohere-embed)
* [LLM University module on Text Representation](https://cohere.com/llmu#text-representation)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
