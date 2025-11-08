---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Perform a near_text search for documents related to "policies related to drug compounding"

response = collection.query.near_text(
    query="policies related to drug compounding",  # Search query

    limit=2,  # Limit the number of results to 2

    return_metadata=MetadataQuery(
        distance=True
    ),  # Include distance metadata in the results

)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
