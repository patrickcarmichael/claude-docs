---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create dataset from a list of examples

examples = [
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"},
            {"role": "assistant", "content": "Paris."}
        ]
    }
]
dataset = Dataset.from_list(examples)
```

### `from_file()`

```python
@classmethod
from_file(path: str)
```
Creates a Dataset from a local JSONL file. The file should contain training examples in OpenAI's chat completion format.
```python
from fireworks import Dataset

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
