---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get queries to run against our index from the model

r = co.chat(PROMPT, model="command-r", search_queries_only=True)
if r.search_queries:
    queries = [q["text"] for q in r.search_queries]
else:
    print("No queries returned by the model")
```
Now, with the queries in hand, we search against our vector index.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
