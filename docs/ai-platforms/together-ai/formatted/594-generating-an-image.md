---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating an image

Here's how to use the new Kontext models:
```python
  from together import Together

  client = Together()

  imageCompletion = client.images.generate(
      model="black-forest-labs/FLUX.1-kontext-pro",
      width=1536,
      height=1024,
      steps=28,
      prompt="make his shirt yellow",
      image_url="https://github.com/nutlope.png",
  )

  print(imageCompletion.data[0].url)
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      model: "black-forest-labs/FLUX.1-kontext-pro",
      width: 1536,
      height: 1024,
      steps: 28,
      prompt: "make his shirt yellow",
      image_url: "https://github.com/nutlope.png",
    });

    console.log(response.data[0].url);
  }

  main();
```
```bash
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-kontext-pro",
         "width": 1536,
         "height": 1024,
         "steps": 28,
         "prompt": "make his shirt yellow",
         "image_url": "https://github.com/nutlope.png"
       }'
```

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=66b5f695ba162346d8079ab48b8f1de3" alt="" data-og-width="904" width="904" data-og-height="492" height="492" data-path="images/hassan-yellow-shirt.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=280&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=cd46f805ebdb73e6a437c6c9cc27e526 280w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=560&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=c4a2d6508e33ede4a7670d26e8423d6a 560w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=840&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=1fcbe3d062c2ca60cf785152728bdf27 840w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=1100&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=45ec4ec28b0e72b7534ebfbc253d7f9f 1100w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=1650&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=3009ea540ed84dbc06d69314337b7c63 1650w, https://mintcdn.com/togetherai-52386018/YmYlzoJDwPs82-4E/images/hassan-yellow-shirt.jpg?w=2500&fit=max&auto=format&n=YmYlzoJDwPs82-4E&q=85&s=745dce4b24cc380ac3cda271cee8fc15 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
