---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Interpreting Results

The most important output from the [Rerank API endpoint](/reference/rerank-1) is the absolute rank exposed in the response object. The score is query dependent, and could be higher or lower depending on the query and passages sent in. In the example below, what matters is that Ottawa is more relevant than Toronto, but the user should not assume that Ottawa is two times more relevant than Ontario.
```
[
	RerankResult<text: Ottawa, index: 1, relevance_score: 0.9109375>,
	RerankResult<text: Toronto, index: 2, relevance_score: 0.7128906>,
	RerankResult<text: Ontario, index: 3, relevance_score: 0.04421997>
]
```
Relevance scores are normalized to be in the range `[0, 1]`. Scores close to `1` indicate a high relevance to the query, and scores closer to `0` indicate low relevance. To find a threshold on the scores to determine whether a document is relevant or not, we recommend going through the following process:

* Select a set of 30-50 representative queries `Q=[q_0, … q_n]` from your domain.
* For each query provide a document that is considered borderline relevant to the query for your specific use case, and create a list of (query, document) pairs: `sample_inputs=[(q_0, d_0), …, (q_n, d_n)]` .
* Pass all tuples in `sample_inputs` through the rerank endpoint in a loop, and gather relevance scores `sample_scores=[s0, ..., s_n]`.

The average of `sample_scores` can then be used as a reference when deciding a threshold for filtering out irrelevant documents.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
