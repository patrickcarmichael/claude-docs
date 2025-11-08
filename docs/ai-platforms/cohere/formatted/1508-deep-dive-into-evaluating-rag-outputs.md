---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deep Dive Into Evaluating RAG Outputs

> This page contains information on evaluating the output of RAG systems.

<AuthorsContainer
  authors={[
    {
      name: "Marco Del Tredici",
      imageSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/f103c96-Marco.jpg",
    },
  ]}
/>

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Deep_dive_into_RAG_evaluation.ipynb" />

In this notebook, we'll show you how to evaluate the output of a RAG system. The high-level RAG flow is depicted in the diagram below.

We will focus on the evaluation of **Retrieve** and **Response** (or **Generation**), and present a set of metrics for each phase. We will deep dive into each metric, to give you a full understanding of how we evaluate models and why we do it this way, and provide code so you can repdroduce on your own data.

To demonstrate the metrics, we will use data from the [Docugami's KG-RAG](https://github.com/docugami/KG-RAG-datasets/tree/main/sec-10-q/data/v1) dataset, a RAG dataset for financial 10Q filing reports. We will focus only on evaluation, without performing the actual Retrieval and response Generation steps.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
