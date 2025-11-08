---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Request Body

<ParamField body="prompt" type="string" required initialValue="A photo of a cat" placeholder="A photo of a cat">
  Prompt to use for the image generation process.
</ParamField>

<ParamField body="input_image" type="string | null" optional>
  Base64 encoded image or URL to use with Kontext.
</ParamField>

<ParamField body="seed" type="integer | null" optional initialValue="42" placeholder="42">
  Optional seed for reproducibility.
</ParamField>

<ParamField body="aspect_ratio" type="string | null" optional>
  Aspect ratio of the image between 21:9 and 9:21.
</ParamField>

<ParamField body="output_format" type="string" optional initialValue="png" placeholder="png">
  Output format for the generated image. Can be 'jpeg' or 'png'.

  **Options:** `jpeg`, `png`
</ParamField>

<ParamField body="webhook_url" type="string | null" optional>
  URL to receive webhook notifications.

  **Length:** 1-2083 characters
</ParamField>

<ParamField body="webhook_secret" type="string | null" optional>
  Optional secret for webhook signature verification.
</ParamField>

<ParamField body="prompt_upsampling" type="boolean" optional initialValue="false" placeholder="false">
  Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation.
</ParamField>

<ParamField body="safety_tolerance" type="integer" optional initialValue="2" placeholder="2">
  Tolerance level for input and output moderation. Between 0 and 6, 0 being most strict, 6 being least strict. Limit of 2 for Image to Image.

  **Range:** 0-6
</ParamField>

<RequestExample>
```python
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}"
  headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      "prompt": "A beautiful sunset over the ocean",
      "input_image": "<string>",
      "seed": 42,
      "aspect_ratio": "<string>",
      "output_format": "jpeg",
      "webhook_url": "<string>",
      "webhook_secret": "<string>",
      "prompt_upsampling": False,
      "safety_tolerance": 2
  }

  response = requests.post(url, headers=headers, json=data)
```
```typescript
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model}", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          prompt: "A beautiful sunset over the ocean"
        }),
      });
  })().catch(console.error);
```
```shell
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/{model} \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    "prompt": "A beautiful sunset over the ocean"
  }'
```
</RequestExample>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
