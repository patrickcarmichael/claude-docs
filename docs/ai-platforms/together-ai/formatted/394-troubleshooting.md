---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

**Image doesn't match prompt well**

* Make prompt more descriptive and specific
* Add style references (e.g., "National Geographic style")
* Use negative prompts to exclude unwanted elements
* Try increasing steps to 30-40

**Poor image quality**

* Increase `steps` to 30-40 for production
* Add quality modifiers: "highly detailed", "8k", "professional"
* Use negative prompt: "blurry, low quality, distorted, pixelated"
* Try a higher-tier model

**Inconsistent results**

* Use `seed` parameter for reproducibility
* Keep the same seed when testing variations
* Generate multiple variations with `n` parameter

**Wrong dimensions or aspect ratio**

* Specify `width` and `height` explicitly
* Common ratios:
  * Square: 1024x1024
  * Landscape: 1344x768
  * Portrait: 768x1344
* Ensure dimensions are multiples of 8


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
