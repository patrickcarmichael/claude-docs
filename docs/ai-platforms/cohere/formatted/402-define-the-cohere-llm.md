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

res = llm.invoke(
    "John is five years old",
    response_format={
        "type": "json_object",
        "schema": {
            "title": "Person",
            "description": "Identifies the age and name of a person",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the person",
                },
                "age": {
                    "type": "number",
                    "description": "Age of the person",
                },
            },
            "required": [
                "name",
                "age",
            ],
        },
    },
)

print(res)
```

### Text Summarization

You can use the `load_summarize_chain` chain to perform text summarization.
```python PYTHON
from langchain_cohere import ChatCohere
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.cohere.com/docs/cohere-toolkit")
docs = loader.load()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
