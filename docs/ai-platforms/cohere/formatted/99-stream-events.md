---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Stream Events

When streaming is enabled, the API sends events down one by one. Each event has a `type`. Events of different types need to be handled correctly.

The following is an example of printing the `content-delta` event type from a streamed response, which contains the text contents of an LLM's response.

<CodeBlocks>
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  res = co.chat_stream(
      model="command-a-03-2025",
      messages=[{"role": "user", "content": "What is an LLM?"}],
  )

  for event in res:
      if event:
          if event.type == "content-delta":
              print(event.delta.message.content.text, end="")
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
          "content": "What is an LLM?"
        }
      ],
      "stream": true
    }'
```
</CodeBlocks>
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
