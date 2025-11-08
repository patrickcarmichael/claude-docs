---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming Responses

For real-time applications, you can stream the response as it's being generated. For a complete example, see the [streaming example notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_streaming_example.ipynb).
```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  stream = llm.responses.create(
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      stream=True,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  for chunk in stream:
      print(chunk)
```
```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  stream = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      stream=True,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  for chunk in stream:
      print(chunk)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
