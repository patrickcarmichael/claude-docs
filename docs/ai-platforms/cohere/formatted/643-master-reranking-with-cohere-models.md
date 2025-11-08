---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Master Reranking with Cohere Models

> This page contains a tutorial on using Cohere's ReRank models.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt5_v2.ipynb">
  Open in Colab
</a>

Reranking is a technique that provides a semantic boost to the search quality of any keyword or vector search system, and is especially useful in [RAG systems](/v2/docs/retrieval-augmented-generation-rag).

We can rerank results from semantic search as well as any other search systems such as lexical search. This means that companies can retain an existing keyword-based (also called “lexical”) or semantic search system for the first-stage retrieval and integrate the [Rerank endpoint](/v2/docs/rerank) in the second-stage reranking.

In this tutorial, you'll learn about:

* Reranking lexical/semantic search results
* Reranking semi-structured data
* Reranking tabular data
* Multilingual reranking

You'll learn these by building an onboarding assistant for new hires.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
