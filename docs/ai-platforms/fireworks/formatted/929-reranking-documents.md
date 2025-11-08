---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reranking documents

Reranking models are used to rerank a list of documents based on a query. We only support reranking with the Qwen3 Reranker family of models:

* `fireworks/qwen3-reranker-8b` (\*available on serverless)
* `fireworks/qwen3-reranker-4b`
* `fireworks/qwen3-reranker-0p6b`

The reranking model takes a query and a list of documents as input and outputs the list of documents scored by relevance to the query.
```python
import requests

url = "https://api.fireworks.ai/inference/v1/rerank"

payload = {
      "model": "fireworks/qwen3-reranker-8b",
      "query": "What was the primary objective of the Apollo 10 mission?",
      "documents": [
        "The Apollo 10 mission was launched in May 1969 and served as a 'dress rehearsal' for the Apollo 11 lunar landing.",
        "The crew of Apollo 10 consisted of astronauts Thomas Stafford, John Young, and Eugene Cernan.",
        "The command module for Apollo 10 was nicknamed 'Charlie Brown' and the lunar module was called 'Snoopy', after characters from the Peanuts comics.",
        "The Apollo program was a series of NASA missions that successfully landed the first humans on the Moon and returned them safely to Earth."
      ],
      "top_n": 3,
      "return_documents": True
}

headers = {
    "Authorization": "Bearer <FIREWORKS_API_KEY>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
