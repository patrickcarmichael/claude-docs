---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Three steps of RAG

The RAG workflow generally consists of **3 steps**:

* **Generating search queries** for finding relevant documents. *What does the model recommend looking up before answering this question?*
* **Fetching relevant documents** from an external data source using the generated search queries. *Performing a search to find some relevant information.*
* **Generating a response** with inline citations using the fetched documents. *Generating a response using the fetched documents. This response will contain inline citations, which you can decide to leverage or ignore*.

### Example: Using RAG to identify the definitive 90s boy band

In this section, we will use the three step RAG workflow to finally settle the score between the notorious boy bands Backstreet Boys and NSYNC. We ask the model to provide an informed answer to the question `"Who is more popular: Nsync or Backstreet Boys?"`

### Step 1: Generating search queries

First, the model needs to generate an optimal set of search queries to use for retrieval.

There are different possible approaches to do this. In this example, we'll take a [tool use](/v2/docs/tool-use) approach.

Here, we build a tool that takes a user query and returns a list of relevant document snippets for that query. The tool can generate zero, one or multiple search queries depending on the user query.
```python PYTHON
message = "Who is more popular: Nsync or Backstreet Boys?"

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
