---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Check for bad states during training

try:
    job.raise_if_bad_state()
except RuntimeError as e:
    print(f"Training failed: {e}")
```

### Usage Example

```python
import time
from fireworks import LLM, Dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
