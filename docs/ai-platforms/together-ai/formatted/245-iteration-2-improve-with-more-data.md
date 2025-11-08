---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Iteration 2: Improve with more data

improved_job = client.fine_tuning.create(
    model="togethercomputer/llama-2-7b-chat",
    from_hf_model="your-username/model-v1",  # Use previous result

    training_file="expanded-dataset-id",  # More/better data

    suffix="v2",
    n_epochs=2,  # Fewer epochs for fine-tuning

    learning_rate=5e-6,  # Lower learning rate

)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
