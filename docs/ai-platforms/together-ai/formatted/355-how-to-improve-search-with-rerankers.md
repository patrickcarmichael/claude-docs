---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How To Improve Search With Rerankers

Source: https://docs.together.ai/docs/how-to-improve-search-with-rerankers

Learn how you can improve semantic search quality with reranker models!

In this guide we will use a reranker model to improve the results produced from a simple semantic search workflow. To get a better understanding of how semantic search works please refer to the [Cookbook here](https://github.com/togethercomputer/together-cookbook/blob/main/Semantic_Search.ipynb) .

A reranker model operates by looking at the query and the retrieved results from the semantic search pipeline one by one and assesses how relevant the returned result is to the query. Because the reranker model can spend compute assessing the query with the returned result at the same time it can better judge how relevant the words and meanings in the query are to individual documents. This also means that rerankers are computationally expensive and slower - thus they cannot be used to rank every document in our database.

We run a semantic search process to obtain a list of 15-25 candidate objects that are similar "enough" to the query and then use the reranker as a fine-toothed comb to pick the top 5-10 objects that are actually closest to our query.

We will be using the [Salesforce Llama Rank](/docs/rerank-overview) reranker model.

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ad1d5a26de9ede54c2151b0e4a4ac56d" alt="How to improve search with rerankers" data-og-width="3205" width="3205" data-og-height="961" height="961" data-path="images/how-to-improve-search-with-rerankers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=624f30da905533bd641cc0cd21159b26 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=de91cec6e273fc75ae8f6fdbb620b8a6 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=a4c24541eb84bb437675e2d213d2c173 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=cf0a5651d917416f9830077c0e3e02d6 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=811e20c89ea9cec15cc638a8c053da9a 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/how-to-improve-search-with-rerankers.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=059eaedb1926ebbefab0c0512cbd43a5 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
