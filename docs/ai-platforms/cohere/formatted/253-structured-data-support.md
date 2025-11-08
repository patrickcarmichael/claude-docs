---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Structured Data Support

Our Rerank models support reranking structured data formatted as a list of YAML strings. Note that since long document strings get truncated, the order of the keys is especially important. When constructing the YAML string from a dictionary, make sure to maintain the order. In Python that is done by setting `sort_keys=False` when using `yaml.dump`.

Example:
```python
import yaml

docs = [
    {
        "Title": "How to fix a dishwasher",
        "Author": "John Smith",
        "Date": "August 1st 2023",
        "Content": "Fixing a dishwasher depends on the specific problem you're facing. Here are some common issues and their potential solutions:....",
    },
    {
        "Title": "How to fix a leaky sink",
        "Date": "July 25th 2024",
        "Content": "Fixing a leaky sink will depend on the source of the leak. Here are general steps you can take to address common types of sink leaks:.....",
    },
]

yaml_docs = [yaml.dump(doc, sort_keys=False) for doc in docs]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
