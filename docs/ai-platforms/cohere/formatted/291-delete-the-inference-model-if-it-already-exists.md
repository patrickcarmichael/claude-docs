---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Delete the inference model if it already exists

client.options(ignore_status=[404]).inference.delete(inference_id="cohere_rerank")

client.inference.put(
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

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
