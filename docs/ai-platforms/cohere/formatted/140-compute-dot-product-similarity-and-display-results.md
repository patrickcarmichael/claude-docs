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

retrieved_documents = [documents[item] for item in max_idx]

for rank, idx in enumerate(max_idx):
    print(f"Rank: {rank+1}")
    print(f"Score: {scores[idx]}")
    print(f"Document: {retrieved_documents[rank]}\n")
```
```mdx
Rank: 1
Score: 0.32653470360872655
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}

Rank: 2
Score: 0.26851855352264786
Document: {'data': {'text': 'Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead.'}}

Rank: 3
Score: 0.2581341975304149
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}

Rank: 4
Score: 0.18633336738178463
Document: {'data': {'text': "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee."}}

Rank: 5
Score: 0.13022396595682814
Document: {'data': {'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'}}
```
>   **📝 Note**
>
> For simplicity, in this example, we are assuming only one query being generated. For practical implementations, multiple queries may be generated. For those scenarios, you will need to perform retrieval for each query.

### Reranking with Rerank

Reranking can boost the results from semantic or lexical search further. The [Rerank endpoint](https://docs.cohere.com/reference/rerank) takes a list of search results and reranks them according to the most relevant documents to a query. This requires just a single line of code to implement.

We call the endpoint using `co.rerank()` and pass the following arguments:

* `query`: The user query
* `documents`: The list of documents we get from the semantic search results
* `top_n`: The top reranked documents to select
* `model`: We choose Rerank English 3

Looking at the results, we see that since the query is about getting to know the team, the document that talks about joining Slack channels is now ranked higher (1st) compared to earlier (3rd).

Here we select `top_n` to be 2, which will be the documents we will pass next for response generation.

<CodeBlocks>
```python PYTHON
  # Rerank the documents

  results = co.rerank(
      model="rerank-v3.5",
      query=search_queries[0],
      documents=[doc["data"]["text"] for doc in retrieved_documents],
      top_n=2,
  )

  # Display the reranking results

  for idx, result in enumerate(results.results):
      print(f"Rank: {idx+1}")
      print(f"Score: {result.relevance_score}")
      print(f"Document: {retrieved_documents[result.index]}\n")

  reranked_documents = [
      retrieved_documents[result.index] for result in results.results
  ]
```
```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/rerank' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "rerank-v3.5",
    "query": "how to get to know your teammates",
    "top_n": 2,
    "documents": [
      "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!",
      "Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead.",
      "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.",
      "Finding Coffee Spots: For your caffeine fix, head to the break room'\''s coffee machine or cross the street to the café for artisan coffee.",
      "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    ]
  }'
```
</CodeBlocks>
```mdx
Rank: 1
Score: 0.07272241
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}

Rank: 2
Score: 0.058674112
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
