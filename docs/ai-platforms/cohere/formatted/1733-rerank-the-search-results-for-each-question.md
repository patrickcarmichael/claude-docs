---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank the search results for each question

top_n = 3
results_reranked_top_n = []

for item in results:
    question = item["question"]
    documents = item["search_results"]
    
    # Rerank the documents using Cohere

    reranked = co.rerank(
        model="rerank-v3.5",
        query=question,
        documents=documents,
        top_n=top_n  # Get top 3 results

    )
    
    # Format the reranked results

    top_results = []
    for result in reranked.results:
        top_results.append(documents[result.index])
    
    # Add to the reranked results list

    results_reranked_top_n.append({
        "question": question,
        "search_results": top_results
    })

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
