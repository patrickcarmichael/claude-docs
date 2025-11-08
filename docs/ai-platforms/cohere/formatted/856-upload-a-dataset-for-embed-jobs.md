---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Upload a dataset for embed jobs

ds = co.datasets.create(
    name="sample_file",
    # insert your file path here - you can upload it on the right - we accept .csv and jsonl files

    data=open("embed_jobs_sample_data.jsonl", "rb"),
    keep_fields=["wiki_id", "url", "views", "title"],
    optional_fields=["langs"],
    type="embed-input",
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
