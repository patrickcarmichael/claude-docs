---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quickstart

### 1. Get your Together API key

First, [register for an account](https://api.together.ai/settings/api-keys?utm_source=docs\&utm_medium=quickstart\&utm_campaign=salesforce-llamarank) to get an API key.

Once you've registered, set your account's API key to an environment variable named `TOGETHER_API_KEY`:
```sh
export TOGETHER_API_KEY=xxxxx
```

### 2. Install your preferred library

Together provides an official library for Python:
```sh
pip install together --upgrade
```
As well as an official library for TypeScript/JavaScript:
```sh
npm install together-ai
```
You can also call our HTTP API directly using any language you like.

### 3. Run your first reranking query against LlamaRank

In the example below, we use the Rerank API endpoint to index the list of `documents` from most to least relevant to the query `What animals can I find near Peru?`.
```py
from together import Together

client = Together()

query = "What animals can I find near Peru?"

documents = [
    "The giant panda (Ailuropoda melanoleuca), also known as the panda bear or simply panda, is a bear species endemic to China.",
    "The llama is a domesticated South American camelid, widely used as a meat and pack animal by Andean cultures since the pre-Columbian era.",
    "The wild Bactrian camel (Camelus ferus) is an endangered species of camel endemic to Northwest China and southwestern Mongolia.",
    "The guanaco is a camelid native to South America, closely related to the llama. Guanacos are one of two wild South American camelids; the other species is the vicuña, which lives at higher elevations.",
]

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=documents,
    top_n=2,
)

for result in response.results:
    print(f"Document Index: {result.index}")
    print(f"Document: {documents[result.index]}")
    print(f"Relevance Score: {result.relevance_score}")
```
In the example above, the documents being passed in are a list of strings, but Together's Rerank API also supports JSON data.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
