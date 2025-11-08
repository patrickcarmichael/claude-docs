---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Base64 Images

If you prefer the image data to be embedded directly in the response, set `response_format` to "base64".
```py
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.1-schnell",
      prompt="a cat in outer space",
      response_format="base64",
  )

  print(response.data[0].b64_json)
```
```typescript
  import Together from "together-ai";

  const client = new Together();

  const response = await client.images.create({
    model: "black-forest-labs/FLUX.1-schnell",
    prompt: "A cat in outer space",
    response_format: "base64",
  });

  console.log(response.data[0].b64_json);
```
```bash
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A cat in outer space",
         "response_format": "base64"
       }'
```

When you do, the model response includes a new `b64_json` field that contains the image encoded as a base64 string.
```json
{
  "id": "oHpD53L-2kFHot-998e0de9fe14d8a1-SEA",
  "model": "black-forest-labs/FLUX.1-schnell",
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAA..."
    }
  ]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
