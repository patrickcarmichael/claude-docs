---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Invoke the model and print the response

result = co.embed(
    model=model_id,
    input_type=input_type,
    texts=texts,
    truncate=truncate,
)  # aws_client.invoke_model(**params)

print(result)
```
Note that we've released multimodal embeddings models that are able to handle images in addition to text. Find [more information here](https://docs.cohere.com/docs/multimodal-embeddings).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
