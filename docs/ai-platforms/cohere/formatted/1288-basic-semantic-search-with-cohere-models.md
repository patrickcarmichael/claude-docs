---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Semantic Search with Cohere Models

> This page describes how to do basic semantic search with Cohere's models.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Basic_Semantic_Search.ipynb" />

Language models give computers the ability to search by meaning and go beyond searching by matching keywords. This capability is called semantic search.

<img alt="Searching an archive using sentence embeddings" src="https://github.com/cohere-ai/cohere-developer-experience/raw/main/notebooks/images/basic-semantic-search-overview.png?3" />

In this notebook, we'll build a simple semantic search engine. The applications of semantic search go beyond building a web search engine. They can empower a private search engine for internal documents or records. It can also be used to power features like StackOverflow's "similar questions" feature.

1. Get the archive of questions
2. [Embed](https://docs.cohere.ai/embed-reference/) the archive
3. Search using an index and nearest neighbor search
4. Visualize the archive based on the embeddings

And if you're running an older version of the SDK, you might need to upgrade it like so:
```python PYTHON
##!pip install --upgrade cohere
```http
Get your Cohere API key by [signing up here](https://dashboard.cohere.com/register). Paste it in the cell below.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
