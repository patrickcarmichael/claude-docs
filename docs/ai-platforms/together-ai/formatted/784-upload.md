---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Upload

To upload a new data file:
```sh
together files upload <FILENAME>
```
Here's a sample output:
```sh
$ together files upload example.jsonl
Uploading example.jsonl: 100%|██████████████████████████████| 5.18M/5.18M [00:01<00:00, 4.20MB/s]
{
    "filename": "example.jsonl",
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "object": "file"
}
```
The `id` field in the response will be the assigned `file-id` for this file object.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
