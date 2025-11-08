---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Perform a near_text semantic search for documents

response = collection.query.near_text(
    query=search_query,  # Search query

    limit=3,                  # Limit the number of results to 3

    return_metadata=MetadataQuery(distance=True)  # Include distance metadata in the results

)

print("Semantic Search")
print("*" * 50)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
