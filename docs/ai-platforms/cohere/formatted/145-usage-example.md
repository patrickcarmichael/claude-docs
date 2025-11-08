---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage example

This section provides an example of handling streamed objects in the tool use response generation step.

### Setup

First, import the Cohere library and create a client.

<Tabs>
  <Tab title="Cohere platform">
```python PYTHON
    # ! pip install -U cohere

    import cohere

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

### Define documents

Next, define the documents to be passed to the endpoint.
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

### Streaming the response

We can now stream the response using the `chat_stream` endpoint.

The events are streamed as `chunk` objects. In the example below, we pick `content-delta` to display the text response and `citation-start` to display the citations.

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
