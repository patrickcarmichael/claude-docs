---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create dataset from a JSONL string

jsonl_data = """
{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there!"}]}
{"messages": [{"role": "user", "content": "What is 1+1?"}, {"role": "assistant", "content": "2"}]}
"""
dataset = Dataset.from_string(jsonl_data)
```

### `from_id()`

```python
@classmethod
from_id(id: str)
```
Creates a Dataset from an existing dataset ID on Fireworks.
```python
from fireworks import Dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
