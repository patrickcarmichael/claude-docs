---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Documents

* v1: the `documents` parameter supports a list of objects with multiple fields per document.
* v2: the `documents` parameter supports a few different options for structuring documents:
  * List of objects with `data` object: same as v1 described above, but each document passed as a `data` object (with an optional `id` field to be used in citations).
  * List of objects with `data` string (with an optional `id` field to be used in citations).
  * List of strings.

**v1**
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
