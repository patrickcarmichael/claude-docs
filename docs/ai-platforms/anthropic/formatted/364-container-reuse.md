---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Container reuse

You can reuse an existing container across multiple API requests by providing the container ID from a previous response.
This allows you to maintain created files between requests.

### Example

```python
  import os
  from anthropic import Anthropic

  # Initialize the client

  client = Anthropic(
      api_key=os.getenv("ANTHROPIC_API_KEY")
  )

  # First request: Create a file with a random number

  response1 = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Write a file with a random number and save it to '/tmp/number.txt'"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  # Extract the container ID from the first response

  container_id = response1.container.id

  # Second request: Reuse the container to read the file

  response2 = client.beta.messages.create(
      container=container_id,  # Reuse the same container

      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Read the number from '/tmp/number.txt' and calculate its square"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  async function main() {
    // First request: Create a file with a random number
    const response1 = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: "Write a file with a random number and save it to '/tmp/number.txt'"
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    // Extract the container ID from the first response
    const containerId = response1.container.id;

    // Second request: Reuse the container to read the file
    const response2 = await anthropic.beta.messages.create({
      container: containerId,  // Reuse the same container
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25"],
      max_tokens: 4096,
      messages: [{
        role: "user",
        content: "Read the number from '/tmp/number.txt' and calculate its square"
      }],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    console.log(response2.content);
  }

  main().catch(console.error);
```
```bash
  # First request: Create a file with a random number

  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Write a file with a random number and save it to \"/tmp/number.txt\""
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }' > response1.json

  # Extract container ID from the response (using jq)

  CONTAINER_ID=$(jq -r '.container.id' response1.json)

  # Second request: Reuse the container to read the file

  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "container": "'$CONTAINER_ID'",
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [{
              "role": "user",
              "content": "Read the number from \"/tmp/number.txt\" and calculate its square"
          }],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
