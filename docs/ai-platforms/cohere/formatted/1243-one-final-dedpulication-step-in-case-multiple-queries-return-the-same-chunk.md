---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## One final dedpulication step in case multiple queries return the same chunk

documents = [dict(t, id=f"doc_{i}") for i, t in enumerate({tuple(d.items()) for d in documents})]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
