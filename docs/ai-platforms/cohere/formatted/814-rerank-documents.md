---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank documents

Adding a reranking component is simple with Cohere Rerank. It takes just one line of code to implement.

Calling the Rerank endpoint requires the following arguments:

* `documents`: The list of documents, which we defined in the previous section
* `query`: The user query; we’ll use 'What emails have been about refunds?' as an example
* `top_n`:  The number of documents we want to be returned, sorted from the most to the least relevant document

When passing documents that contain multiple fields like in this case, for best performance we recommend formatting them as YAML strings.
```python PYTHON
import yaml

yaml_docs = [yaml.dump(doc, sort_keys=False) for doc in documents]

query = "What emails have been about refunds?"

results = co.rerank(
    model="model",  # Pass a dummy string

    documents=yaml_docs,
    query=query,
    top_n=3,
)
```
Since we set `top_n=3`, the response will return the three documents most relevant to our query. Each result includes both the document's original position (index) in our input list and a score indicating how well it matches the query.

Let's examine the reranked results below.
```python PYTHON
def return_results(results, documents):
    for idx, result in enumerate(results.results):
        print(f"Rank: {idx+1}")
        print(f"Score: {result.relevance_score}")
        print(f"Document: {documents[result.index]}\n")


return_results(results, documents)
```
```mdx
Rank: 1
Score: 8.547617e-05
Document: {'Title': 'Return Defective Product', 'Content': 'Hello, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.'}

Rank: 2
Score: 5.1442214e-05
Document: {'Title': 'Questions about Return Policy', 'Content': 'Hello, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.'}

Rank: 3
Score: 3.591301e-05
Document: {'Title': 'Return Policy for Defective Product', 'Content': 'Hi, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.'}
```
The search query was looking for emails about refunds. But none of the documents mention the word “refunds” specifically.

However, the Rerank model was able to retrieve the right documents. Some of the documents mentioned the word “return”, which has a very similar meaning to "refunds."

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
