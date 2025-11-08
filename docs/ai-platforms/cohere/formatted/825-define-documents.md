---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define documents

Next, we’ll define the documents we’ll use for RAG. We’ll use a few pages from the Cohere documentation that discuss prompt engineering. Each entry is identified by its title and URL.
```python PYTHON
raw_documents = [
    {
        "title": "Crafting Effective Prompts",
        "url": "https://docs.cohere.com/docs/crafting-effective-prompts",
    },
    {
        "title": "Advanced Prompt Engineering Techniques",
        "url": "https://docs.cohere.com/docs/advanced-prompt-engineering-techniques",
    },
    {
        "title": "Prompt Truncation",
        "url": "https://docs.cohere.com/docs/prompt-truncation",
    },
    {
        "title": "Preambles",
        "url": "https://docs.cohere.com/docs/preambles",
    },
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
