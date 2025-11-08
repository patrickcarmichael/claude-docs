---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1: Install libaries and Set Environment Variables

Critical Security Reminder: Safeguard your production environment by never committing sensitive information, such as environment variable values, to public repositories. This practice is essential for maintaining the security and integrity of your systems.

Libraries:

* `cohere`: A Python library for accessing Cohere's large language models, enabling natural language processing tasks like text generation, classification, and embedding.
* `pymongo`: The recommended Python driver for MongoDB, allowing Python applications to interact with MongoDB databases for data storage and retrieval.
* `datasets`: A library by Hugging Face that provides easy access to a wide range of datasets for machine learning and natural language processing tasks.
  \*`tqdm`: A fast, extensible progress bar library for Python, useful for displaying progress in long-running operations or loops.
```sh
pip install --quiet datasets tqdm cohere pymongo
```
```python
import os
import cohere

os.environ["COHERE_API_KEY"] = ""
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

os.environ["HF_TOKEN"] = ""
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
