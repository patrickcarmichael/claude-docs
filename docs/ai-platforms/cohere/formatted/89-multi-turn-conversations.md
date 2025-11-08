---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-Turn Conversations

A single Chat request can encapsulate multiple turns of a conversation, where each message in the `messages` list appears in the order it was sent. Sending multiple messages can give the model context for generating a response.

<CodeBlocks>
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="<YOUR API KEY>")

  system_message = "You respond concisely, in about 5 words or less"

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {"role": "system", "content": system_message},
          {
              "role": "user",
              "content": "Write a title for a blog post about API design. Only output the title text.",
          },
          {"role": "assistant", "content": "Designing Perfect APIs"},
          {
              "role": "user",
              "content": "Another one about generative AI.",
          },
      ],
  )

  # "AI: The Generative Age"

  print(res.message.content[0].text)
```
```bash Curl
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
          "content": "You respond concisely, in about 5 words or less"
        },
        {
          "role": "user",
          "content": "Write a title for a blog post about API design. Only output the title text."
        },
        {
          "role": "assistant",
          "content": "Designing Perfect APIs"
        },
        {
          "role": "user",
          "content": "Another one about generative AI."
        }
      ]
    }'
```
</CodeBlocks>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
