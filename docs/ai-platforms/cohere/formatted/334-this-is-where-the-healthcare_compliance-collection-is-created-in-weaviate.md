---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## This is where the "Healthcare_Compliance" collection is created in Weaviate.

client.collections.create(
    "Healthcare_Compliance",
    vectorizer_config=[
        # Configure a named vectorizer using Cohere's  model

        Configure.NamedVectors.text2vec_cohere(
            name="title_vector",  # Name of the vectorizer

            source_properties=[
                "title"
            ],  # Property to vectorize (in this case, the "title" field)

            model="embed-english-v3.0",  # Cohere model to use for vectorization

        )
    ],
)
```
You'll see something like this:
```
<weaviate.collections.collection.sync.Collection at 0x7f48a5604590>
```
Next, we'll define the list of healthcare compliance documents, retrieve the `"Healthcare_Compliance"` collection from the Weaviate client, and use a dynamic batch process to add multiple documents to the collection efficiently.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
