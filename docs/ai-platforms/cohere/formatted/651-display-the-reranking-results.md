---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display the reranking results

def return_results(results, documents):
    for idx, result in enumerate(results.results):
        print(f"Rank: {idx+1}")
        print(f"Score: {result.relevance_score}")
        print(f"Document: {documents[result.index]}\n")


return_results(results, faqs_short)
```
```
Rank: 1
Score: 0.01798621
Document: {'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'}

Rank: 2
Score: 8.463939e-06
Document: {'text': 'Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year.'}
```
Further reading:

* [Rerank endpoint API reference](https://docs.cohere.com/reference/rerank)
* [Documentation on Rerank](https://docs.cohere.com/docs/rerank-overview)
* [Documentation on Rerank fine-tuning](https://docs.cohere.com/docs/rerank-fine-tuning)
* [Documentation on Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices)
* [LLM University module on Text Representation](https://cohere.com/llmu#text-representation)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
