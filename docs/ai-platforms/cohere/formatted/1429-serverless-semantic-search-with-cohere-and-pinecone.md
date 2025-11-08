---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Serverless Semantic Search with Cohere and Pinecone

> This page contains a basic tutorial on how to get Cohere and the Pinecone vector database to work well together.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Embed_Jobs_Serverless_Pinecone_Semantic_Search.ipynb" />
```python PYTHON
import os
import json
import time
import numpy as np
import cohere
from pinecone import Pinecone

co = cohere.Client('COHERE_API_KEY')
pc = Pinecone(
    api_key="PINECONE_API_KEY",
    source_tag="cohere"
)
```
```txt title="Output"
/usr/local/lib/python3.10/dist-packages/pinecone/data/index.py:1: TqdmExperimentalWarning: Using `tqdm.autonotebook.tqdm` in notebook mode. Use `tqdm.tqdm` instead to force console mode (e.g. in jupyter console)
    from tqdm.autonotebook import tqdm
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
