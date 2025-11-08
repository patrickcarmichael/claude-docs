---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Delete the inference model if it already exists

client.options(ignore_status=[404]).inference.delete(
    inference_id="cohere_embeddings"
)

client.inference.put(
    task_type="text_embedding",
    inference_id="cohere_embeddings",
    body={
        "service": "cohere",
        "service_settings": {
            "api_key": COHERE_API_KEY,
            "model_id": "embed-v4.0",
            "embedding_type": "int8",
            "similarity": "cosine",
        },
        "task_settings": {},
    },
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
