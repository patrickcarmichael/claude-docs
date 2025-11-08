---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Client initial state:

{
    "0": "This is the first sentence",
    "1": "This is the second sentence",
}
```

When the server sends the next updates to the transcription, the client updates the state dictionary based on the segment `id`:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
