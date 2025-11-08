---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Document ID

When passing the documents as context, you can optionally add custom IDs to the `id` field in the `document` object. These IDs will be used by the endpoint as the citation reference.

If you don't provide the `id` field, the ID will be auto-generated in the the format of `doc:<auto_generated_id>`. Example: `doc:0`.

Here is an example of using custom IDs. Here, we are adding custom IDs `100` and `101` to each of the two documents we are passing as context.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
