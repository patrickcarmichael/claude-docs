---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Use Llama Rank to Rerank Top 25 Movies

Treating the top 25 matching movies as good candidate matches, potentially with irrelevant false positives, that might have snuck in we want to have the reranker model look and rerank each based on similarity to the query.
```py
query = "super hero mystery action movie about bats"  # we keep the same query - can change if we want

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=top_25_sorted_titles,
    top_n=5,  # we only want the top 5 results

)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {top_25_sorted_titles[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")
```

This will give us a reranked list of movies as shown below:
```
Document Index: 12
Document: Batman Returns
Relevance Score: 0.35380946383813044

Document Index: 8
Document: Batman Begins
Relevance Score: 0.339339115127178

Document Index: 7
Document: Batman & Robin
Relevance Score: 0.33013392395016167

Document Index: 5
Document: Batman v Superman: Dawn of Justice
Relevance Score: 0.3289763252445171

Document Index: 9
Document: Super 8
Relevance Score: 0.258483721657576
```

Here we can see that that reranker was able to improve the list by demoting irrelevant movies like Watchmen, Predator, Despicable Me 2, Night at the Museum: Secret of the Tomb, Penguins of Madagascar, further down the list and promoting Batman Returns, Batman Begins, Batman & Robin, Batman v Superman: Dawn of Justice to the top of the list!

The `bge-base-en-v1.5` embedding model gives us a fuzzy match to concepts mentioned in the query, the Llama-Rank-V1 reranker then imrpoves the quality of our list further by spending more compute to resort the list of movies.

Learn more about how to use reranker models in the [docs here](/docs/rerank-overview) !

***


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
