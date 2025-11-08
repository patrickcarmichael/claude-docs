---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## read in your documents

jsonl_file_path = "data/redis_guide_data.jsonl"

corpus = []
text_to_embed = []

with jsonlines.open(jsonl_file_path, mode="r") as reader:
    for line in reader:
        corpus.append(line)
        # we want to store the embeddings of the field called `text`

        text_to_embed.append(line["text"])

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
