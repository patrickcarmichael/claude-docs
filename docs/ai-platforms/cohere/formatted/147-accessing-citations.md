---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Accessing citations

The Chat endpoint generates fine-grained citations for its RAG response. This capability is included out-of-the-box with the Command family of models.

The following sections describe how to access the citations in both the non-streaming and streaming modes.

### Non-streaming

First, define the documents to be passed as the context of the model's response.

<Tabs>
  <Tab title="Cohere platform">
```python PYTHON
    # ! pip install -U cohere

    import cohere
    import json

    co = cohere.ClientV2(
        "COHERE_API_KEY"
    )  # Get your free API key here: https://dashboard.cohere.com/api-keys

```
  </Tab>

  <Tab title="Private deployment">
```python PYTHON
    # ! pip install -U cohere

    import cohere

    co = cohere.ClientV2(
        api_key="",  # Leave this blank

        base_url="<YOUR_DEPLOYMENT_URL>",
    )
```
  </Tab>
</Tabs>
```python PYTHON
documents = [
    {
        "data": {
            "title": "Tall penguins",
            "snippet": "Emperor penguins are the tallest.",
        }
    },
    {
        "data": {
            "title": "Penguin habitats",
            "snippet": "Emperor penguins only live in Antarctica.",
        }
    },
]
```
In the non-streaming mode (using `chat` to generate the model response), the citations are provided in the `message.citations` field of the response object.

Each citation object contains:

* `start` and `end`: the start and end indices of the text that cites a source(s)
* `text`: its corresponding span of text
* `sources`: the source(s) that it references

<CodeBlocks>
```python PYTHON
  messages = [
      {"role": "user", "content": "Where do the tallest penguins live?"}
  ]

  response = co.chat(
      model="command-r-08-2024",
      messages=messages,
      documents=documents,
  )

  print(response.message.content[0].text)

  for citation in response.message.citations:
      print(citation, "\n")
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "command-r-08-2024",
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
      }
    ]
  }'
```
</CodeBlocks>

Example response:
```mdx wordWrap
The tallest penguins are the Emperor penguins. They only live in Antarctica.

start=29 end=46 text='Emperor penguins.' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})] type='TEXT_CONTENT' 

start=65 end=76 text='Antarctica.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})] type='TEXT_CONTENT' 
```

### Streaming

In a streaming scenario (using `chat_stream` to generate the model response), the citations are provided in the `citation-start` events.

Each citation object contains the same fields as the [non-streaming scenario](#non-streaming).

<CodeBlocks>
```python PYTHON
  messages = [
      {"role": "user", "content": "Where do the tallest penguins live?"}
  ]

  response = co.chat_stream(
      model="command-a-03-2025",
      messages=messages,
      documents=documents,
  )

  response_text = ""
  citations = []
  for chunk in response:
      if chunk:
          if chunk.type == "content-delta":
              response_text += chunk.delta.message.content.text
              print(chunk.delta.message.content.text, end="")
          if chunk.type == "citation-start":
              citations.append(chunk.delta.message.citations)

  for citation in citations:
      print(citation, "\n")
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: text/event-stream' \
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
      }
    ],
    "stream": true
  }'
```
</CodeBlocks>

Example response:
```mdx wordWrap
The tallest penguins are the Emperor penguins, which only live in Antarctica.

start=29 end=45 text='Emperor penguins' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})] type='TEXT_CONTENT' 

start=66 end=77 text='Antarctica.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})] type='TEXT_CONTENT' 
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
