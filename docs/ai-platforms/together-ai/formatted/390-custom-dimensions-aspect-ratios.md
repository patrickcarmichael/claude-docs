---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Custom Dimensions & Aspect Ratios

Different aspect ratios for different use cases:
```py
  # Square - Social media posts, profile pictures

  response_square = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=1024,
      height=1024,
      steps=4,
  )

  # Landscape - Banners, desktop wallpapers

  response_landscape = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=1344,
      height=768,
      steps=4,
  )

  # Portrait - Mobile wallpapers, posters

  response_portrait = client.images.generate(
      prompt="A peaceful zen garden with a stone path",
      model="black-forest-labs/FLUX.1-schnell",
      width=768,
      height=1344,
      steps=4,
  )
```
```typescript
  // Square - Social media posts, profile pictures
  const response_square = await together.images.create({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1024,
    height: 1024,
    steps: 4,
  });

  // Landscape - Banners, desktop wallpapers
  const response_landscape = await together.images.create({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 1344,
    height: 768,
    steps: 4,
  });

  // Portrait - Mobile wallpapers, posters
  const response_portrait = await together.images.create({
    prompt: "A peaceful zen garden with a stone path",
    model: "black-forest-labs/FLUX.1-schnell",
    width: 768,
    height: 1344,
    steps: 4,
  });
```
```bash
  # Square - Social media posts, profile pictures

  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 1024,
         "height": 1024,
         "steps": 4
       }'

  # Landscape - Banners, desktop wallpapers

  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 1344,
         "height": 768,
         "steps": 4
       }'

  # Portrait - Mobile wallpapers, posters

  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-schnell",
         "prompt": "A peaceful zen garden with a stone path",
         "width": 768,
         "height": 1344,
         "steps": 4
       }'
```

<img src="https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=4f81f0c9d03a7334a193c2416557a0be" alt="Reference image: dims.png" data-og-width="1391" width="1391" data-og-height="990" height="990" data-path="images/dims.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=280&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=fb9e0821836ed9861a522698f5948224 280w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=560&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=31194ec41bed9963e9a7324149eb1551 560w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=840&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=062be3089cbc119efac695191a12e5bf 840w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=1100&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=0d77614e227264a1c2c7bae6d2fe12ad 1100w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=1650&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=a205e3cd5d3de30a59af5ddc0cfbadf4 1650w, https://mintcdn.com/togetherai-52386018/uy594wXLVXj0azjk/images/dims.png?w=2500&fit=max&auto=format&n=uy594wXLVXj0azjk&q=85&s=868d9308fc95e6b4c518cb98a3b01797 2500w" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
