---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Check finetuning status

Once the finetuning job finishes and the finetuned model is ready to use, you will get notified via email. Or you can check of the status of your finetuning job as follows.
```python
response = co.finetuning.get_finetuned_model(
    cfqa_finetune.finetuned_model.id
)
print(
    response.finetuned_model.status
)  # when the job finished this will be STATUS_READY

```
You may view the fine-tuning job loss curves via the Weights and Biases dashboard. It will be available via the following URL once the training starts: `https://wandb.ai/<your-entity>/<your-project>/runs/<finetuned-model-id>`. We log the following to WandB:

* training loss at every training step
* validation loss and accuracy (as described [here](https://docs.cohere.com/docs/chat-understanding-the-results)) at every validation step

For this particular fientuning job, the traning loss, validation loss and validation accuracy should look as follows.

Once the training job finished you can also check the validation metrics as follows.
```python
train_step_metrics = co.finetuning.list_training_step_metrics(
    finetuned_model_id=cfqa_finetune.finetuned_model.id
)

for metric in train_step_metrics.step_metrics:
    print(metric.metrics)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
