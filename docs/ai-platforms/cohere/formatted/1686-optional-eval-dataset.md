---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## optional eval dataset

eval_dataset = S3Uploader.upload(
    "./scienceQA_eval.jsonl", s3_data_dir, sagemaker_session=sess
)
print("traint_dataset", train_dataset)
print("eval_dataset", eval_dataset)
```
**Note:** If eval dataset is absent, we will auto-split the training dataset into training and evaluation datasets with the ratio of 80:20.

Each dataset must contain at least 1 examples. If an evaluation dataset is absent, training dataset must cointain at least 2 examples.

We recommend using a dataset than contains at least 100 examples but a larger dataset is likely to yield high quality finetunes. Be aware that a larger dataset would mean that the time to finetune would also be longer.

Specify a directory on S3 where finetuned models should be stored. **Make sure you *do not reuse the same directory* across multiple runs.**
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
