---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create the inference endpoint

Let's create the inference endpoint by using the [Create inference API](https://www.elastic.co/guide/en/elasticsearch/reference/current/put-inference-api.html).

You'll need an Cohere API key for this that you can find in your Cohere account under the [API keys section](https://dashboard.cohere.com/api-keys). A production key is required to complete the steps in this notebook as the Cohere free trial API usage is limited.
```python PYTHON
COHERE_API_KEY = getpass("Enter Cohere API key:  ")

client.options(ignore_status=[404]).inference.delete_model(inference_id="cohere_embeddings")

client.inference.put_model(
    task_type="text_embedding",
    inference_id="cohere_embeddings",
    body={
        "service": "cohere",
        "service_settings": {
            "api_key": COHERE_API_KEY,
            "model_id": "embed-v4.0",
            "embedding_type": "int8",
            "similarity": "cosine"
        },
        "task_settings": {},
    },
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
