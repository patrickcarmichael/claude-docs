---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tokenized Data

You can also provide tokenized data for more advanced use cases. You may want to use this data format if you are:

1. Using the same dataset for multiple experiments: this saves the tokenization step and accelerates your fine-tuning job.
2. Using a custom tokenizer that's intentionally different than the base model tokenizer
3. Masking out certain parts of your examples for the loss calculation (which are not covered by instruction or conversational dataset use cases above)

Your data file must meet the following requirements:

* The data file size must be under 25GB.
* The file format must be in the `.parquet` format.
* Allowed fields:
  * `input_ids`(required): List of token ids to be fed to a model.
  * `attention_mask`(required): List of indices specifying which tokens should be attended to by the model.
  * `labels`(optional): List of token ids to be used as target predictions. The default token ID to be ignored in the loss calculation is `-100`. To ignore certain predictions in the loss, replace their corresponding values with `-100`. If this field is not given, `input_ids` will be used.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
