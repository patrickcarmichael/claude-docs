---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieve content

To download a previously uploaded file:
```sh
together files retrieve-content <FILE-ID>
```
Here's a sample output:
```sh
$ together files retrieve-content file-d931200a-6b7f-476b-9ae2-8fddd5112308
Downloading file-d931200a-6b7f-476b-9ae2-8fddd5112308.jsonl: 100%|██████████| 5.43M/5.43M [00:00<00:00, 10.0MiB/s]
file-d931200a-6b7f-476b-9ae2-8fddd5112308.jsonl
```
You can specify the output filename with `--output FILENAME` or `-o FILENAME`. By default, the dataset is saved to `<FILE-ID>.jsonl`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
