---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Iteration 3: Specialized fine-tuning

specialized_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="your-username/model-v2",
    training_file="specialized-task-dataset",
    suffix="specialized-v3",
    n_epochs=1,
    learning_rate=1e-6,
)
```

### Continuing Training from a Previous Fine-tune

Resume training from a checkpoint you previously created to add more data or continue the adaptation process:
```python
client.fine_tuning.create(
    model="google/gemma-3-4b-it",
    from_hf_model="your-username/previous-finetune-v1",
    training_file="new-training-data",
    n_epochs=2,  # Additional training epochs

)
```

### Fine-tuning a Community Specialist Model

Leverage community models that have already been optimized for specific domains:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
