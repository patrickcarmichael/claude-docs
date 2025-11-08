---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieval augmented generation (RAG) - Cohere on Azure AI Foundry

> A guide for performing retrieval augmented generation (RAG) with Cohere's Command models on Azure AI Foundry (API v2).

[Open in GitHub](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/cohere-on-azure/v2/azure-ai-rag.ipynb)

Large Language Models (LLMs) excel at generating text and maintaining conversational context in chat applications. However, LLMs can sometimes hallucinate - producing responses that are factually incorrect. This is particularly important to mitigate in enterprise environments where organizations work with proprietary information that wasn't part of the model's training data.

Retrieval-augmented generation (RAG) addresses this limitation by enabling LLMs to incorporate external knowledge sources into their response generation process. By grounding responses in retrieved facts, RAG significantly reduces hallucinations and improves the accuracy and reliability of the model's outputs.

In this tutorial, we'll cover:

* Setting up the Cohere client
* Building a RAG application by combining retrieval and chat capabilities
* Managing chat history and maintaining conversational context
* Handling direct responses vs responses requiring retrieval
* Generating citations for retrieved information

In the next tutorial, we'll explore how to leverage Cohere's tool use features to build agentic applications.

We'll use Cohere's Command, Embed, and Rerank models deployed on Azure.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
