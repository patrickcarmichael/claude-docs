---
title: "Langgraph: Store with specific fields to embed"
description: "Store with specific fields to embed section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Store with specific fields to embed

store.put(
    namespace_for_memory,
    str(uuid.uuid4()),
    {
        "food_preference": "I love Italian cuisine",
        "context": "Discussing dinner plans"
    },
    index=["food_preference"]  # Only embed "food_preferences" field
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Find memories about food preferences](./441-find-memories-about-food-preferences.md)

**Next:** [Store without embedding (still retrievable, but not searchable) →](./443-store-without-embedding-still-retrievable-but-not-.md)
