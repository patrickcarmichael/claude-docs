---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Upload training data

with open("legal_qa_dataset.jsonl", "rb") as f:
    file_upload = client.files.upload(file=f, purpose="fine-tune")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
