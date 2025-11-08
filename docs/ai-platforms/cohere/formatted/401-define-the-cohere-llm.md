---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the Cohere LLM

llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

chain = create_stuff_documents_chain(llm, prompt)

docs = [
    Document(page_content="Jesse loves red but not yellow"),
    Document(
        page_content="Jamal loves green but not as much as he loves orange"
    ),
]

chain.invoke({"context": docs})
```

### Structured Output Generation

Cohere supports generating JSON objects to structure and organize the model’s responses in a way that can be used in downstream applications.

You can specify the `response_format` parameter to indicate that you want the response in a JSON object format.
```python PYTHON
from langchain_cohere import ChatCohere

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
