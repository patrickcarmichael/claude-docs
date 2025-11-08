---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reconstruct the input documents based on the index provided in the rereank response

ranked_documents = []
for document in response.body["rerank"]:
  ranked_documents.append({
      "title": raw_documents[int(document["index"])]["_source"]["title"],
      "text": raw_documents[int(document["index"])]["_source"]["text"]
  })

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
