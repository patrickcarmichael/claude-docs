---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic RAG

To see how RAG works, let's define the documents that the application has access to. We'll use a short list of documents consisting of internal FAQs about the fictitious company Co1t (in production, these documents are massive).

In this example, each document is a `data` object with one field, `text`. But we can define any number of fields we want, depending on the nature of the documents. For example, emails could contain `title` and `text` fields.
```python PYTHON
documents = [
    {
        "data": {
            "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
        }
    },
    {
        "data": {
            "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
        }
    },
    {
        "data": {
            "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
        }
    },
]
```
To call the Chat API with RAG, pass the following parameters at a minimum. This tells the model to run in RAG-mode and use these documents in its response.

* `model` for the model ID
* `messages` for the user's query.
* `documents` for defining the documents.

Let's create a query asking about the company's support for personal well-being, which is not going to be available to the model based on the data its trained on. It will need to use external documents.

RAG introduces additional objects in the Chat response. One of them is `citations`, which contains details about:

* specific text spans from the retrieved documents on which the response is grounded.
* the documents referenced in the citations.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
