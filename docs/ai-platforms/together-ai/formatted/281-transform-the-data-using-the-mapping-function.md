---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Transform the data using the mapping function

train_messages = coqa_dataset["train"].map(
    map_fields,
    remove_columns=coqa_dataset["train"].column_names,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
