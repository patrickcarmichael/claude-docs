---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 1: Generating search queries

Next, we create a search query generation tool for generating search queries from user queries.

We pass a user query, which in this example, asks about how to get to know the team.

<CodeBlocks>
```python PYTHON
  message = "How to get to know my teammates"

  # Define the query generation tool

  query_gen_tool = [
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
                          "description": "a list of queries to search the internet with.",
                      }
                  },
                  "required": ["queries"],
              },
          },
      }
  ]

  # Define a system message to optimize search query generation

  instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."

  # Generate search queries (if any)

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
    --url 'https://api.cohere.ai/v2/chat' \
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
        "content": "I'\''m joining a new team as a Principal Analyst. What are the best ways to quickly get to know my teammates?"
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
                "items": {
                  "type": "string"
                },
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
</CodeBlocks>

Example response:
```mdx
['how to get to know your teammates']
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
