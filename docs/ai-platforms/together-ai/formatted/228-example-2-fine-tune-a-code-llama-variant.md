---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 2: Fine-tune a Code Llama variant

client.fine_tuning.create(
    model="meta-llama/Llama-3-8b-chat-hf",
    from_hf_model="codellama/CodeLlama-7b-Instruct-hf",
    training_file="code-dataset-id",
    batch_size=2,  # Reduce for code models

    n_epochs=2,
)
```

**Qwen Family Models**
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
