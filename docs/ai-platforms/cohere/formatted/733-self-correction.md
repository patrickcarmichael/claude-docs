---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Self-correction

The concept of sequential reasoning is useful in a broader sense, particularly where the agent needs to adapt and change its plan midway in a task.

In other words, it allows the agent to self-correct.

To illustrate this, let's look at an example. Here, the user is asking about the authors of the sentence BERT paper.

The agent attempted to find required information via the `search_developer_docs` tool.

However, we know that the tool doesn't contain this information because we have only added a small sample of documents.

As a result, the agent, having received the documents back without any relevant information, decides to search the internet instead. This is also helped by the fact that we have added specific instructions in the `search_internet` tool to search the internet for information not found in the developer documentation.

It finally has the information it needs, and uses it to answer the user's question.

This highlights another important aspect of agentic RAG, which allows a RAG system to be flexible. This is achieved by powering the retrieval component with an LLM.

On the other hand, a standard RAG system would typically hand-engineer this, and hence, is more rigid.
```python PYTHON
messages = run_agent(
    "Who are the authors of the sentence BERT paper?"
)
```
```mdx
QUESTION:
Who are the authors of the sentence BERT paper?
==================================================
TOOL PLAN:
I will search for the authors of the sentence BERT paper. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"authors of the sentence BERT paper"}
==================================================
TOOL PLAN:
I was unable to find any information about the authors of the sentence BERT paper. I will now search for 'sentence BERT paper authors'. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"sentence BERT paper authors"}
==================================================
RESPONSE:
The authors of the Sentence-BERT paper are Nils Reimers and Iryna Gurevych.
==================================================
CITATIONS:

Start: 43| End:55| Text:'Nils Reimers' 
Sources:
1. search_internet_z8t19852my9q:0
2. search_internet_z8t19852my9q:1
3. search_internet_z8t19852my9q:2
4. search_internet_z8t19852my9q:3
5. search_internet_z8t19852my9q:4


Start: 60| End:75| Text:'Iryna Gurevych.' 
Sources:
1. search_internet_z8t19852my9q:0
2. search_internet_z8t19852my9q:1
3. search_internet_z8t19852my9q:2
4. search_internet_z8t19852my9q:3
5. search_internet_z8t19852my9q:4
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
