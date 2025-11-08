---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run LLM-as-a-judge evaluation to compare the two engines

Now we'll implement an evaluation framework using LLMs as judges to compare our two retrieval approaches:

* Engine A: Wikipedia results reranked by Cohere's reranking model
* Engine B: Original Wikipedia search results

Using LLMs as evaluators allows us to programmatically assess the quality of search results without human annotation. The following code implements the following steps:

* Setting up the evaluation protocol
  * First, define a clear protocol for how the LLM judges will evaluate the search results. This includes creating a system prompt and a template for each evaluation.
* Using multiple models as independent judges
  * To get more robust results, use multiple LLM models as independent judges. This reduces bias from any single model.
* Implementing a majority voting system
  * Combine judgments from multiple models using a majority voting system to determine which engine performed better for each query:
* Presenting the results
  * After evaluating all queries, present the results to determine which retrieval approach performed better overall.

This approach provides a scalable, reproducible method to evaluate and compare retrieval systems quantitatively.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
