---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using Vision Models

```python
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  response = client.chat.completions.create(
      model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "What's in this image?"},
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                      },
                  },
              ],
          }
      ],
  )

  print(response.choices[0].message.content)
```
```typescript
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const response = await openai.chat.completions.create({
      model: "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
      messages: [{
          role: "user",
          content: [
              { type: "text", text: "What is in this image?" },
              {
                  type: "image_url",
                  image_url: {
                      url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                  },
              },
          ],
      }],
  });

  console.log(response.choices[0].message.content);
```

Output:
```text
The image depicts a serene and idyllic scene of a wooden boardwalk winding through a lush, green field on a sunny day.

*   **Sky:**
    *   The sky is a brilliant blue with wispy white clouds scattered across it.
    *   The clouds are thin and feathery, adding to the overall sense of tranquility.
*   **Boardwalk:**
    *   The boardwalk is made of weathered wooden planks, worn smooth by time and use.
    *   It stretches out into the distance, disappearing into the horizon.
    *   The boardwalk is flanked by tall grasses and reeds that reach up to the knees.
*   **Field:**
    *   The field is filled with tall, green grasses and reeds that sway gently in the breeze.
    *   The grasses are so tall that they almost obscure the boardwalk, creating a sense of mystery and adventure.
    *   In the distance, trees and bushes can be seen, adding depth and texture to the scene.
*   **Atmosphere:**
    *   The overall atmosphere is one of peace and serenity, inviting the viewer to step into the tranquil world depicted in the image.
    *   The warm sunlight and gentle breeze create a sense of comfort and relaxation.

In summary, the image presents a picturesque scene of a wooden boardwalk meandering through a lush, green field on a sunny day, evoking feelings of peace and serenity.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
