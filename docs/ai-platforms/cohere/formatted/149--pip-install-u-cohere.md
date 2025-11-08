---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## ! pip install -U cohere

import cohere
import json

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key here: https://dashboard.cohere.com/api-keys

documents = [
    {
        "data": {
            "title": "Tall penguins",
            "snippet": "Emperor penguins are the tallest.",
        },
        "id": "100",
    },
    {
        "data": {
            "title": "Penguin habitats",
            "snippet": "Emperor penguins only live in Antarctica.",
        },
        "id": "101",
    },
]
```
When document IDs are provided, the citation will refer to the documents using these IDs.

<CodeBlocks>
```python PYTHON
  messages = [
      {"role": "user", "content": "Where do the tallest penguins live?"}
  ]

  response = co.chat(
      model="command-a-03-2025",
      messages=messages,
      documents=documents,
  )

  print(response.message.content[0].text)
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
        },
        "id": "100"
      },
      {
        "data": {
          "title": "Penguin habitats",
          "snippet": "Emperor penguins only live in Antarctica."
        },
        "id": "101"
      }
    ]
  }'
```
</CodeBlocks>

Note the `id` fields in the citations, which refer to the IDs in the `document` object.

Example response:
```mdx wordWrap
The tallest penguins are the Emperor penguins, which only live in Antarctica.

start=29 end=45 text='Emperor penguins' sources=[DocumentSource(type='document', id='100', document={'id': '100', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})] type='TEXT_CONTENT' 

start=66 end=77 text='Antarctica.' sources=[DocumentSource(type='document', id='101', document={'id': '101', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})] type='TEXT_CONTENT' 
```
In contrast, here's an example citation when the IDs are not provided.

Example response:
```mdx wordWrap
The tallest penguins are the Emperor penguins, which only live in Antarctica.

start=29 end=45 text='Emperor penguins' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})] type='TEXT_CONTENT' 

start=66 end=77 text='Antarctica.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})] type='TEXT_CONTENT' 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
