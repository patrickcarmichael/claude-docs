---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Perform a near_text search with reranking for documents related to "property contracts and zoning regulations"

rerank_response = collection.query.near_text(
    query=search_query,
    limit=3,
    rerank=Rerank(
        prop="description",  # Property to rerank based on (description in this case)

        query=search_query,  # Query to use for reranking

    ),
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
