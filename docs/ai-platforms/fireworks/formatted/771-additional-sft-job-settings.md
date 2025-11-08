---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Additional SFT job settings

Additional tuning settings are available when starting a fine-tuning job. All of the below settings are optional and will have reasonable defaults if not specified. For settings that affect tuning quality like `epochs` and `learning rate`, we recommend using default settings and only changing hyperparameters if results are not as desired.

<AccordionGroup>
  <Accordion title="Evaluation">
    By default, the fine-tuning job will run evaluation by running the fine-tuned model against an evaluation set that's created by automatically carving out a portion of your training set. You have the option to explicitly specify a separate evaluation dataset to use instead of carving out training data.

    `evaluation_dataset`: The ID of a separate dataset to use for evaluation. Must be pre-uploaded via firectl
```shell
    firectl create sftj \
      --evaluation-dataset my-eval-set \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="Early stopping">
    Early stopping stops training early if the validation loss does not improve. It is off by default.
```shell
    firectl create sftj \
      --early-stop \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="Max Context Length">
    By default, fine-tuned models support a max context length of 8k. Increase max context length if your use case requires context above 8k. Maximum context length can be increased up to the default context length of your selected model. For models with over 70B parameters, we only support up to 65536 max context length.
```shell
    firectl create sftj \
      --max-context-length 65536 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="Epochs">
    Epochs are the number of passes over the training data. Our default value is 1. If the model does not follow the training data as much as expected, increase the number of epochs by 1 or 2. Non-integer values are supported.

    **Note: we set a max value of 3 million dataset examples × epochs**
```shell
    firectl create sftj \
      --epochs 2.0 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="Learning rate">
    Learning rate controls how fast the model updates from data. We generally do not recommend changing learning rate. The default value is automatically based on your selected model.
```shell
    firectl create sftj \
      --learning-rate 0.0001 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="LoRA Rank">
    LoRA rank refers to the number of parameters that will be tuned in your LoRA add-on. Higher LoRA rank increases the amount of information that can be captured while tuning. LoRA rank must be a power of 2 up to 64. Our default value is 8.
```shell
    firectl create sftj \
      --lora-rank 16 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="Training progress and monitoring">
    The fine-tuning service integrates with Weights & Biases to provide observability into the tuning process. To use this feature, you must have a Weights & Biases account and have provisioned an API key.
```shell
    firectl create sftj \
      --wandb-entity my-org \
      --wandb-api-key xxx \
      --wandb-project "My Project" \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="Model ID">
    By default, the fine-tuning job will generate a random unique ID for the model. This ID is used to refer to the model at inference time. You can optionally specify a custom ID, within [ID constraints](/getting-started/concepts#resource-names-and-ids).
```shell
    firectl create sftj \
      --output-model my-model \
      --base-model MY_BASE_MODEL \
      --dataset cancerset
```
  </Accordion>

  <Accordion title="Job ID">
    By default, the fine-tuning job will generate a random unique ID for the fine-tuning job. You can optionally choose a custom ID.
```shell
    firectl create sftj \
      --job-id my-fine-tuning-job \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>

  <Accordion title="Turbo Mode">
    By default, the fine-tuning job will use a single GPU. You can optionally enable the turbo mode to accelerate with multiple GPUs (only for non-Deepseek models).
```shell
    firectl create sftj \
      --turbo \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
```
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
