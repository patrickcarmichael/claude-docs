---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Motivation

Retrieval augmented generation (RAG) has been a go-to use case that enterprises have been adopting with large language models (LLMs). Even though it works well in general, there are edge cases where this can fail. Most commonly, when the retrieved document mentions the query but actually refers to another document, the model will fail to generate the correct answer.

We propose an agentic RAG system that leverages tool use to continue to retrieve documents if correct ones were not retrieved at first try. This is ideal for use cases where accuracy is a top priority and latency is not. For example, lawyers trying to find the most accurate answer from their contracts are willing to wait a few more seconds to get the answer instead of getting wrong answers fast.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
