---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display the reranking results

for idx, result in enumerate(results.results):
    print(f"Rank: {idx+1}")
    print(f"Score: {result.relevance_score}")
    print(f"Document: {retrieved_documents[result.index]}\n")

reranked_documents = [
    retrieved_documents[result.index] for result in results.results
]
```
```
Rank: 1
Score: 0.0020507434
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}

Rank: 2
Score: 0.0014158706
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}
```
Finally we reach the step that we saw in the earlier "Basic RAG" section.

To call the Chat API with RAG, we pass the following parameters. This tells the model to run in RAG-mode and use these documents in its response.

* `model` for the model ID
* `messages` for the user's query.
* `documents` for defining the documents.

The response is then generated based on the the query and the documents retrieved.

RAG introduces additional objects in the Chat response. One of them is `citations`, which contains details about:

* specific text spans from the retrieved documents on which the response is grounded.
* the documents referenced in the citations.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
