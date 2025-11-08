---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank the documents

results = co.rerank(
    model="rerank-v3.5",
    query=query,
    documents=yaml_docs,
    top_n=1,
)
return_results(results, employees)
```
```
Rank: 1
Score: 0.986828
Document: {'name': 'Emma Williams', 'role': 'Product Designer', 'join_date': '2024-06-15', 'email': 'emma@co1t.com', 'status': 'Full-time'}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
