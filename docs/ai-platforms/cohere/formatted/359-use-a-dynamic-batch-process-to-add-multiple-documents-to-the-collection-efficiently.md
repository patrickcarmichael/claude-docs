---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use a dynamic batch process to add multiple documents to the collection efficiently

with collection.batch.dynamic() as batch:
    for src_obj in legal_documents:
        # Add each document to the batch, specifying the "title" and "description" properties

        batch.add_object(
            properties={
                "title": src_obj["title"],
                "description": src_obj["description"],
            },
        )
```
As before, we'll iterate over the object and print the result:
```python PYTHON
from weaviate.classes.config import Configure
from weaviate.classes.generate import GenerativeConfig

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
