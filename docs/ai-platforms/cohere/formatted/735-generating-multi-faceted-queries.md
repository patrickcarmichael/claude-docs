---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating Multi-Faceted Queries

> Build a system that generates multi-faceted queries to capture the full intent of a user's request.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt4_multi_faceted_queries.ipynb">
  Open in Colab
</a>

Consider a RAG system that needs to search through a large database of code examples and tutorials. A user might ask for "Python examples using the chat endpoint" or "JavaScript tutorials for text summarization".

In a basic RAG setup, these queries would be passed as-is to a search function, potentially missing important context or failing to leverage the structured nature of the data. For example, the code examples database might consist of metadata such as the programming language, the created time, the tech stack used, and so on.

It would be great if we could design a system that could leverage this metadata as a filter to retrieve only the relevant results.

We can achieve this using a tool use approach. Here, we can build a system that generates multi-faceted queries to capture the full intent of a user's request. This allows for more precise and relevant results by utilizing the semi-structured nature of the data.

Here are some examples of how this approach can be applied:

1. E-commerce product searches: Filtering by price range, category, brand, customer ratings, and availability.
2. Academic research databases: Narrowing results by publication year, field of study, citation count, and peer-review status.
3. Job search platforms: Refining job listings by location, experience level, salary range, and required skills.

In this tutorial, we'll cover:

* Defining the function for data querying
* Creating the tool for generating multi-faceted queries
* Building an agent for performing multi-faceted queries
* Running the agent

We'll build an agent that helps developers find relevant code examples and tutorials for using Cohere.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
