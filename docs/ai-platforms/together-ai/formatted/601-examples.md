---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Examples

The example below produces a realistic tarot card of a panda:
```py
prompt = "a baby panda eating bamboo in the style of TOK a trtcrd tarot style"

response = client.images.generate(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-dev-lora",
    width=1024,
    height=768,
    steps=28,
    n=1,
    response_format="url",
    image_loras=[
        {
            "path": "https://huggingface.co/multimodalart/flux-tarot-v1",
            "scale": 1,
        },
        {
            "path": "https://huggingface.co/Shakker-Labs/FLUX.1-dev-LoRA-add-details",
            "scale": 0.8,
        },
    ],
)
```
<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=cb73a699bcb42f2deec002a9670cb4d6" alt="" data-og-width="1218" width="1218" data-og-height="918" height="918" data-path="images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=280&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a176678d92b45daa26c77ada7aa668b3 280w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=560&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=30d0981ee82e0beb8711bfdb78d3bb03 560w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=840&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=64a9e45ac4f261e8568a9d089b21f65d 840w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=1100&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=8077759db2f874c8daf5cf83e5d503ce 1100w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=1650&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=a9c6a5082858a26e6990d556502964fd 1650w, https://mintcdn.com/togetherai-52386018/-CYPjI-GKL4GZ_Jy/images/22424d205f06f9cffcfead6d4fd868796acefd1ba69fe874c6f6eb79fa93471d-Screenshot_2025-01-26_at_10.19.07_PM.png?w=2500&fit=max&auto=format&n=-CYPjI-GKL4GZ_Jy&q=85&s=b64bfe2edff61a5e2ffe31803ddc557e 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
