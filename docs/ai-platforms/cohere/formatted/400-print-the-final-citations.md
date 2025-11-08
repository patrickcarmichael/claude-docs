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

#### Using the `create_stuff_documents_chain` Chain

This chain takes a list of documents and formats them all into a prompt, then passes that prompt to an LLM. It passes ALL documents, so you should make sure it fits within the context window of the LLM you are using.

Note: this feature is currently in beta.
```python PYTHON
from langchain_cohere import ChatCohere
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)

prompt = ChatPromptTemplate.from_messages(
    [("human", "What are everyone's favorite colors:\n\n{context}")]
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
