---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic Usage

You can interact with the Response API using the Fireworks Python SDK or by making direct HTTP requests.

### Creating a Response

To start a new conversation, you use the `client.responses.create` method. For a complete example, see the [getting started notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_mcp_examples.ipynb).
```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  response = llm.responses.create(
      input="What is reward-kit and what are its 2 main features? Keep it short Please analyze the fw-ai-external/reward-kit repository.",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(response.output[-1].content[0].text.split("</think>")[-1])
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
      input="What is reward-kit and what are its 2 main features? Keep it short Please analyze the fw-ai-external/reward-kit repository.",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(response.output[-1].content[0].text.split("</think>")[-1])
```

### Continuing a Conversation with `previous_response_id`

To continue a conversation, you can use the `previous_response_id` parameter. This tells the API to use the context from a previous response, so you don't have to send the entire conversation history again. For a complete example, see the [previous response ID notebook](https://github.com/fw-ai/cookbook/blob/main/learn/response-api/fireworks_previous_response_cookbook.ipynb).
```python Python (Fireworks) theme={null}
  from fireworks import LLM

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  # First, create an initial response

  initial_response = llm.responses.create(
      input="What are the key features of reward-kit?",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )
  initial_response_id = initial_response.id

  # Now, continue the conversation

  continuation_response = llm.responses.create(
      input="How do I install it?",
      previous_response_id=initial_response_id,
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(continuation_response.output[-1].content[0].text.split("</think>")[-1])
```
```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  # First, create an initial response

  initial_response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="What are the key features of reward-kit?",
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )
  initial_response_id = initial_response.id

  # Now, continue the conversation

  continuation_response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="How do I install it?",
      previous_response_id=initial_response_id,
      tools=[{"type": "sse", "server_url": "https://gitmcp.io/docs"}]
  )

  print(continuation_response.output[-1].content[0].text.split("</think>")[-1])
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
