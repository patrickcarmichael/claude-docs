---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setting up the Schema.yaml:

To configure a Redis index you can either specify a `yaml` file or import a dictionary. In this tutorial we will be using a `yaml` file with the following schema. Either use the `yaml` file found at this [link](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/configs/redis_guide_schema.yaml), or create a `.yaml` file locally with the following configuration.
```yaml YAML
version: "0.1.0"
index:
  name: semantic_search_demo
  prefix: rvl
  storage_type: hash

fields:
  - name: url
    type: text
  - name: title
    type: tag
  - name: text
    type: text
  - name: wiki_id
    type: numeric
  - name: paragraph_id
    type: numeric
  - name: id
    type: numeric
  - name: views
    type: numeric
  - name: langs
    type: numeric
  - name: embedding
    type: vector
    attrs:
      algorithm: flat
      dims: 1024
      distance_metric: cosine
      datatype: float32
```
This index has a name of `semantic_search_demo` and uses `storage_type: hash` which means we must set `as_buffer=True` whenever we call the vectorizer. Hash data structures are serialized as a string and thus we store the embeddings in hashes as a byte string.

For this guide, we will be using the Cohere `embed-english-v3.0 model` which has a vector dimension size of `1024`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
