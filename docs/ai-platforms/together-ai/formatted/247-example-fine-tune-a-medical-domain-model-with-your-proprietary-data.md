---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example: Fine-tune a medical domain model with your proprietary data

client.fine_tuning.create(
    model="Qwen/Qwen3-4B",  # Base architecture it's built on

    from_hf_model="community/medical-Qwen3-4B",  # Specialized variant

    training_file="your-medical-data",
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
