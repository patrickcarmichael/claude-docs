---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example

You can find an [example script ](https://github.com/togethercomputer/together-python/blob/main/examples/tokenize_data.py) that converts text data in Hugging Face Hub to the tokenized format.

In this example, we will use a toy dataset [clam004/antihallucination\_dataset](https://huggingface.co/datasets/clam004/antihallucination_dataset) in Hugging Face Hub with the tokenizer from `NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT`model. The max sequence length of this model is 32768. To compare the differences between packing and padding, we will run the script twice with and without `--packing`. When packing is not applied, each example will be (left-)padded with the tokenizer's own pad token to keep the length of all examples consistent. Note that packing is used during training by default, and we recommend to use packing during the tokenization step by passing `--packing` in the example script. Also note that we shift labels internally for model training and you do not need to do this.

* With packing,
```Text
python tokenize_data.py --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" --max-seq-length=32768 --add-labels --packing --out-filename="processed_dataset_packed.parquet"
```

`processed_dataset_packed.parquet` will be saved under the same directory.

* Without packing,
```Text
python tokenize_data.py --tokenizer="NousResearch/Nous-Hermes-2-Mixtral-8x7B-SFT" --max-seq-length=32768 --add-labels --out-filename="processed_dataset.parquet"
```

`processed_dataset_padded.parquet` will be saved under the same directory.

Let's load the generated files to see the results. In python,
```Text
>>> from datasets import load_dataset
>>> dataset_packed = load_dataset("parquet", data_files={'train': 'processed_dataset_packed.parquet'})
>>> dataset_padded = load_dataset("parquet", data_files={'train': 'processed_dataset_padded.parquet'})
```

First, you will see the number of examples from the dataset with packing is only 6 while the one without packing has 238:
```Text
>>> dataset_packed['train']
Dataset({
    features: ['input_ids', 'attention_mask', 'labels'],
    num_rows: 6
})
>>> dataset_padded['train']
Dataset({
    features: ['input_ids', 'attention_mask', 'labels'],
    num_rows: 238
})
```

In the first example of `dataset_padded` you will find the first 31140 tokens are padded and have `-100` as their labels to be ignored during the loss mask. The pad token for this tokenizer is `32000`
```python
{
    "input_ids": [32000, 32000, 32000, ..., 3409, 6898, 28767],
    "attention_masks": [0, 0, 0, ..., 1, 1, 1],
    "labels": [-100, -100, -100, ..., 3409, 6898, 28767],
}
```

On the other hand, in the first example of `dataset_packed`, no padding is used. And the first 1628 token ids match the last 1628 token ids from the first example of `dataset_padded`.
```text
{
  "input_ids": [1, 523, 434, ..., 6549, 3805, 7457],
  "attention_masks": [1, 1, 1, ..., 1, 1, 1],
  "labels": [1, 523, 434,..., 6549, 3805, 7457]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
