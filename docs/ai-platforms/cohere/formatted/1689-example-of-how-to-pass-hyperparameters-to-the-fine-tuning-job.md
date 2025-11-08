---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example of how to pass hyperparameters to the fine-tuning job

train_parameters = {
    "train_epochs": 1,
    "early_stopping_patience": 2,
    "early_stopping_threshold": 0.001,
    "learning_rate": 0.01,
    "train_batch_size": 16,
}
```
Create fine-tuning jobs for the uploaded datasets. Add a field for `eval_data` if you have pre-split your dataset and uploaded both training and evaluation datasets to S3. Remember to use p4de for Command-R Finetuning.
```python
finetune_name = "test-finetune"
co.sagemaker_finetuning.create_finetune(
    arn=arn,
    name=finetune_name,
    train_data=train_dataset,
    eval_data=eval_dataset,
    s3_models_dir=s3_models_dir,
    instance_type="ml.p4de.24xlarge",
    training_parameters=train_parameters,
    role="ServiceRoleSagemaker",
)
```
The finetuned weights for the above will be store in a tar file `{s3_models_dir}/test-finetune.tar.gz` where the file name is the same as the name used during the creation of the finetune.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
