---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text parsing

filename = "llamaparse-text-parsed-{}.txt".format(source_filename)

with open("{}/{}".format(data_dir, filename), "r") as doc:
    parsed_document = doc.read()

print(parsed_document[:1000])
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
