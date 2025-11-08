---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating an image

To query an image model, use the `.images` method and specify the image model you want to use.
```py
  client = Together()

  # Generate an image from a text prompt

  response = client.images.generate(
      prompt="A serene mountain landscape at sunset with a lake reflection",
      model="black-forest-labs/FLUX.1-schnell",
      steps=4,
  )

  print(f"Image URL: {response.data[0].url}")
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      prompt: "A serene mountain landscape at sunset with a lake reflection",
      model: "black-forest-labs/FLUX.1-schnell",
      steps: 4,
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
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A serene mountain landscape at sunset with a lake reflection",
         "steps": 4
       }'
```

Example response structure and output:
```json
{
  "id": "oFuwv7Y-2kFHot-99170ebf9e84e0ce-SJC",
  "model": "black-forest-labs/FLUX.1-schnell",
  "data": [
    {
      "index": 0,
      "url": "https://api.together.ai/v1/images/..."
    }
  ]
}
```

<img src="https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=4d99c87bb633262fdb932f3f9a9fa436" alt="Reference image: image-overview1.png" width="350" data-og-width="1024" data-og-height="1024" data-path="images/image-overview1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=280&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=8a8cc7b204ced18a0f54475d6c29d083 280w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=560&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=7b9316fc8048f5099c9fc93ea7d0f8f9 560w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=840&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=6c4e6b322d745bde355f796f173f3acf 840w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=1100&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=b508dae30e522a828fec8a36d1bcfdff 1100w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=1650&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=3975e1d0af34f521c5bdf143df8cd11a 1650w, https://mintcdn.com/togetherai-52386018/iDTycfazH2_GOS_A/images/image-overview1.png?w=2500&fit=max&auto=format&n=iDTycfazH2_GOS_A&q=85&s=0130a5593fd60a023b9e0960a4824464 2500w" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
