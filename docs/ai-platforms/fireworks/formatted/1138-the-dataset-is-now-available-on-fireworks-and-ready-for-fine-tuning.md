---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The dataset is now available on Fireworks and ready for fine-tuning

```

### `delete()`

Deletes the dataset from Fireworks.
```python
dataset = Dataset.from_file("path/to/training_data.jsonl")
dataset.delete()
```

### `head(n: int = 5, as_dataset: bool = False)`

Returns the first n rows of the dataset.

**Arguments:**

* `n` *int, optional* - Number of rows to return. Defaults to 5.
* `as_dataset` *bool, optional* - If True, return a Dataset object; if False, return a list. Defaults to False.

**Returns:**

* *list or Dataset* - List of dictionaries if as\_dataset=False, Dataset object if as\_dataset=True
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
