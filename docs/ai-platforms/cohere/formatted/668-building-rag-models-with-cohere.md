---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building RAG models with Cohere

> This page walks through building a retrieval-augmented generation model with Cohere.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt6_v2.ipynb">
  Open in Colab
</a>

The Chat endpoint provides comprehensive support for various text generation use cases, including retrieval-augmented generation (RAG).

While LLMs are good at maintaining the context of the conversation and generating responses, they can be prone to hallucinate and include factually incorrect or incomplete information in their responses.

RAG enables a model to access and utilize supplementary information from external documents, thereby improving the accuracy of its responses.

When using RAG with the Chat endpoint, these responses are backed by fine-grained citations linking to the source documents. This makes the responses easily verifiable.

In this tutorial, you'll learn about:

* Basic RAG
* Search query generation
* Retrieval with Embed
* Reranking with Rerank
* Response and citation generation

You'll learn these by building an onboarding assistant for new hires.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
