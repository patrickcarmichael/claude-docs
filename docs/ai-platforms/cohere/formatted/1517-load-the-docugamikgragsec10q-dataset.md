---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## load the DocugamiKgRagSec10Q dataset

if os.path.exists("./data/source_files") and os.path.exists("./data/rag_dataset.json"):
        rag_dataset = LabelledRagDataset.from_json("./data/rag_dataset.json")
        documents = SimpleDirectoryReader(input_dir="./data/source_files").load_data(show_progress=True)
else:
    rag_dataset, documents = download_llama_dataset("DocugamiKgRagSec10Q", "./data")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
