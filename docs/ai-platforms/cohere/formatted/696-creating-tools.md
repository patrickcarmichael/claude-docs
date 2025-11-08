---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating tools

The pre-requisite, before we can run a tool use workflow, is to set up the tools. Let's create three tools:

* `search_faqs`: A tool for searching the FAQs. For simplicity, we'll not implement any retrieval logic, but we'll simply pass a list of pre-defined documents, which are the FAQ documents we had used in the Text Embeddings section.
* `search_emails`: A tool for searching the emails. Same as above, we'll simply pass a list of pre-defined emails from the Reranking section.
* `create_calendar_event`: A tool for creating new calendar events. Again, for simplicity, we'll not implement actual event bookings, but will return a mock success event. In practice, we can connect to a calendar service API and implement all the necessary logic here.

Here, we are defining a Python function for each tool, but more broadly, the tool can be any function or service that can receive and send objects.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
