---
title: "Langgraph: Find memories about food preferences"
description: "Find memories about food preferences section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Find memories about food preferences

# (This can be done after putting memories into the store)
memories = store.search(
    namespace_for_memory,
    query="What does the user like to eat?",
    limit=3  # Return top 3 matches
)
```

You can control which parts of your memories get embedded by configuring the `fields` parameter or by specifying the `index` parameter when storing memories:

```python

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Memory Store](./440-memory-store.md)

**Next:** [Store with specific fields to embed →](./442-store-with-specific-fields-to-embed.md)
