---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Web search

* v1: Supported via the `web-search` connector in the `connectors` parameter
* v2: Supported via user-defined tools.

**v1**

Uses the web search connector to search the internet for information relevant to the user's query.
```python PYTHON
res_v1 = co_v1.chat(
    message="who won euro 2024",
    connectors=[{"id": "web-search"}],
)

print(res_v1.text)
```
```
Spain won the UEFA Euro 2024, defeating England 2-1 in the final.
```
**v2**

Web search functionality is supported via tools.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
