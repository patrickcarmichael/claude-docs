---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Key Parameters

Flux Kontext models support the following key parameters:

* `model`: Choose from `black-forest-labs/FLUX.1-kontext-pro`, `black-forest-labs/FLUX.1-kontext-max`, or `black-forest-labs/FLUX.1-kontext-dev`
* `prompt`: Text description of the transformation you want to apply
* `image_url`: URL of the reference image to transform
* `aspect_ratio`: Output aspect ratio (e.g., "1:1", "16:9", "9:16", "4:3", "3:2") - alternatively, you can use `width` and `height` for precise pixel dimensions
* `steps`: Number of diffusion steps (default: 28, higher values may improve quality)
* `seed`: Random seed for reproducible results

For complete parameter documentation, see the [Images Overview](/docs/images-overview#parameters).

See all available image models: [Image Models](/docs/serverless-models#image-models)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
