---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display search results

for idx, docs_idx in enumerate(top_doc_idxs):
    print(f"Rank: {idx+1}")
    print(f"Document: {documents[docs_idx]}\n")
```
Here's a sample output:
```
Rank: 1
Document: COVID-19 symptoms can include: a high temperature or shivering (chills); a new, continuous cough; a loss or change to your sense of smell or taste; and many more

Rank: 2
Document: COVID-19 is a disease caused by a virus. The most common symptoms are fever, chills, and sore throat, but there are a range of others.

Rank: 3
Document: COVID-19 has the following symptom: Experiencing memory loss, poor judgment, and confusion.

Rank: 4
Document: COVID-19 has many symptoms.

Rank: 5
Document: COVID-19 symptoms are not nice
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
