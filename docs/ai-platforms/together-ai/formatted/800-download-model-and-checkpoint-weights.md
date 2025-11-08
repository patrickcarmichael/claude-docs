---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Download Model and Checkpoint Weights

To download the weights of a fine-tuned model, run:
```shell
  together fine-tuning download <FT-ID>
```

This command will download ZSTD compressed weights of the model. To extract the weights, run `tar -xf filename`.

Other arguments:

* `--output`,`-o` (filename, *optional*) -- Specify the output filename. Default: `<MODEL-NAME>.tar.zst`
* `--step`,`-s` (integer, *optional*) -- Download a specific checkpoint's weights. Defaults to download the latest weights. Default: `-1`


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
