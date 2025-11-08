---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Provide reference image

Use a reference image to guide the generation:
```py
  from together import Together

  client = Together()

  response = client.images.generate(
      model="black-forest-labs/FLUX.1-kontext-pro",
      width=1024,
      height=768,
      prompt="Transform this into a watercolor painting",
      image_url="https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
  )
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  const response = await together.images.create({
    model: "black-forest-labs/FLUX.1-kontext-pro",
    width: 1024,
    height: 768,
    prompt: "Transform this into a watercolor painting",
    image_url:
      "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
  });
```
```bash
  curl -X POST "https://api.together.xyz/v1/images/generations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{
         "model": "black-forest-labs/FLUX.1-kontext-pro",
         "width": 1024,
         "height": 768,
         "prompt": "Transform this into a watercolor painting",
         "image_url": "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg"
       }'
```

Example output:

<img src="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=2f4036b77e23ee90388200b71abfc7af" alt="Reference image: reference_image.png" data-og-width="989" width="989" data-og-height="360" height="360" data-path="images/reference_image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=280&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=09e764929470af3788d2be654ad50464 280w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=560&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=e45d47b542c051c2e2f375a4f357a79f 560w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=840&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=748b9876fb4984438c0acc635fa2314d 840w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=1100&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=da6a7a5a109aa3c7321871e17e020293 1100w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=1650&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=eb058db20b8898e80f62a2da77f23b6c 1650w, https://mintcdn.com/togetherai-52386018/cT7ZxyHutQ2IcmKA/images/reference_image.png?w=2500&fit=max&auto=format&n=cT7ZxyHutQ2IcmKA&q=85&s=4a5ba1b910dba43bee558540f35124f9 2500w" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
