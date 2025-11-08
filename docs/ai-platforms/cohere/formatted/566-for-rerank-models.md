---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## For Rerank models

co_rerank = cohere.Client(
    api_key="AZURE_INFERENCE_CREDENTIAL",
    base_url="AZURE_MODEL_ENDPOINT",  # Example - https://cohere-rerank-v3-multilingual-xyz.eastus.models.ai.azure.com/

)
```

### Chat

```python PYTHON
message = "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates."

response = co_chat.chat(message=message)

print(response)
```

### RAG

```python PYTHON
faqs_short = [
    {
        "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
    },
    {
        "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    },
]

query = "Are there fitness-related perks?"

response = co_chat.chat(message=query, documents=faqs_short)

print(response)
```

### Embed

```python PYTHON
docs = [
    "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.",
    "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee.",
]

doc_emb = co_embed.embed(
    input_type="search_document",
    texts=docs,
).embeddings
```

### Rerank

```python PYTHON
faqs_short = [
    {
        "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
    },
    {
        "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
    },
    {
        "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    },
]

query = "Are there fitness-related perks?"

results = co_rerank.rerank(
    query=query,
    documents=faqs_short,
    top_n=2,
    model="rerank-english-v3.0",
)
```typescript
Here are some other examples for [Command](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/cohere/cohere-cmdR.ipynb) and [Embed](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/cohere/cohere-embed.ipynb).

The important thing to understand is that our new and existing customers can call the models from Azure while still leveraging their integration with the Cohere SDK.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
