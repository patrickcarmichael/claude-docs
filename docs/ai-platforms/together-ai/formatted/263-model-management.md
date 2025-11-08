---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Model Management

### Can I download the weights of my model?

Yes, to use your fine-tuned model outside our platform:

Run: `together fine-tuning download <FT-ID>`

This downloads ZSTD compressed weights. Extract with `tar -xf filename`.

Options:

* `--output`,`-o` (filename, optional) -- Specify output filename. Default: `<MODEL-NAME>.tar.zst`
* `--step`,`-s` (integer, optional) -- Download specific checkpoint. Default: latest (-1)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
