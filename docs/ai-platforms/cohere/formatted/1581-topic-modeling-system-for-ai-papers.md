---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Topic Modeling System for AI Papers

> This page discusses how to create a topic-modeling system for papers focused on AI papers.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/Topic_Modeling_AI_Papers.ipynb" />

Natural Language Processing (NLP) is a key area of machine learning focused on analyzing and understanding text data. One popular NLP application is topic modeling, which uses unsupervised learning and clustering algorithms to group similar texts and extract underlying topics from document collections. This approach enables automatic document organization, efficient information retrieval, and content filtering.

Here, you'll learn how to use Cohere’s NLP tools to perform semantic search and clustering of AI Papers, which could help you discover trends in AI. You'll:

* Scrape the most recent page of the ArXiv page for AI, with the output being a list of recently published AI papers.
* Use Cohere’s Embed Endpoint to generate word embeddings using your list of AI papers.
* Visualize the embeddings and proceed to perform topic modeling.
* Use a tool to find the papers most relevant to a query you provide.

To follow along with this tutorial, you need to be familiar with Python and have python version 3.6+ installed, and you'll need to have a Cohere account. Everything that follows can be tested with a Google Colab notebook.

First, you need to install the python dependencies required to run the project. Use pip to install them using the command below.
```python PYTHON
pip install requests beautifulsoup4 cohere altair clean-text numpy pandas scikit-learn > /dev/null
```
And we'll also initialize the Cohere client.
```python PYTHON
import cohere

api_key = '<api_key>'
co = cohere.ClientV2(api_key="YOUR API KEY")
```typescript
With that done, we'll import the required libraries to make web requests, process the web content, and perform our topic-modeling functions.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
