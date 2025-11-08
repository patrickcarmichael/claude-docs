---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank semi structured data

The Rerank 3 model supports multi-aspect and semi-structured data like emails, invoices, JSON documents, code, and tables. By setting the rank fields, you can select which fields the model should consider for reranking.

In the following example, we’ll use an email data example. It is a semi-stuctured data that contains a number of fields – from, to, date, subject, and text.

The model will rerank based on order of the fields passed.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
