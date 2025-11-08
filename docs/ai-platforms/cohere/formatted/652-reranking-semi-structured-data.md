---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reranking semi-structured data

The Rerank 3 model supports multi-aspect and semi-structured data like emails, invoices, JSON documents, code, and tables. By setting the rank fields, you can select which fields the model should consider for reranking.

In the following example, we'll use an email data example. It is a semi-stuctured data that contains a number of fields – `from`, `to`, `date`, `subject`, and `text`.

Suppose the new hire now wants to search for any emails about check-in sessions. Let's pretend we have a list of 5 emails retrieved from the email provider's API.

To perform reranking over semi-structured data, we serialize the documents to YAML format, which prepares the data in the format required for reranking. Then, we pass the YAML formatted documents to the Rerank endpoint.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
