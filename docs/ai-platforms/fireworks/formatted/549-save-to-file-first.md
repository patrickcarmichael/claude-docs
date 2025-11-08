---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Save to file first

dataset_filename = "kd_sft_dataset.jsonl"
with open(dataset_filename, 'w') as f:
    for example in sft_training_data:
        f.write(json.dumps(example) + '\n')

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
