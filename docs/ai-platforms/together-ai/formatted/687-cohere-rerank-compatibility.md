---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere Rerank compatibility

The Together Rerank endpoint is compatible with Cohere Rerank, making it easy to test out LlamaRank for your existing applications. Simply switch it out by updating the `URL`, `API key` and `model`.
```py
import cohere

co = cohere.Client(
    base_url="https://api.together.xyz/v1",
    api_key=TOGETHER_API_KEY,
)
docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment (the death penalty) has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
]
response = co.rerank(
    model="Salesforce/Llama-Rank-V1",
    query="What is the capital of the United States?",
    documents=docs,
    top_n=3,
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
