---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting started with Voyage AI

To access Voyage embeddings:

1. Sign up on Voyage AI's website
2. Obtain an API key
3. Set the API key as an environment variable for convenience:
```bash
export VOYAGE_API_KEY="<your secret key>"
```
You can obtain the embeddings by either using the official [`voyageai` Python package](https://github.com/voyage-ai/voyageai-python) or HTTP requests, as described below.

### Voyage Python library

The `voyageai` package can be installed using the following command:
```bash
pip install -U voyageai
```
Then, you can create a client object and start using it to embed your texts:
```python
import voyageai

vo = voyageai.Client()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
