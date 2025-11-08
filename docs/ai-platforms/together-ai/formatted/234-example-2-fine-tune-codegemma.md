---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example 2: Fine-tune CodeGemma

client.fine_tuning.create(
    model="google/gemma-3-4b-it",
    from_hf_model="google/codegemma-7b-it",  # Code-specialized

    training_file="code-instruction-dataset",
    learning_rate=1e-5,
)
```

### End-to-End Workflow Examples

**Complete Domain Adaptation Workflow**
```python
from together import Together
import json

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
