---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

The only difference between using Cohere's models on private deployments and the Cohere platform is how you set up the client. With private deployments, you need to pass the following parameters:

* `api_key` - Pass a blank value
* `base_url` - Pass the URL of your private deployment
```python PYTHON
import cohere

co = cohere.ClientV2(
    api_key="",  # Leave this blank

    base_url="<YOUR_DEPLOYMENT_URL>",
)
```typescript
To get started with example use cases, refer to the following quickstart examples:

* [Text Generation (Command model)](https://docs.cohere.com/docs/text-gen-quickstart)
* [RAG (Command model)](https://docs.cohere.com/docs/rag-quickstart)
* [Tool Use (Command model)](https://docs.cohere.com/docs/tool-use-quickstart)
* [Semantic Search (Embed model)](https://docs.cohere.com/docs/sem-search-quickstart)
* [Reranking (Rerank model)](https://docs.cohere.com/docs/reranking-quickstart)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
