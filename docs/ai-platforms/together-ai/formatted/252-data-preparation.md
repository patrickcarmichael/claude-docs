---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Data Preparation

Source: https://docs.together.ai/docs/fine-tuning-data-preparation

Together Fine-tuning API accepts two data formats for training dataset files: text data and tokenized data (in the form of Parquet files). Below, you can learn about different types of those formats and the scenarios in which they can be most useful.

Together Fine-tuning API accepts two data formats for training dataset files: text data and tokenized data (in the form of Parquet files). Below, you can learn about different types of those formats and the scenarios in which they can be most useful.

### Which file format should I use for data?

JSONL is simpler and will work for many cases, while Parquet stores pre-tokenized data, providing flexibility to specify custom attention mask and labels (loss masking). It also saves you time for each job you run by skipping the tokenization step.

By default, it's easier to use JSONL. However, there are a couple of things to keep in mind:

1. For JSONL training data, we use a variation of [sample packing](https://huggingface.co/docs/trl/main/en/reducing_memory_usage#packing) that improves training efficiency by utilizing the maximum context length via packing multiple examples together. This technique changes the effective batch size, making it larger than the specified batch size, and reduces the total number of training steps.\
   If you'd like to disable packing during training, you can provide a tokenized dataset in a Parquet file. [This example script](https://github.com/togethercomputer/together-python/blob/main/examples/tokenize_data.py#L34) for tokenizing a dataset demonstrates padding each example with a padding token. Note that the corresponding `attention_mask` and `labels` should be set to 0 and -100, respectively, so that the model ignores the padding tokens during prediction and excludes them from the loss calculation.
2. If you want to specify custom `attention_mask` values or apply some tokenization customizations unique to your setup, you can use the Parquet format as well.

**Note**: Regardless of the dataset format, the data file size must be under 25GB.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
