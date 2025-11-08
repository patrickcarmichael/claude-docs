---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create index

The mapping of the destination index – the index that contains the embeddings that the model will create based on your input text – must be created. The destination index must have a field with the [dense\_vector](https://www.elastic.co/guide/en/elasticsearch/reference/current/dense-vector.html) field type to index the output of the Cohere model.

Let's create an index named `cohere-wiki-embeddings` with the mappings we need.
```python PYTHON
client.indices.delete(index="cohere-wiki-embeddings", ignore_unavailable=True)
client.indices.create(
    index="cohere-wiki-embeddings",
    settings={"index": {"default_pipeline": "cohere_embeddings"}},
    mappings={
        "properties": {
            "text_embedding": {
                "type": "dense_vector",
                "dims": 1024,
                "element_type": "byte"
            },
            "text": {"type": "text"},
            "wiki_id": {"type": "integer"},
            "url": {"type": "text"},
            "views": {"type": "float"},
            "langs": {"type": "integer"},
            "title": {"type": "text"},
            "paragraph_id": {"type": "integer"},
            "id": {"type": "integer"}
        }
    },
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
