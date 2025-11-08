---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## DO NOT add a trailing slash at the end

s3_models_dir = f"s3://..."
```
Create Cohere client:
```python
co = cohere.SagemakerClient(region_name=region)
```

#### Optional: Define hyperparameters

* `train_epochs`: Integer. This is the maximum number of training epochs to run for. Defaults to **1**

| Default | Min | Max |
| ------- | --- | --- |
| 1       | 1   | 10  |

* `learning_rate`: Float. The initial learning rate to be used during training. Default to **0.0001**

| Default | Min      | Max |
| ------- | -------- | --- |
| 0.0001  | 0.000005 | 0.1 |

* `train_batch_size`: Integer. The batch size used during training. Defaults to **16** for Command.

| Default | Min | Max |
| ------- | --- | --- |
| 16      | 8   | 32  |

* `early_stopping_enabled`: Boolean. Enables early stopping. When set to true, the final model is the best model found based on the validation set. When set to false, the final model is the last model of training. Defaults to **true**.

* `early_stopping_patience`: Integer. Stop training if the loss metric does not improve beyond 'early\_stopping\_threshold' for this many times of evaluation. Defaults to **10**

| Default | Min | Max |
| ------- | --- | --- |
| 10      | 1   | 15  |

* `early_stopping_threshold`: Float. How much the loss must improve to prevent early stopping. Defaults to **0.001**.

| Default | Min   | Max |
| ------- | ----- | --- |
| 0.001   | 0.001 | 0.1 |

If the algorithm is **command-r-0824-ft**, you have the option to define:

* `lora_rank': Integer`. Lora adapter rank. Defaults to **32**

| Default | Min | Max |
| ------- | --- | --- |
| 32      | 8   | 32  |
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
