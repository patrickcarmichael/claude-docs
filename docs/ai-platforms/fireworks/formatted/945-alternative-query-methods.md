---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Alternative query methods

<Accordion title="Completions API (advanced)">
  For the Completions API, manually insert the image token `<image>` in your prompt and supply images as an ordered list:
```python
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ.get("FIREWORKS_API_KEY"),
      base_url="https://api.fireworks.ai/inference/v1"
  )

  response = client.completions.create(
      model="accounts/fireworks/models/qwen2p5-vl-32b-instruct",
      prompt="SYSTEM: Hello\n\nUSER:<image>\ntell me about the image\n\nASSISTANT:",
      extra_body={
          "images": ["https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"]
      }
  )

  print(response.choices[0].text)
```
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
