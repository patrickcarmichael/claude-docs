---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deleting Stored Responses

When responses are stored (the default behavior with `store=True`), you can immediately delete them from storage using the DELETE endpoint. This permanently removes the conversation data.
```python Python (Fireworks) theme={null}
  from fireworks import LLM
  import requests
  import os

  llm = LLM(model="qwen3-235b-a22b", deployment_type="serverless")

  # Create a response

  response = llm.responses.create(
      input="What is the capital of France?",
      store=True  # This is the default

  )

  response_id = response.id
  print(f"Created response with ID: {response_id}")

  # Delete the response immediately

  headers = {
      "Authorization": f"Bearer {os.getenv('FIREWORKS_API_KEY')}",
      "x-fireworks-account-id": "your-account-id"
  }
  delete_response = requests.delete(
      f"https://api.fireworks.ai/inference/v1/responses/{response_id}",
      headers=headers
  )

  if delete_response.status_code == 200:
      print("Response deleted successfully")
  else:
      print(f"Failed to delete response: {delete_response.status_code}")
```
```python Python (OpenAI) theme={null}
  import os
  from openai import OpenAI
  import requests

  client = OpenAI(
      base_url="https://api.fireworks.ai/inference/v1",
      api_key=os.getenv("FIREWORKS_API_KEY", "YOUR_FIREWORKS_API_KEY_HERE")
  )

  # Create a response

  response = client.responses.create(
      model="accounts/fireworks/models/qwen3-235b-a22b",
      input="What is the capital of France?",
      store=True  # This is the default

  )

  response_id = response.id
  print(f"Created response with ID: {response_id}")

  # Delete the response immediately

  headers = {
      "Authorization": f"Bearer {os.getenv('FIREWORKS_API_KEY')}",
      "x-fireworks-account-id": "your-account-id"
  }
  delete_response = requests.delete(
      f"https://api.fireworks.ai/inference/v1/responses/{response_id}",
      headers=headers
  )

  if delete_response.status_code == 200:
      print("Response deleted successfully")
  else:
      print(f"Failed to delete response: {delete_response.status_code}")
```
```bash
  # First create a response and capture the ID

  RESPONSE=$(curl -X POST https://api.fireworks.ai/inference/v1/responses \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "accounts/fireworks/models/qwen3-235b-a22b",
      "input": "What is the capital of France?",
      "store": true
    }')

  # Extract the response ID (using jq or similar JSON parser)

  RESPONSE_ID=$(echo $RESPONSE | jq -r '.id')

  # Delete the response

  curl -X DELETE "https://api.fireworks.ai/inference/v1/responses/$RESPONSE_ID" \
    -H "Authorization: Bearer $FIREWORKS_API_KEY" \
    -H "x-fireworks-account-id: your-account-id"
```

>   **⚠️ Warning**
>
> Once a response is deleted, it cannot be recovered.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
