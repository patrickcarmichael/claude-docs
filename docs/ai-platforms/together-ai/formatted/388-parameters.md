---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parameters

| Parameter         | Type    | Description                                                                              | Default      |
| ----------------- | ------- | ---------------------------------------------------------------------------------------- | ------------ |
| `prompt`          | string  | Text description of the image to generate                                                | **Required** |
| `model`           | string  | Model identifier                                                                         | **Required** |
| `width`           | integer | Image width in pixels                                                                    | 1024         |
| `height`          | integer | Image height in pixels                                                                   | 1024         |
| `n`               | integer | Number of images to generate (1-4)                                                       | 1            |
| `steps`           | integer | Diffusion steps (higher = better quality, slower)                                        | 1-50         |
| `seed`            | integer | Random seed for reproducibility                                                          | any          |
| `negative_prompt` | string  | What to avoid in generation                                                              | -            |
| `frame_images`    | array   | **Required for Kling model.** Array of images to guide video generation, like keyframes. | -            |

* `prompt` is required for all models except Kling
* `width` and `height` will rely on defaults unless otherwise specified - options for dimensions differ by model
* Flux Schnell and Kontext \[Pro/Max/Dev] models use the `aspect_ratio` parameter to set the output image size whereas Flux.1 Pro, Flux 1.1 Pro, and Flux.1 Dev use `width` and `height` parameters.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
