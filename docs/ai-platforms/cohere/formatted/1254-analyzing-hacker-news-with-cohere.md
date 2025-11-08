---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Analyzing Hacker News with Cohere

> This page describes building a generative-AI powered tool to analyze headlines with Cohere.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Analyzing_Hacker_News_with_Six_Language_Understanding_Methods.ipynb" />

Large language models give machines a vastly improved representation and understanding of language. These abilities give developers more options for content recommendation, analysis, and filtering.

In this notebook we take thousands of the most popular posts from Hacker News and demonstrate some of these functionalities:

1. Given an existing post title, retrieve the most similar posts (nearest neighbor search using embeddings)
2. Given a query that we write, retrieve the most similar posts
3. Plot the archive of articles by similarity (where similar posts are close together and different ones are far)
4. Cluster the posts to identify the major common themes
5. Extract major keywords from each cluster so we can identify what the clsuter is about
6. (Experimental) Name clusters with a generative language model

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
