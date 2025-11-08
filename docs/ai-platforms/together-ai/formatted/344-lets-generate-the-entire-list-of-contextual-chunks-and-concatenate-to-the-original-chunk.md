---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Let's generate the entire list of contextual chunks and concatenate to the original chunk

contextual_chunks = [
    generate_context(prompts[i]) + " " + chunks[i] for i in range(len(chunks))
]
```

Now we can embed each chunk into a vector index.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
