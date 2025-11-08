---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Take the original search results and filter the top\_n results ("Engine B")

In this section, we'll implement our second retrieval approach as a baseline comparison. For "Engine B", we'll simply take the original Wikipedia search results without any reranking and select the top-n results.

This approach reflects how many traditional search engines work - returning results based on their original relevance score from the data source. By comparing this baseline against our reranked approach (Engine A), we can evaluate whether reranking provides meaningful improvements in result quality.

We'll use the same number of results (top\_n) as Engine A to ensure a fair comparison in our evaluation.
```python PYTHON
results_top_n = []

for item in results:
    results_top_n.append({
        "question": item["question"],
        "search_results": item["search_results"][:top_n]
    })
    

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
