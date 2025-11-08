---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the Index

The mapping of the destination index – the index that contains the embeddings that the model will generate based on your input text – must be created. The destination index must have a field with the [`semantic_text`](https://www.google.com/url?q=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2Fcurrent%2Fsemantic-text.html) field type to index the output of the Cohere model.

Let's create an index named cohere-wiki-embeddings with the mappings we need
```python PYTHON
client.indices.delete(
    index="cohere-wiki-embeddings", ignore_unavailable=True
)
client.indices.create(
    index="cohere-wiki-embeddings",
    mappings={
        "properties": {
            "text_semantic": {
                "type": "semantic_text",
                "inference_id": "cohere_embeddings",
            },
            "text": {"type": "text", "copy_to": "text_semantic"},
            "wiki_id": {"type": "integer"},
            "url": {"type": "text"},
            "views": {"type": "float"},
            "langs": {"type": "integer"},
            "title": {"type": "text"},
            "paragraph_id": {"type": "integer"},
            "id": {"type": "integer"},
        }
    },
)
```
You might see something like this:
```
ObjectApiResponse({'acknowledged': True, 'shards_acknowledged': True, 'index': 'cohere-wiki-embeddings'})
```
Let's note a few important parameters from that API call:

* `semantic_text`: A field type automatically generates embeddings for text content using an inference endpoint.
* `inference_id`: Specifies the ID of the inference endpoint to be used. In this example, the model ID is set to cohere\_embeddings.
* `copy_to`: Specifies the output field which contains inference results

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
