---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Storing Responses

By default, responses are stored and can be referenced by their ID. You can disable this by setting `store=False`. If you do this, you will not be able to use the `previous_response_id` to continue the conversation. For a complete example, see the [store=False notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/mcp_server_with_store_false_argument.ipynb).
```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  response = llm.responses.create(
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      store=False,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  # This will fail because the previous response was not stored

  try:
      continuation_response = llm.responses.create(
          input="Explain the second fact in more detail.",
          previous_response_id=response.id
      )
  except Exception as e:
      print(e)
```
```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="give me 5 interesting facts on modelcontextprotocol/python-sdk -- keep it short!",
      store=False,
      tools=[{"type": "mcp", "server_url": "https://mcp.deepwiki.com/mcp"}]
  )

  # This will fail because the previous response was not stored

  try:
      continuation_response = client.responses.create(
          model="accounts/fireworks/models/qwen3-235b-a22b",
          input="Explain the second fact in more detail.",
          previous_response_id=response.id
      )
  except Exception as e:
      print(e)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
