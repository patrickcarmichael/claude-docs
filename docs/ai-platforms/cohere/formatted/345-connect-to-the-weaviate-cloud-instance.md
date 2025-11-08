---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Connect to the Weaviate cloud instance

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,  # `weaviate_url`: your Weaviate URL

    auth_credentials=Auth.api_key(
        weaviate_key
    ),  # `weaviate_key`: your Weaviate API key

    headers=headers,  # Include the Cohere API key in the headers

)
```
And here we'll create a `"Legal_Docs"` collection in the Weaviate database:
```python PYTHON
from weaviate.classes.config import Configure, Property, DataType

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
