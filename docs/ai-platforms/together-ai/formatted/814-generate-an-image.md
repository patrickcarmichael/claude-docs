---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate an image

To generate an image, use the `together images generate` method.

Pass the prompt in as the first argument, and use the `--model` option to choose your model:
```sh
together images generate \
  "space robots" \
  --model black-forest-labs/FLUX.1-dev
```
The image is opened in the default image viewer by default. To disable this, use `--no-show`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
