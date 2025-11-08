---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Weaviate and Cohere (Integration Guide)

> This page describes how to integrate Cohere with the Weaviate database.

<img src="file:264fd6e0-c583-42dc-8742-0612e48f1074" width="200px" height="auto" class="light-bg" />

[Weaviate](https://weaviate.io/) is an open source vector search engine that stores both objects and vectors, allowing for combining vector search with structured filtering. Here, we'll create a Weaviate Cluster to index your data with Cohere Embed, and process it with Rerank and Command.

Here are the steps involved:

* Create the Weaviate cluster (see [this post](https://weaviate.io/developers/wcs/quickstart) for more detail.)
* Once the cluster is created, you will receive the cluster URL and API key.
* Use the provided URL and API key to connect to your Weaviate cluster.
* Use the Weaviate Python client to create your collection to store data

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
