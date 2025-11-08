---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Testing Your Fine-tuned VLM

After deployment, test your fine-tuned VLM using the same API patterns as base VLMs:
```python Python (OpenAI Compatible) theme={null}
  import openai

  client = openai.OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key="<FIREWORKS_API_KEY>",
  )

  response = client.chat.completions.create(
      model="accounts/your-account/models/my-custom-vlm",
      messages=[{
          "role": "user",
          "content": [{
              "type": "image_url",
              "image_url": {
                  "url": "https://raw.githubusercontent.com/fw-ai/cookbook/refs/heads/main/learn/vlm-finetuning/images/icecream.jpeg"
              },
          },{
              "type": "text",
              "text": "What's in this image?",
          }],
      }]
  )
  print(response.choices[0].message.content)
```
```python Python (Fireworks SDK) theme={null}
  from fireworks import LLM

  # Use your fine-tuned model

  llm = LLM(model="accounts/your-account/models/my-custom-vlm")

  response = llm.chat.completions.create(
      messages=[{
          "role": "user",
          "content": [{
              "type": "image_url",
              "image_url": {
                  "url": "https://raw.githubusercontent.com/fw-ai/cookbook/refs/heads/main/learn/vlm-finetuning/images/icecream.jpeg"
              },
          },{
              "type": "text",
              "text": "What's in this image?",
          }],
      }]
  )
  print(response.choices[0].message.content)
```

<Tip>
  If you fine-tuned using the example dataset, your model should include `<think></think>` tags in its response.
</Tip>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
