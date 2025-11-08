---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate search queries (if any)

import json

search_queries = []

res = co.chat(
    model="command-a-03-2025",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": message},
    ],
    tools=query_gen_tool,
)

if res.message.tool_calls:
    for tc in res.message.tool_calls:
        queries = json.loads(tc.function.arguments)["queries"]
        search_queries.extend(queries)

print(search_queries)
```
```bash cURL
curl --request POST \
  --url https://api.cohere.ai/v2/chat \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --header "Authorization: bearer $CO_API_KEY" \
  --data '{
    "model": "command-a-03-2025",
    "messages": [
      {
        "role": "system",
        "content": "Write a search query that will find helpful information for answering the user'\''s question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."
      },
      {
        "role": "user",
        "content": "Who is more popular: Nsync or Backstreet Boys?"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "internet_search",
          "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
          "parameters": {
            "type": "object",
            "properties": {
              "queries": {
                "type": "array",
                "items": {"type": "string"},
                "description": "a list of queries to search the internet with."
              }
            },
            "required": ["queries"]
          }
        }
      }
    ]
  }'
```
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
