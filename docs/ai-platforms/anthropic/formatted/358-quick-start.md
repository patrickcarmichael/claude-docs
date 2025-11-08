---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quick start

Here's a simple example that asks Claude to perform a calculation:
```bash
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "anthropic-beta: code-execution-2025-08-25" \
      --header "content-type: application/json" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
              }
          ],
          "tools": [{
              "type": "code_execution_20250825",
              "name": "code_execution"
          }]
      }'
```
```python
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      betas=["code-execution-2025-08-25"],
      max_tokens=4096,
      messages=[{
          "role": "user",
          "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      }],
      tools=[{
          "type": "code_execution_20250825",
          "name": "code_execution"
      }]
  )

  print(response)
```
```typescript
  import { Anthropic } from '@anthropic-ai/sdk';

  const anthropic = new Anthropic();

  async function main() {
    const response = await anthropic.beta.messages.create({
      model: "claude-sonnet-4-5",
      betas: ["code-execution-2025-08-25"],
      max_tokens: 4096,
      messages: [
        {
          role: "user",
          content: "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
        }
      ],
      tools: [{
        type: "code_execution_20250825",
        name: "code_execution"
      }]
    });

    console.log(response);
  }

  main().catch(console.error);
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
