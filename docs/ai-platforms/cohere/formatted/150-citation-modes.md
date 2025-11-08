---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Citation modes

When running RAG in streaming mode, it’s possible to configure how citations are generated and presented. You can choose between fast citations or accurate citations, depending on your latency and precision needs.

### Accurate citations

The model produces its answer first, and then, after the entire response is generated, it provides citations that map to specific segments of the response text. This approach may incur slightly higher latency, but it ensures the citation indices are more precisely aligned with the final text segments of the model’s answer.

This is the default option, or you can explicitly specify it by adding the `citation_options={"mode": "accurate"}` argument in the API call.

Here is an example using the same list of pre-defined `messages` as the above.

With the `citation_options` mode set to `accurate`, we get the citations after the entire response is generated.

<CodeBlocks>
```python PYTHON
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

  messages = [
      {"role": "user", "content": "Where do the tallest penguins live?"}
  ]

  response = co.chat_stream(
      model="command-a-03-2025",
      messages=messages,
      documents=documents,
      citation_options={"mode": "accurate"},
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

  print("\n")
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
    ],
    "citation_options": {
      "mode": "accurate"
    },
    "stream": true
  }'
```
</CodeBlocks>

Example response:
```mdx wordWrap
The tallest penguins are the Emperor penguins. They live in Antarctica.

start=29 end=46 text='Emperor penguins.' sources=[DocumentSource(type='document', id='100', document={'id': '100', 'snippet': 'Emperor penguins are the tallest.', 'title': 'Tall penguins'})] type='TEXT_CONTENT' 

start=60 end=71 text='Antarctica.' sources=[DocumentSource(type='document', id='101', document={'id': '101', 'snippet': 'Emperor penguins only live in Antarctica.', 'title': 'Penguin habitats'})] type='TEXT_CONTENT' 
```

### Fast citations

The model generates citations inline, as the response is being produced. In streaming mode, you will see citations injected at the exact moment the model uses a particular piece of external context. This approach provides immediate traceability at the expense of slightly less precision in citation relevance.

You can specify it by adding the `citation_options={"mode": "fast"}` argument in the API call.

With the `citation_options` mode set to `fast`, we get the citations inline as the model generates the response.

<CodeBlocks>
```python PYTHON
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

  messages = [
      {"role": "user", "content": "Where do the tallest penguins live?"}
  ]

  response = co.chat_stream(
      model="command-a-03-2025",
      messages=messages,
      documents=documents,
      citation_options={"mode": "fast"},
  )

  response_text = ""
  for chunk in response:
      if chunk:
          if chunk.type == "content-delta":
              response_text += chunk.delta.message.content.text
              print(chunk.delta.message.content.text, end="")
          if chunk.type == "citation-start":
              print(
                  f" [{chunk.delta.message.citations.sources[0].id}]",
                  end="",
              )
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
    ],
    "citation_options": {
      "mode": "fast"
    },
    "stream": true
  }'
```
</CodeBlocks>

Example response:
```mdx wordWrap
The tallest penguins [100] are the Emperor penguins [100] which only live in Antarctica. [101]
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
