---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Start finetuning

Once the dataset is validated, we can start a finetuning job with the [Finetuning API](https://docs.cohere.com/reference/createfinetunedmodel).

### Hyperparameters

There are several hyperparameters that you can modify to get the most out of your finetuning, including LoRA-specific params. You can find detailed explanation [here](https://docs.cohere.com/reference/createfinetunedmodel#request.body.settings.hyperparameters).
```python
hp_config = Hyperparameters(
    train_batch_size=16,
    train_epochs=1,
    learning_rate=0.0001,
)
```
<a id="sec_wandb" />

### WandB integration

For chat finetuning, we support WandB integration which allows you to monitor the loss curves of finetuning jobs in real-time without having to wait for the job to finish. You can find more info [here](https://docs.cohere.com/reference/createfinetunedmodel#request.body.settings.wandb).
```python
wnb_config = WandbConfig(
    project="test-project",
    api_key="<wandb_api_key>",
    entity="test-entity",  # must be a valid enitity associated with the provided API key

)
```

### Create the finetuning job

With the dataset, hyperparameters, and the wandb configurations ready, we can create a fientuning job as follows. You can find the details of all params in the [Finetuning API](https://docs.cohere.com/reference/createfinetunedmodel#request) documentation.
```python
cfqa_finetune = co.finetuning.create_finetuned_model(
    request=FinetunedModel(
        name="cfqa-command-r-ft",
        settings=Settings(
            base_model=BaseModel(
                base_type="BASE_TYPE_CHAT",  # specifies this is a chat finetuning

            ),
            dataset_id=chat_dataset.id,  # the id of the dataset we created above

            hyperparameters=hp_config,
            wandb=wnb_config,
        ),
    ),
)
print(
    cfqa_finetune.finetuned_model.id
)  # we will use this id to refer to the finetuned model when making predictions/getting status/etc.

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
