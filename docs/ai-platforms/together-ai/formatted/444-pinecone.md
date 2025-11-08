---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pinecone

*Pinecone is a vector database that helps companies build RAG applications.*

Here's some sample code to get you started with Pinecone + Together AI:
```python
from pinecone import Pinecone, ServerlessSpec
from together import Together

pc = Pinecone(api_key="PINECONE_API_KEY", source_tag="TOGETHER_AI")
client = Together()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
