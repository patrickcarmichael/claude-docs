---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## construct a search index from the schema - this schema is called "semantic_search_demo"

schema = IndexSchema.from_yaml("./schema.yaml")
client = Redis.from_url("redis://localhost:6379")
index = SearchIndex(schema, client)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
