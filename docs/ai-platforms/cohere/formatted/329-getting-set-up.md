---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Set up

First, let's handle the imports, the URLs, and the pip installs.
```python PYTHON
from google.colab import userdata

weaviate_url = userdata.get("WEAVIATE_ENDPOINT")
weaviate_key = userdata.get("WEAVIATE_API_KEY")
cohere_key = userdata.get("COHERE_API_KEY")
```
```python PYTHON
!pip install -U weaviate-client -q
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
