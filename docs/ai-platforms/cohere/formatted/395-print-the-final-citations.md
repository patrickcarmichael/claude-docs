---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print the final citations

citations = docs[-1].metadata["citations"]
print("Citations:")
print(citations)
```

#### Using a Connector

In this example, we create a generation with a [connector](https://docs.cohere.com/v1/docs/overview-rag-connectors) which allows us to get a generation with citations to results from the connector. We use the "web-search" connector, which is available to everyone. But if you have created your own connector in your org you can pass in its id, like so: `rag = CohereRagRetriever(llm=cohere_chat_model, connectors=[{"id": "example-connector-id"}])`

Here's a code sample illustrating how to use a connector:
```python PYTHON
from langchain_cohere import CohereRagRetriever
from langchain_cohere import ChatCohere
from langchain_core.documents import Document

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
