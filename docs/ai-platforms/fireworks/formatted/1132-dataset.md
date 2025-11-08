---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Dataset

The `Dataset` class provides a convenient way to manage datasets for fine-tuning on Fireworks. It offers smart features like automatic naming and uploading of datasets. You do not instantiate a `Dataset` object directly. Instead, you create a `Dataset` object by using one of the class methods below.

**Properties:**

* `name` *str* - The full name of the dataset (e.g., `accounts/my-account/datasets/dataset-12345-my-data`)
* `id` *str* - The dataset identifier (e.g., `dataset-12345-my-data`)
* `url` *str* - The URL to view the dataset in the Fireworks dashboard

### `from_list()`

```python
@classmethod
from_list(data: list)
```
Creates a Dataset from a list of training examples. Each example should be compatible with OpenAI's chat completion format.
```python
from fireworks import Dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
