---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Rerank

You can use this code to invoke our latest Rerank models on Bedrock
```python PYTHON
import cohere

co = cohere.BedrockClientV2(
    aws_region="us-west-2",  # pick a region where the model is available

    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
]

response = co.rerank(
    model="cohere.rerank-v3-5:0",
    query="What is the capital of the United States?",
    documents=docs,
    top_n=3,
)

print(response)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
