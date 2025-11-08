---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed + Rerank + Command

Finally, we'll add Command into the mix. This handles imports and creates a fresh `"Legal_Docs"` in the Weaviate database.
```python PYTHON
from weaviate.classes.config import Configure
from weaviate.classes.generate import GenerativeConfig

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
