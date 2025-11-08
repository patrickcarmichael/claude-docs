---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How the Files API works

The Files API provides a simple create-once, use-many-times approach for working with files:

* **Upload files** to our secure storage and receive a unique `file_id`
* **Download files** that are created from skills or the code execution tool
* **Reference files** in [Messages](/en/api/messages) requests using the `file_id` instead of re-uploading content
* **Manage your files** with list, retrieve, and delete operations

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
