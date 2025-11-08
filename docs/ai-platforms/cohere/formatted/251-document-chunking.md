---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Document Chunking

Under the hood, the Rerank API turns user input into text chunks. Every chunk will include the `query` and a portion of the document text. Chunk size depends on the model.

For example, if

* the selected model is `rerank-v3.5`, which has context length (aka max chunk size) of 4096 tokens
* the query is 100 tokens
* there is one document and it is 10,000 tokens long
* document truncation is disabled by setting `max_tokens_per_doc` parameter to 10,000 tokens

Then the document will be broken into the following three chunks:
```
relevance_score_1 = <padding_tokens, query[0,99], document[0,3992]>
relevance_score_2 = <padding_tokens, query[0,99], document[3993,7985]>
relevance_score_3 = <padding_tokens, query[0,99], document[7986,9999]>
```
And the final relevance score for that document will be computed as the highest score among those chunks:
```python
relevance_score = max(
    relevance_score_1, relevance_score_2, relevance_score_3
)
```
If you would like more control over how chunking is done, we recommend that you chunk your documents yourself.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
