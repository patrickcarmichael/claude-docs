---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Make your first Serverless API call

<Tabs>
  <Tab title="Python">
    Fireworks provides an OpenAI compatible endpoint. Install the OpenAI Python SDK:
```bash
    pip install openai
```
    Then make your first Serverless API call:
```python
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        messages=[{
            "role": "user",
            "content": "Say hello in Spanish",
        }],
    )

    print(response.choices[0].message.content)
```
  </Tab>

  <Tab title="JavaScript">
    Fireworks provides an OpenAI compatible endpoint. Install the OpenAI Node.js SDK:
```bash
    npm install openai
```
    Then make your first Serverless API call:
```javascript
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      messages: [
        {
          role: "user",
          content: "Say hello in Spanish",
        },
      ],
    });

    console.log(response.choices[0].message.content);
```
  </Tab>

  <Tab title="curl">
```bash
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "messages": [
          {
            "role": "user",
            "content": "Say hello in Spanish"
          }
        ]
      }'
```
  </Tab>
</Tabs>

You should see a response like: `"¡Hola!"`

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
