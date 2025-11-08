---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieval evaluation using LLM-as-a-judge via Pydantic AI

> This page contains a tutorial on how to evaluate retrieval systems using LLMs as judges via Pydantic AI.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/retrieval_eval_pydantic_ai.ipynb" />

We'll explore how to evaluate retrieval systems using Large Language Models (LLMs) as judges.Retrieval evaluation is a critical component in building high-quality information retrieval systems, and recent advancements in LLMs have made it possible to automate this evaluation process.

**What we'll cover**

* How to query the Wikipedia API
* How to implement and compare two different retrieval approaches:
  * The original search results from the Wikipedia API
  * Using Cohere's reranking model to rerank the search results
* How to set up an LLM-as-a-judge evaluation framework using Pydantic AI

**Tools We'll Use**

* **Cohere's API**: For reranking search results and providing evaluation models
* **Wikipedia's API**: As our information source
* **Pydantic AI**: For creating evaluation agents

This tutorial demonstrates a methodology for comparing different retrieval systems objectively. By the end, you'll have an example you can adapt to evaluate your own retrieval systems across different domains and use cases.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
