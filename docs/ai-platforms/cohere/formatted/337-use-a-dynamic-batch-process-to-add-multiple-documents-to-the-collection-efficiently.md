---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use a dynamic batch process to add multiple documents to the collection efficiently

with collection.batch.dynamic() as batch:
    for src_obj in hl_compliance_docs:
        # Add each document to the batch, specifying the "title" and "description" properties

        batch.add_object(
            properties={
                "title": src_obj["title"],
                "description": src_obj["description"],
            },
        )
```
Now, we'll iterate over the objects we've retrieved and print their results:
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
