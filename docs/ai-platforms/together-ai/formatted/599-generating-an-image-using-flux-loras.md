---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating an image using Flux LoRAs

Some Flux LoRA fine-tunes need to be activated using a trigger phrases that can be used in the prompt and can typically be found in the model cards. For example with: [https://huggingface.co/multimodalart/flux-tarot-v1](https://huggingface.co/multimodalart/flux-tarot-v1), you should use `in the style of TOK a trtcrd tarot style` to trigger the image generation.

You can add up to 2 LoRAs per image to combine the style from the different fine-tunes. The `scale` parameter allows you to specify the strength of each LoRA. Typically values of `0.3-1.2` will produce good results.
```py
  from together import Together

  client = Together()
  response = client.images.generate(
      prompt="a BLKLGHT image of man walking outside on rainy day",
      model="black-forest-labs/FLUX.1-dev-lora",
      width=1024,
      height=768,
      steps=28,
      n=1,
      response_format="url",
      image_loras=[
          {"path": "https://replicate.com/fofr/flux-black-light", "scale": 0.8},
          {
              "path": "https://huggingface.co/XLabs-AI/flux-RealismLora",
              "scale": 0.8,
          },
      ],
  )
  print(response.data[0].url)
```
```sh
  curl -X POST "https://api.together.xyz/v1/images/generations"
  -H "Authorization: Bearer $TOGETHER_API_KEY"
  -H "Content-Type: application/json"
  -d '{
      "model": "black-forest-labs/FLUX.1-dev-lora",
      "prompt": "cute dog",
      "width": 1024,
      "height": 768,
      "steps": 28,
      "n": 1,
      "response_format": "url",
      "image_loras": [{"path":"https://huggingface.co/XLabs-AI/flux-RealismLora","scale":1},
          {"path": "https://huggingface.co/XLabs-AI/flux-RealismLora", "scale": 0.8}]
     }'
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
