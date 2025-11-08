---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print the final citations

citations = docs[-1].metadata["citations"]
print("Citations:")
print(citations)
```

### Using LangChain on Private Deployments

You can use LangChain with privately deployed Cohere models. To use it, specify your model deployment URL in the `base_url` parameter.
```python PYTHON
llm = CohereRerank(
    base_url="<YOUR_DEPLOYMENT_URL>",
    cohere_api_key="COHERE_API_KEY",
    model="MODEL_NAME",
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
