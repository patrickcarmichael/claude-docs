---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

**No images in response?**

* Verify the model supports image generation (`output_modalities` includes `"image"`)
* Ensure you've included `"modalities": ["image", "text"]` in your request
* Check that your prompt is requesting image generation

**Model not found?**

* Use the [Models page](/models) to find available image generation models
* Filter by output modalities to see compatible models


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
