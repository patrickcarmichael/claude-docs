---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create dataset from existing ID

dataset = Dataset.from_id("existing-dataset-id")
```

### `sync()`

Uploads the dataset to Fireworks if it doesn't already exist. This method automatically:

1. Checks if a dataset with the same content hash already exists
2. If it exists, skips the upload to avoid duplicates
3. If it doesn't exist, creates and uploads the dataset to Fireworks
4. Validates the dataset after upload
```python
from fireworks import Dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
