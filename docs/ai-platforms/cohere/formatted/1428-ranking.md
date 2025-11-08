---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Ranking

In order to effectively combine the results from our vector and BM25 retrieval, we can use Cohere's Rerank 3 model through the inference API to provide a final, more precise, semantic reranking of our results.

First, create an inference endpoint with your Cohere API key. Make sure to specify a name for your endpoint, and the model\_id of one of the rerank models. In this example we will use Rerank 3.
```python PYTHON
client.options(ignore_status=[404]).inference.delete_model(inference_id="cohere_rerank")

client.inference.put_model(
    task_type="rerank",
    inference_id="cohere_rerank",
    body={
        "service": "cohere",
        "service_settings":{
            "api_key": COHERE_API_KEY,
            "model_id": "rerank-english-v3.0"
           },
        "task_settings": {
            "top_n": 10,
        },
    }
)
```
You can now rerank your results using that inference endpoint. Here we will pass in the query we used for retrieval, along with the documents we just retrieved using hybrid search.

The inference service will respond with a list of documents in descending order of relevance. Each document has a corresponding index (reflecting to the order the documents were in when sent to the inference endpoint), and if the “return\_documents” task setting is True, then the document texts will be included as well.

In this case we will set the response to False and will reconstruct the input documents based on the index returned in the response.
```python PYTHON
response = client.inference.inference(
    inference_id="cohere_rerank",
    body={
        "query": query,
        "input": documents,
        "task_settings": {
            "return_documents": False
            }
        }
)

ranked_documents = []
for document in response.body["rerank"]:
  ranked_documents.append({
      "title": raw_documents[int(document["index"])]["_source"]["title"],
      "text": raw_documents[int(document["index"])]["_source"]["text"]
  })

for document in ranked_documents[0:10]:
  print(f"Title: {document['title']}\nText: {document['text']}\n")
```
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
    model='command-a-03-2025'
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
  if document['id'] in source_documents:
    print(f"{document['title']}: {document['text']}")
```
And there you have it! A quick and easy implementation of hybrid search and RAG with Cohere and Elastic.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
