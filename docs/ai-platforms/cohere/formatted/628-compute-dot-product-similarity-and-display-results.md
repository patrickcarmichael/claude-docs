---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Compute dot product similarity and display results

def return_results(query_emb, doc_emb, documents):
    n = 2
    scores = np.dot(query_emb, np.transpose(doc_emb))[0]
    scores_sorted = sorted(
        enumerate(scores), key=lambda x: x[1], reverse=True
    )[:n]

    for idx, item in enumerate(scores_sorted):
        print(f"Rank: {idx+1}")
        print(f"Score: {item[1]}")
        print(f"Document: {documents[item[0]]}\n")


return_results(query_emb, doc_emb, documents)
```
```
Rank: 1
Score: 0.352135965228231
Document: {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}

Rank: 2
Score: 0.31995661889273097
Document: {'text': 'Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours.'}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
