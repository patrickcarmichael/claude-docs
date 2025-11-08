---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Add the user message

message = "Where do the tallest penguins live?"

messages = [{"role": "user", "content": message}]

response = co.chat(
    model="command-a-03-2025",
    messages=messages,
    documents=documents,
)

print(response.message.content[0].text)

print(response.message.citations)
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
        "role": "user",
        "content": "Where do the tallest penguins live?"
      }
    ],
    "documents": [
      {
        "data": {
          "title": "Tall penguins",
          "snippet": "Emperor penguins are the tallest."
        }
      },
      {
        "data": {
          "title": "Penguin habitats",
          "snippet": "Emperor penguins only live in Antarctica."
        }
      },
      {
        "data": {
          "title": "What are animals?",
          "snippet": "Animals are different from plants."
        }
      }
    ]
  }'
```
The resulting generation is`"The tallest penguins are emperor penguins, which live in Antarctica."`. The model was able to combine partial information from multiple sources and ignore irrelevant documents to arrive at the full answer.

Nice :penguin:❄️!

Example response:
```mdx

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
