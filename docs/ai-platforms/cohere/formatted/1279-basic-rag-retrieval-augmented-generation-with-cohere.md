---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic RAG: Retrieval-Augmented Generation with Cohere

> This page describes how to work with Cohere's basic retrieval-augmented generation functionality.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Vanilla_RAG.ipynb" />

Retrieval-Augmented Generation (RAG) is a technique that combines the strengths of pre-trained language models with the ability to retrieve information from a large corpus of documents. RAG **enables the language model to produce more informed, accurate, and contextually relevant answers** than by relying on its pre-trained knowledge alone.

At Cohere, all RAG calls come with... **precise citations**! 🎉
The model cites which groups of words, in the RAG chunks, were used to generate the final answer.\
These citations make it easy to check where the model’s generated response claims are coming from and they help users gain visibility into the model reasoning.

RAG consists of 3 steps:

* Step 1: Indexing and given a user query, retrieve the relevant chunks from the index
* Step 2: Optionally, rerank the retrieved chunks
* Step 3: Generate the model final answer with **precise citations**, given the retrieved and reranked chunks

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
