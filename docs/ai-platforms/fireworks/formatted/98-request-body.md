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

<ParamField body="aspect_ratio" type="string" optional initialValue="16:9" placeholder="16:9">
  Aspect ratio of the generated image.

  **Options:** `1:1`, `21:9`, `16:9`, `3:2`, `5:4`, `4:5`, `2:3`, `9:16`, `9:21`, `4:3`, `3:4`
</ParamField>

<ParamField body="guidance_scale" type="float" optional initialValue="3.5" placeholder="3.5">
  Classifier-free guidance scale for the image diffusion process. Default value is 3.5.
</ParamField>

<ParamField body="num_inference_steps" type="integer" optional initialValue="4" placeholder="4">
  Number of denoising steps for the image generation process. Default value is 4.
</ParamField>

<ParamField body="seed" type="integer" optional initialValue="0" placeholder="0">
  Random seed to use for the image generation process. If 0, we will use a totally random seed.
</ParamField>

<RequestExample>
```python
  import requests

  url = "https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image"
  headers = {
      "Content-Type": "application/json",
      "Accept": "image/jpeg",
      "Authorization": "Bearer $API_KEY",
  }
  data = {
      "prompt": "A beautiful sunset over the ocean"
  }

  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
      with open("a.jpg", "wb") as f:
          f.write(response.content)
      print("Image saved as a.jpg")
  else:
      print("Error:", response.status_code, response.text)
```
```typescript
  import fs from "fs";
  import fetch from "node-fetch";

  (async () => {
      const response = await fetch("https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "image/jpeg",
          "Authorization": "Bearer $API_KEY"
        },
        body: JSON.stringify({
          prompt: "A beautiful sunset over the ocean"
        }),
      });

      // To process the response and get the image:
      const buffer = await response.arrayBuffer();

      fs.writeFile('a.jpg', Buffer.from(buffer), () => console.log('Finished downloading!'));
  })().catch(console.error);
```
```shell
  curl --request POST \
  -S --fail-with-body \
  --url https://api.fireworks.ai/inference/v1/workflows/accounts/fireworks/models/flux-1-schnell-fp8/text_to_image \
  -H 'Content-Type: application/json' \
  -H 'Accept: image/jpeg' \
  -H "Authorization: Bearer $API_KEY" \
  --data '
  {
    "prompt": "A beautiful sunset over the ocean"
  }' -o a.jpg
```
</RequestExample>

<ResponseExample>
```json Accept: application/json theme={null}
  {
    "id": "1234567890",
    "base64": ["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...", "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."],
    "finishReason": "SUCCESS",
    "seed": 1234567890
  }
```
```txt Accept: image/jpeg theme={null}
  /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k=
```
```txt Accept: image/png theme={null}
  iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==
```
</ResponseExample>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
