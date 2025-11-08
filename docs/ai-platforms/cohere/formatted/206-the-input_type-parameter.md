---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The `input_type` parameter

Cohere embeddings are optimized for different types of inputs.

* When using embeddings for [semantic search](/docs/semantic-search), the search query should be embedded by setting `input_type="search_query"`
* When using embeddings for semantic search, the text passages that are being searched over should be embedded with `input_type="search_document"`.
* When using embedding for `classification` and `clustering` tasks, you can set `input_type` to either 'classification' or 'clustering' to optimize the embeddings appropriately.
* When `input_type='image'` for `embed-v3.0`, the expected input to be embedded is an image instead of text. If you use `input_type=images` with `embed-v4.0` it will default to `search_document`. We recommend using `search_document` when working with `embed-v4.0`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
