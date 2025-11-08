---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multilingual semantic search

The Embed endpoint also supports multilingual semantic search via the `embed-multilingual-...` models. This means you can perform semantic search on texts in different languages.

Specifically, you can do both multilingual and cross-lingual searches using one single model.

Multilingual search happens when the query and the result are of the same language. For example, an English query of “places to eat” returning an English result of “Bob's Burgers.” You can replace English with other languages and use the same model for performing search.

Cross-lingual search happens when the query and the result are of a different language. For example, a Hindi query of “खाने की जगह” (places to eat) returning an English result of “Bob's Burgers.”

In the example below, we repeat the steps of performing semantic search with one difference – changing the model type to the multilingual version. Here, we use the `embed-v4.0` model. Here, we are searching a French version of the FAQ list using an English query.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
