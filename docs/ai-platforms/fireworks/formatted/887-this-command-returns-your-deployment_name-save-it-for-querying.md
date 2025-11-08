---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## This command returns your DEPLOYMENT_NAME - save it for querying

firectl create deployment accounts/fireworks/models/<MODEL_NAME> --wait
```
See [Deployment shapes](#deployment-shapes) below to optimize for speed, throughput, or cost.

**Query your deployment:**

After creating a deployment, query it using this format:
```
<MODEL_NAME>#<DEPLOYMENT_NAME>
```
<Tip>
  You can find your deployment name anytime with `firectl list deployments` and `firectl get deployment <DEPLOYMENT_ID>`.
</Tip>

**Examples:**

<Tabs>
  <Tab title="Fireworks model">
```
    accounts/fireworks/models/mixtral-8x7b#accounts/alice/deployments/12345678
```
    * Model: `accounts/fireworks/models/mixtral-8x7b`
    * Deployment: `accounts/alice/deployments/12345678`

    <Tip>
      You can also use shorthand: `fireworks/mixtral-8x7b#alice/12345678`
    </Tip>
  </Tab>

  <Tab title="Custom model">
```
    accounts/alice/models/custom-model#accounts/alice/deployments/12345678
```
    * Model: `accounts/alice/models/custom-model`
    * Deployment: `accounts/alice/deployments/12345678`

    <Tip>
      You can also use shorthand: `alice/custom-model#alice/12345678`
    </Tip>
  </Tab>
</Tabs>

### Code examples

<Tabs>
  <Tab title="Python">
```python
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
        messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
    )

    print(response.choices[0].message.content)
```
  </Tab>

  <Tab title="JavaScript">
```javascript
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
      messages: [
        {
          role: "user",
          content: "Explain quantum computing in simple terms",
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
        "model": "accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
        "messages": [
          {
            "role": "user",
            "content": "Explain quantum computing in simple terms"
          }
        ]
      }'
```
  </Tab>
</Tabs>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
