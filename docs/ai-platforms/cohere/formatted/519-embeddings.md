---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embeddings

You can use this code to invoke Cohere's embed model on Amazon SageMaker:
```python PYTHON
import cohere

co = cohere.SagemakerClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
