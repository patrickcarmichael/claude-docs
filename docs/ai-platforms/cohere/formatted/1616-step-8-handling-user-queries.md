---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 8: Handling User Queries

```python
def format_documents_for_chat(documents):
    return [
        {
            "company": doc["company"],
            # "reports": doc['reports'],

            "combined_attributes": doc["combined_attributes"],
        }
        for doc in documents
    ]


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
