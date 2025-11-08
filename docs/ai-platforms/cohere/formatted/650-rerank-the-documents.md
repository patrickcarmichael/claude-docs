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

print(results)
```
```
id='2fa5bc0d-28aa-4c99-8355-7de78dbf3c86' results=[RerankResponseResultsItem(document=None, index=2, relevance_score=0.01798621), RerankResponseResultsItem(document=None, index=3, relevance_score=8.463939e-06)] meta=ApiMeta(api_version=ApiMetaApiVersion(version='1', is_deprecated=None, is_experimental=None), billed_units=ApiMetaBilledUnits(input_tokens=None, output_tokens=None, search_units=1.0, classifications=None), tokens=None, warnings=None)
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
