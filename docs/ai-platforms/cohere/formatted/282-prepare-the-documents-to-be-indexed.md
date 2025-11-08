---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prepare the documents to be indexed

documents = []
for line in jsonl_data:
    data_dict = json.loads(line)
    documents.append(
        {
            "_index": "cohere-wiki-embeddings",
            "_source": data_dict,
        }
    )

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
