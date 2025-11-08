---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reranking - Cohere on Azure AI Foundry

> A guide for performing reranking with Cohere's Reranking models on Azure AI Foundry (API v2).

[Open in GitHub](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/cohere-on-azure/v2/azure-ai-reranking.ipynb)

In this tutorial, we'll explore reranking using Cohere's Rerank model on Azure AI Foundry.

Reranking is a crucial technique used in information retrieval systems, particularly for large-scale search applications. The process involves taking an initial set of retrieved documents and reordering them based on how relevant they are to the user's search query.

One of the most compelling aspects of reranking is its ease of implementation - despite providing substantial improvements to search results, Cohere's Rerank models can be integrated into any existing search system with just a single line of code, regardless of whether it uses semantic or traditional keyword-based search approaches.

In this tutorial, we'll cover:

* Setting up the Cohere client
* Retrieving documents
* Reranking documents
* Reranking semi structured data

We'll use Cohere's Embed model deployed on Azure to demonstrate these capabilities and help you understand how to effectively implement semantic search in your applications.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
