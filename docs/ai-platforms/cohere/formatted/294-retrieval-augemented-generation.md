---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieval augemented generation

Now that we have ranked our results, we can easily turn this into a RAG system with Cohere's Chat API. Pass in the retrieved documents, along with the query and see the grounded response using Cohere's newest generative model Command R+.

First, we will create the Cohere client.
```python PYTHON 
co = cohere.Client(COHERE_API_KEY)
```
Next, we can easily get a grounded generation with citations from the Cohere Chat API. We simply pass in the user query and documents retrieved from Elastic to the API, and print out our grounded response.
```python PYTHON
response = co.chat(
    message=query,
    documents=ranked_documents,
    model="command-a-03-2025",
)

source_documents = []
for citation in response.citations:
    for document_id in citation.document_ids:
        if document_id not in source_documents:
            source_documents.append(document_id)

print(f"Query: {query}")
print(f"Response: {response.text}")
print("Sources:")
for document in response.documents:
    if document["id"] in source_documents:
        print(f"{document['title']}: {document['text']}")
```
And there you have it! A quick and easy implementation of hybrid search and RAG with Cohere and Elastic.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
