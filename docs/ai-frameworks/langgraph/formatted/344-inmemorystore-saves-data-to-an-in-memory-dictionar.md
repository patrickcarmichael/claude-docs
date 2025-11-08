---
title: "Langgraph: InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use."
description: "InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.

store = InMemoryStore(index={"embed": embed, "dims": 2})
user_id = "my-user"
application_context = "chitchat"
namespace = (user_id, application_context)
store.put(
    namespace,
    "a-memory",
    {
        "rules": [
            "User likes short, direct language",
            "User only speaks English & python",
        ],
        "my-key": "my-value",
    },
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Node that updates instructions](./343-node-that-updates-instructions.md)

**Next:** [get the "memory" by ID →](./345-get-the-memory-by-id.md)
