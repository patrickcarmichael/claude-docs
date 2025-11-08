---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Upload to Fireworks

dataset = Dataset.from_file(dataset_filename)
dataset.sync()
```

### SFT Training Configuration

**Supervised Fine-Tuning Job**:

* **Model**: `Qwen2.5 7B`
* **Dataset**: dataset (Your uploaded dataset)
* **Epochs**: 5-8 (format learning needs repetition)
* **Learning Rate**: 1e-5

**Critical Parameters for Format Learning**:

* **Higher Learning Rate**: Needed to override existing response patterns
* **More Epochs**: Format internalization requires repetition
* **Larger Model**: 3B+ has capacity to learn complex structural patterns
* **No System Prompts in Training**: Teaches default behavior, not instruction-following

### Running the SFT Training Job

```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
