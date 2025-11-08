---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Assemble versioned documents together ({"doc_name": [(0, doc_content_0), (1, doc_content_1), ...]}).

for filename, doc_content in versioned_parsed_documents:
  filename, version = "-".join(filename.split("-")[:-1]), filename.split("-")[-1]
  combined_versioned_parsed_documents[filename].append((version, doc_content))

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
