---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating a QA Bot From Technical Documentation

> This page describes how to use Cohere to build a simple question-answering system.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Creating_a_QA_bot_from_technical_documentation.ipynb" />

This notebook demonstrates how to create a chatbot (single turn) that answers user questions based on technical documentation made available to the model.

We use the `aws-documentation` dataset ([link](https://github.com/siagholami/aws-documentation/tree/main)) for representativeness. This dataset contains 26k+ AWS documentation pages, preprocessed into 120k+ chunks, and 100 questions based on real user questions.

We proceed as follows:

1. Embed the AWS documentation into a vector database using Cohere embeddings and `llama_index`
2. Build a retriever using Cohere's `rerank` for better accuracy, lower inference costs and lower latency
3. Create model answers for the eval set of 100 questions
4. Evaluate the model answers against the golden answers of the eval set

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
