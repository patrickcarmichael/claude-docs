---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Acceptable LoRA URL formats

You can point to any URL that has a `.safetensors` file with a valid Flux LoRA fine-tune.

| Format                                        | Example                                                                                                                                                                                                                                        |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HuggingFace Repo Link                         | [https://huggingface.co/multimodalart/flux-tarot-v1](https://huggingface.co/multimodalart/flux-tarot-v1)                                                                                                                                       |
| HuggingFace Direct File Link with "resolve"\* | [https://huggingface.co/XLabs-AI/flux-lora-collection/resolve/main/anime\_lora.safetensors](https://huggingface.co/XLabs-AI/flux-lora-collection/resolve/main/anime_lora.safetensors)                                                          |
| Civit Download Link                           | [https://civitai.com/api/download/models/913438?type=Model\&format=SafeTensor](https://civitai.com/api/download/models/913438?type=Model\&format=SafeTensor)                                                                                   |
| Replicate Fine-tuned Flux Model Link          | [https://replicate.com/fofr/flux-black-light](https://replicate.com/fofr/flux-black-light)                                                                                                                                                     |
| Replicate Fine-tuned Flux Version Link        | [https://replicate.com/fofr/flux-black-light/versions/d0d48e298dcb51118c3f903817c833bba063936637a33ac52a8ffd6a94859af7](https://replicate.com/fofr/flux-black-light/versions/d0d48e298dcb51118c3f903817c833bba063936637a33ac52a8ffd6a94859af7) |
| Direct file link ending with ".safetensors"   | [https://mybucket.s3.amazonaws.com/my\_special\_lora.safetensors](https://mybucket.s3.amazonaws.com/my_special_lora.safetensors)                                                                                                               |

\*Note: the HuggingFace web page for a file ([https://huggingface.co/XLabs-AI/flux-lora-collection/blob/main/anime\_lora.safetensors](https://huggingface.co/XLabs-AI/flux-lora-collection/blob/main/anime_lora.safetensors)) will NOT work

If the safetensors file has incompatible keys, you'll get the message " has unused keys \<keys...>". This will happen if you pass a finetune of a non-flux model or an otherwise invalid file.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
