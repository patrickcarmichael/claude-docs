---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Redis and Cohere (Integration Guide)

> Learn how to integrate Cohere with Redis for similarity searches on text data with this step-by-step guide.

<img src="file:15a113d5-0075-4708-8f6f-4ad28c682e53" width="200px" height="auto" class="light-bg" />

[RedisVL](https://www.redisvl.com/) provides a powerful, dedicated Python client library for using Redis as a Vector Database. This walks through how to integrate [Cohere embeddings](/docs/embeddings) with Redis using a dataset of Wikipedia articles to set up a pipeline for semantic search. It will cover:

* Setting up a Redis index
* Embedding passages and storing them in the database
* Embedding the user’s search query and searching against your Redis index
* Exploring different filtering options for your query

To see the full code sample, refer to this [notebook](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Cohere_Redis_Guide.ipynb). You can also consult [this guide](https://www.redisvl.com/user_guide/vectorizers_04.html#cohere) for more information on using Cohere with Redis.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
