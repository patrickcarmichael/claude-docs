---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the Cohere LLM

llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

chain = load_summarize_chain(llm, chain_type="stuff")

chain.invoke({"input_documents": docs})
```

### Using LangChain on Private Deployments

You can use LangChain with privately deployed Cohere models. To use it, specify your model deployment URL in the `base_url` parameter.
```python PYTHON
llm = ChatCohere(
    base_url="<YOUR_DEPLOYMENT_URL>",
    cohere_api_key="COHERE_API_KEY",
    model="MODEL_NAME",
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
