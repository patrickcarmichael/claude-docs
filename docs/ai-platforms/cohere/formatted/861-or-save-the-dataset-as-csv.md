---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## or save the dataset as csv

co.utils.save_dataset(
    dataset=my_dataset, filepath="./path/to/new/file.csv"
)
```

### Deleting a dataset

Datasets are automatically deleted after 30 days, but they can also be deleted manually. Here's a code snippet showing how to do that:
```python PYTHON
co.datasets.delete(id="<DATASET_ID>")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
