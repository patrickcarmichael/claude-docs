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
    top_n=2,
)

return_results(results, emails)
```
```
Rank: 1
Score: 0.1979091
Document: {'from': 'john@co1t.com', 'to': 'david@co1t.com', 'date': '2024-06-24', 'subject': 'First Week Check-In', 'text': "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!"}

Rank: 2
Score: 9.535461e-05
Document: {'from': 'hr@co1t.com', 'to': 'david@co1t.com', 'date': '2024-06-24', 'subject': 'A Warm Welcome to Co1t!', 'text': "We are delighted to welcome you to the team! As you embark on your journey with us, you'll find attached an agenda to guide you through your first week."}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
