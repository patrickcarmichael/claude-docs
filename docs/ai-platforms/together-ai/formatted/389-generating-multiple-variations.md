---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating Multiple Variations

Generate multiple variations of the same prompt to choose from:
```py
  response = client.images.generate(
      prompt="A cute robot assistant helping in a modern office",
      model="black-forest-labs/FLUX.1-schnell",
      n=4,
      steps=4,
  )

  print(f"Generated {len(response.data)} variations")
  for i, image in enumerate(response.data):
      print(f"Variation {i+1}: {image.url}")
```
```typescript
  const response = await together.images.create({
    prompt: "A cute robot assistant helping in a modern office",
    model: "black-forest-labs/FLUX.1-schnell",
    n: 4,
    steps: 4,
  });

  console.log(`Generated ${response.data.length} variations`);

  response.data.forEach((image, i) => {
    console.log(`Variation ${i + 1}: ${image.url}`);
  });
```
```bash
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A cute robot assistant helping in a modern office",
         "n": 4,
         "steps": 4
       }'
```

Example output:
<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4662cd539affb47b8b31d363690a809b" alt="Multiple generated image variations" data-og-width="1166" width="1166" data-og-height="1190" height="1190" data-path="images/variations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=93ce50657e7617eede86cdc398a8cae8 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=5faa41043c62d7de67af33a993ecdde9 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=52a3acce05e8bcf79199cdb6017f7532 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=97a98672d86219304b56546b0f25d197 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=aa884d182ac397f5d42095d73662461f 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/variations.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=727080d2779f9ca84713b1c4e0b92c9d 2500w" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
