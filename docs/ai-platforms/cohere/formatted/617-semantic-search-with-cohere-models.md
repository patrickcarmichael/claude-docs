---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Semantic Search with Cohere Models

> This is a tutorial describing how to leverage Cohere's models for semantic search.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt4_v2.ipynb">
  Open in Colab
</a>

[Text embeddings](/v2/docs/embeddings) are lists of numbers that represent the context or meaning inside a piece of text. This is particularly useful in search or information retrieval applications. With text embeddings, this is called semantic search.

Semantic search solves the problem faced by the more traditional approach of lexical search, which is great at finding keyword matches, but struggles to capture the context or meaning of a piece of text.

With Cohere, you can generate text embeddings through the Embed endpoint.

In this tutorial, you'll learn about:

* Embedding the documents
* Embedding the query
* Performing semantic search
* Multilingual semantic search
* Changing embedding compression types

You'll learn these by building an onboarding assistant for new hires.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
