---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed documents

docs = top_80_df["text"].to_list()
docs_lang = top_80_df["lang"].to_list()
translated_docs = top_80_df[
    "translation"
].to_list()  # for reference when returning non-English results

doc_embs = co.embed(
    model="embed-v4.0",
    texts=docs,
    input_type="search_document",
    embedding_types=["float"],
).embeddings.float

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
