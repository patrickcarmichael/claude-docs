---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Replace the profile name with the one created in the setup.

embeddings = BedrockEmbeddings(
    credentials_profile_name="{PROFILE-NAME}",
    region_name="us-east-1",
    model_id="cohere.embed-english-v3",
)

embeddings.embed_query("This is a content of the document")
```

### Using LangChain on Private Deployments

You can use LangChain with privately deployed Cohere models. To use it, specify your model deployment URL in the `base_url` parameter.
```python PYTHON
llm = CohereEmbeddings(
    base_url="<YOUR_DEPLOYMENT_URL>",
    cohere_api_key="COHERE_API_KEY",
    model="MODEL_NAME",
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
