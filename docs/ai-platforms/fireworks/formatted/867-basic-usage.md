---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic usage

<Tabs>
  <Tab title="Python">
```python
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.completions.create(
        model="accounts/fireworks/models/deepseek-v3p1",
        prompt="Once upon a time"
    )

    print(response.choices[0].text)
```
  </Tab>

  <Tab title="JavaScript">
```javascript
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.completions.create({
      model: "accounts/fireworks/models/deepseek-v3p1",
      prompt: "Once upon a time",
    });

    console.log(response.choices[0].text);
```
  </Tab>

  <Tab title="curl">
```bash
    curl https://api.fireworks.ai/inference/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/fireworks/models/deepseek-v3p1",
        "prompt": "Once upon a time"
      }'
```
  </Tab>
</Tabs>

>   **📝 Note**
>
> Most models automatically prepend the beginning-of-sequence (BOS) token (e.g., `<s>`) to your prompt. Verify this with the `raw_output` parameter if needed.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
