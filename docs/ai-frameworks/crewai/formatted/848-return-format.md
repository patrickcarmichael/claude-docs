---
title: "Crewai: Return Format"
description: "Return Format section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Return Format


The tool returns results in JSON format:

```json  theme={null}
[
  {
    "metadata": {
      // Any metadata stored with the document
    },
    "context": "The actual text content of the document",
    "distance": 0.95  // Similarity score
  }
]
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Search Parameters](./847-search-parameters.md)

**Next:** [Default Embedding →](./849-default-embedding.md)
