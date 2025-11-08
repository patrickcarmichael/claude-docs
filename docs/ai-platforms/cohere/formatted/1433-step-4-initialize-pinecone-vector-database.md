---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 4: Initialize Pinecone vector database

```python PYTHON
from pinecone import ServerlessSpec

index_name = "embed-jobs-serverless-test-example"

pc.create_index(
name=index_name,
dimension=1024,
metric="cosine",
spec=ServerlessSpec(cloud='aws', region='us-west-2')
)

idx = pc.Index(index_name)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
