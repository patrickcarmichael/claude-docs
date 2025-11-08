---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Combining methods: supervised fine-tuning & preference fine-tuning

Supervised fine-tuning (SFT) is the default method on our platform. The recommended approach is to first perform SFT followed up by preference tuning as follows:

1. First perform [supervised fine-tuning (SFT)](/docs/finetuning) on your data.
2. Then refine with preference fine-tuning using [continued fine-tuning](/docs/finetuning#continue-a-fine-tuning-job) on your SFT checkpoint.

Performing SFT on your dataset prior to DPO can significantly increase the resulting model quality, especially if your training data differs significantly from the data the base model observed during pretraining. To perform SFT, you can concatenate the context with the preferred output and use one of our [SFT data formats](/docs/fine-tuning-data-preparation#data-formats) .


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
