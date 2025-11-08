---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Image models

Use our [Images](/reference/post-images-generations) endpoint for Image Models.

| Organization      | Model Name                     | Model String for API                     | Default steps |
| :---------------- | :----------------------------- | :--------------------------------------- | :------------ |
| Google            | Imagen 4.0 Preview             | google/imagen-4.0-preview                | -             |
| Google            | Imagen 4.0 Fast                | google/imagen-4.0-fast                   | -             |
| Google            | Imagen 4.0 Ultra               | google/imagen-4.0-ultra                  | -             |
| Google            | Flash Image 2.5 (Nano Banana)  | google/flash-image-2.5                   | -             |
| Black Forest Labs | Flux.1 \[schnell] **(free)\*** | black-forest-labs/FLUX.1-schnell-Free    | N/A           |
| Black Forest Labs | Flux.1 \[schnell] (Turbo)      | black-forest-labs/FLUX.1-schnell         | 4             |
| Black Forest Labs | Flux.1 Dev                     | black-forest-labs/FLUX.1-dev             | 28            |
| Black Forest Labs | Flux1.1 \[pro]                 | black-forest-labs/FLUX.1.1-pro           | -             |
| Black Forest Labs | Flux.1 Kontext \[pro]          | black-forest-labs/FLUX.1-kontext-pro     | 28            |
| Black Forest Labs | Flux.1 Kontext \[max]          | black-forest-labs/FLUX.1-kontext-max     | 28            |
| Black Forest Labs | Flux.1 Kontext \[dev]          | black-forest-labs/FLUX.1-kontext-dev     | 28            |
| Black Forest Labs | FLUX.1 Krea \[dev]             | black-forest-labs/FLUX.1-krea-dev        | 28            |
| ByteDance         | Seedream 3.0                   | ByteDance-Seed/Seedream-3.0              | -             |
| ByteDance         | Seedream 4.0                   | ByteDance-Seed/Seedream-4.0              | -             |
| Qwen              | Qwen Image                     | Qwen/Qwen-Image                          | -             |
| RunDiffusion      | Juggernaut Pro Flux            | RunDiffusion/Juggernaut-pro-flux         | -             |
| RunDiffusion      | Juggernaut Lightning Flux      | Rundiffusion/Juggernaut-Lightning-Flux   | -             |
| HiDream           | HiDream-I1-Full                | HiDream-ai/HiDream-I1-Full               | -             |
| HiDream           | HiDream-I1-Dev                 | HiDream-ai/HiDream-I1-Dev                | -             |
| HiDream           | HiDream-I1-Fast                | HiDream-ai/HiDream-I1-Fast               | -             |
| Ideogram          | Ideogram 3.0                   | ideogram/ideogram-3.0                    | -             |
| Lykon             | Dreamshaper                    | Lykon/DreamShaper                        | -             |
| Stability AI      | SD XL                          | stabilityai/stable-diffusion-xl-base-1.0 | -             |
| Stability AI      | Stable Diffusion 3             | stabilityai/stable-diffusion-3-medium    | -             |

Note: Due to high demand, FLUX.1 \[schnell] Free has a model specific rate limit of 10 img/min. Image models can also only be used with credits. Users are unable to call Image models with a zero or negative balance.

\*Free model has reduced rate limits and performance compared to our paid Turbo endpoint for Flux Shnell named `black-forest-labs/FLUX.1-schnell`

**Image Model Examples**

* [Blinkshot.io](https://www.blinkshot.io/) - A realtime AI image playground built with Flux Schnell
* [Logo Creator](https://www.logo-creator.io/) - An logo generator that creates professional logos in seconds using Flux Pro 1.1
* [PicMenu](https://www.picmenu.co/) - A menu visualizer that takes a restaurant menu and generates nice images for each dish.
* [Flux LoRA Inference Notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Flux_LoRA_Inference.ipynb) - Using LoRA fine-tuned image generations models

**How FLUX pricing works** For FLUX models (except for pro) pricing is based on the size of generated images (in megapixels) and the number of steps used (if the number of steps exceed the default steps).

* **Default pricing:** The listed per megapixel prices are for the default number of steps.
* **Using more or fewer steps:** Costs are adjusted based on the number of steps used **only if you go above the default steps**. If you use more steps, the cost increases proportionally using the formula below. If you use fewer steps, the cost *does not* decrease and is based on the default rate.

Here’s a formula to calculate cost:

Cost = MP × Price per MP × (Steps ÷ Default Steps)

Where:

* MP = (Width × Height ÷ 1,000,000)
* Price per MP = Cost for generating one megapixel at the default steps
* Steps = The number of steps used for the image generation. This is only factored in if going above default steps.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
