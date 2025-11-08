---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Compute dot product similarity and display results

n = 5
scores = np.dot(query_emb, np.transpose(doc_emb))[0]
max_idx = np.argsort(-scores)[:n]

retrieved_documents = [faqs_long[item] for item in max_idx]

for rank, idx in enumerate(max_idx):
    print(f"Rank: {rank+1}")
    print(f"Score: {scores[idx]}")
    print(f"Document: {retrieved_documents[rank]}\n")
```
```
Rank: 1
Score: 0.34212792245283796
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}

Rank: 2
Score: 0.2883222063024371
Document: {'data': {'text': 'Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead.'}}

Rank: 3
Score: 0.278128283997032
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}

Rank: 4
Score: 0.19474858706643985
Document: {'data': {'text': "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee."}}

Rank: 5
Score: 0.13713692506528824
Document: {'data': {'text': 'Side Projects Policy: We encourage you to pursue your passions. Just be mindful of any potential conflicts of interest with our business.'}}
```
Reranking can boost the results from semantic or lexical search further. The Rerank endpoint takes a list of search results and reranks them according to the most relevant documents to a query. This requires just a single line of code to implement.

We call the endpoint using `co.rerank()` and pass the following arguments:

* `query`: The user query
* `documents`: The list of documents we get from the semantic search results
* `top_n`: The top reranked documents to select
* `model`: We choose Rerank English 3

Looking at the results, we see that the given a query about getting to know the team, the document that talks about joining Slack channels is now ranked higher (1st) compared to earlier (3rd).

Here we select `top_n` to be 2, which will be the documents we will pass next for response generation.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
