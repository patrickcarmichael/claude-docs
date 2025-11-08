---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Starting a Fine-tuning Job

With our data uploaded, we can now launch the fine-tuning job using `client.fine_tuning.create()`.

**Key Parameters**

* `model`: The base model you want to fine-tune (e.g., `'meta-llama/Meta-Llama-3.1-8B-Instruct-Reference'`)
* `training_file`: The ID of your uploaded training JSONL file
* `validation_file`: Optional ID of validation file (highly recommended for monitoring)
* `suffix`: A custom string added to create your unique model name (e.g., `'test1_8b'`)
* `n_epochs`: Number of times the model sees the entire dataset
* `n_checkpoints`: Number of checkpoints to save during training (for resuming or selecting the best model)
* `learning_rate`: Controls how much model weights are updated
* `batch_size`: Number of examples processed per iteration (default: "max")
* `lora`: Set to `True` for LoRA fine-tuning
* `train_on_inputs`: Whether to mask user messages or prompts (can be bool or 'auto')
* `warmup_ratio`: Ratio of steps for warmup

<Icon icon="link" iconType="solid" /> For an exhaustive list of all the available
fine-tuning parameters refer to the [Together AI Fine-tuning API Reference](/reference/post-fine-tunes)
docs.

**LoRA Fine-tuning (Recommended)**
```python
  ## Using Python - This fine-tuning job should take ~10-15 minutes to complete

  ft_resp = client.fine_tuning.create(
      training_file=train_file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      train_on_inputs="auto",
      n_epochs=3,
      n_checkpoints=1,
      wandb_api_key=WANDB_API_KEY,  # Optional, for visualization

      lora=True,  # Default True

      warmup_ratio=0,
      learning_rate=1e-5,
      suffix="test1_8b",
  )

  print(ft_resp.id)  # Save this job ID for monitoring

```
```bash
  ## Using CLI

  together fine-tuning create \
    --training-file "file-id-from-upload" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --train-on-inputs auto \
    --lora \
    --n-epochs 3 \
    --n-checkpoints 1 \
    --warmup-ratio 0 \
    --learning-rate 1e-5 \
    --suffix "test1_8b" \
    --wandb-api-key $WANDB_API_KEY  # Optional

```

**Full Fine-tuning**

For full fine-tuning, simply omit the `lora` parameter:
```python
  ## Using Python

  ft_resp = client.fine_tuning.create(
      training_file=train_file_resp.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      train_on_inputs="auto",
      n_epochs=3,
      n_checkpoints=1,
      warmup_ratio=0,
      lora=False,  # Must be specified as False, defaults to True

      learning_rate=1e-5,
      suffix="test1_8b_full_finetune",
  )
```
```bash
  ## Using CLI

  together fine-tuning create \
    --training-file "file-id-from-upload" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --train-on-inputs auto \
    --n-epochs 3 \
    --n-checkpoints 1 \
    --warmup-ratio 0 \
    --no-lora \
    --learning-rate 1e-5 \
    --suffix "test1_8b_full_finetune"
```

The response will include your job ID, which you'll use to monitor progress:
```text
ft-d1522ffb-8f3e #fine-tuning job id
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
