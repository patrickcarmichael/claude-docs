---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## System Message

Developers can adjust the LLMs behavior by including a system message in the `messages` list
with the role set to `system`.

The system message contains instructions that the model will respect over any instructions sent in messages sent from other roles. It is often used by developers to control the style in which the model communicates and to provide guidelines for how to handle various topics.

It is recommended to send the system message as the first element in the messages list.

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
      ],  # "Designing Perfect APIs"

  )

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
        }
      ]
    }'
```
</CodeBlocks>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
