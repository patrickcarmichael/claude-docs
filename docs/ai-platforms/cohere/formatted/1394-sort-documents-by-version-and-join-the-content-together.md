---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Sort documents by version and join the content together.

for filename, docs in combined_versioned_parsed_documents.items():
  doc_content = " ".join([x[1] for x in sorted(docs, key=lambda x: x[0])])
  parsed_documents.append((filename, doc_content))

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
