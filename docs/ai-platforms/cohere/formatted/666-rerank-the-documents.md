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
    documents=faqs,
    top_n=1,
)

return_results(results, faqs)
```
```
Rank: 1
Score: 0.42232594
Document: {'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'}

Rank: 2
Score: 0.00025118678
Document: {'text': 'Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year.'}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
