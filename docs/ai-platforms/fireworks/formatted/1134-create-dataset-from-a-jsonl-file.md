---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create dataset from a JSONL file

dataset = Dataset.from_file("path/to/training_data.jsonl")
```

### `from_string()`

```python
@classmethod
from_string(data: str)
```
Creates a Dataset from a string containing JSONL-formatted training examples.
```python
from fireworks import Dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
