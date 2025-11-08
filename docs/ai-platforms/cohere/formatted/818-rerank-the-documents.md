---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank the documents

results = co.rerank(
    model="model",  # Pass a dummy string

    query=query,
    documents=yaml_emails,
    top_n=2,
)

return_results(results, emails)
```
```mdx
Rank: 1
Score: 0.13477592
Document: {'from': 'john@co1t.com', 'to': 'david@co1t.com', 'date': '2024-06-24', 'subject': 'First Week Check-In', 'text': "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!"}

Rank: 2
Score: 0.0010083435
Document: {'from': 'it@co1t.com', 'to': 'david@co1t.com', 'date': '2024-06-24', 'subject': 'Setting Up Your IT Needs', 'text': 'Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.'}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
