---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Elasticsearch and Cohere (Integration Guide)

> Learn how to create a semantic search pipeline with Elasticsearch and Cohere's generative AI capabilities.

<img src="file:23ad5437-5d6c-48df-85f8-c38f862ae641" width="200px" height="auto" class="light-bg" />

[Elasticsearch](https://www.elastic.co/search-labs/blog/elasticsearch-cohere-embeddings-support) has all the tools developers need to build next generation search experiences with generative AI, and it supports native integration with [Cohere](https://www.elastic.co/search-labs/blog/elasticsearch-cohere-embeddings-support) through their [inference API](https://www.elastic.co/guide/en/elasticsearch/reference/current/semantic-search-inference.html).

Use Elastic if you’d like to build with:

* A vector database
* Deploy multiple ML models
* Perform text, vector and hybrid search
* Search with filters, facet, aggregations
* Apply document and field level security
* Run on-prem, cloud, or serverless (preview)

This guide uses a dataset of Wikipedia articles to set up a pipeline for semantic search. It will cover:

* Creating an Elastic inference processor using Cohere embeddings
* Creating an Elasticsearch index with embeddings
* Performing hybrid search on the Elasticsearch index and reranking results
* Performing basic RAG

To see the full code sample, refer to this [notebook](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Cohere_Elastic_Guide.ipynb). You can also find an integration guide [here](https://www.elastic.co/search-labs/integrations/cohere).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
