---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieve

To retrieve the metadata of a previously uploaded file:
```sh
together files retrieve <FILE-ID>
```
Here's a sample output:
```sh
$ together files retrieve file-d931200a-6b7f-476b-9ae2-8fddd5112308
{
    "filename": "example.jsonl",
    "bytes": 5433223,
    "created_at": 1690432046,
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "purpose": "fine-tune",
    "object": "file",
    "LineCount": 0,
    "Processed": true
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
