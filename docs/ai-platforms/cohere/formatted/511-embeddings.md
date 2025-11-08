---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embeddings

You can use this code to invoke Cohere’s Embed English v3 model (`cohere.embed-english-v3`) or Embed Multilingual v3 model (`cohere.embed-multilingual-v3`) on Amazon Bedrock:
```python PYTHON
import cohere

co = cohere.BedrockClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
