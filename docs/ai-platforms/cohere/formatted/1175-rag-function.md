---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## RAG function

```python PYTHON
def simple_rag(query, db):
    """
    Given user's query, retrieve top documents and generate response using documents parameter.
    """
    top_matched_document = retrieve_documents(query)["top_matched_document"]

    print("top_matched_document", top_matched_document)

    output = co.chat(
        message=query, model=COHERE_MODEL, documents=[top_matched_document]
    )

    return output.text
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
