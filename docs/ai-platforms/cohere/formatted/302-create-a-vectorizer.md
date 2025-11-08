---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## create a vectorizer

api_key = "{Insert your cohere API Key}"

cohere_vectorizer = CohereTextVectorizer(
    model="embed-english-v3.0",
    api_config={"api_key": api_key},
)
```
Create a `CohereTextVectorizer` by specifying the embedding model and your api key.

The following [link](/docs/embed-2) contains details around the available embedding models from Cohere and their respective dimensions.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
