---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Complete example

Here's a complete example that demonstrates connecting to an existing deployment and using it for a conversation:
```python Basic usage theme={null}
  from fireworks import LLM

  # Connect to existing deployment

  llm = LLM(
      model="llama-v3p2-3b-instruct",
      deployment_type="on-demand",
      id="my-existing-deployment",
  )

  # Use OpenAI-compatible chat completions

  response = llm.chat.completions.create(
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Explain quantum computing in simple terms."}
      ],
      max_tokens=150,
      temperature=0.7
  )

  print(response.choices[0].message.content)
```
```python Streaming responses theme={null}
  from fireworks import LLM

  llm = LLM(
      model="llama-v3p2-3b-instruct",
      deployment_type="on-demand",
      id="my-existing-deployment",
  )

  # Stream the response

  stream = llm.chat.completions.create(
      messages=[{"role": "user", "content": "Write a short poem about AI."}],
      stream=True,
      max_tokens=100
  )

  for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
