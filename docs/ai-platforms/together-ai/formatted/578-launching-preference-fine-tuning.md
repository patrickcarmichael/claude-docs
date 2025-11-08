---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Launching preference fine-tuning

### Hyperparameters

* Set `--training-method="dpo"`

* The `--dpo-beta` parameter controls how much the model is allowed to deviate from its reference (or pre-tuned) model during fine-tuning. The default value is `0.1` but you can experiment with values between `0.05-0.9`

  * A lower value of beta (e.g., 0.1) allows the model to update more aggressively toward preferred responses
  * A higher value of beta(e.g., 0.7) keeps the updated model closer to the reference behavior.

* The `--dpo-normalize-logratios-by-length` parameter (optional, default is False) enables normalization of log ratios by sample length during the DPO loss calculation.

* The `--rpo-alpha` coefficient (optional, default is 0.0) incorporates the NLL loss on selected samples with the corresponding weight.

* The `--simpo-gamma` coefficient (optional, default is 0.0) adds a margin to the loss calculation, force-enables log ratio normalization (--dpo-normalize-logratios-by-length), and excludes reference logits from the loss computation. The resulting loss function is equivalent to the one used in the [SimPO](https://arxiv.org/pdf/2405.14734) paper.
```shell
  together fine-tuning create \
    --training-file $FILE_ID \
    --model "meta-llama/Llama-3.2-3B-Instruct" \
    --wandb-api-key $WANDB_API_KEY \
    --lora \
    --training-method "dpo" \
    --dpo-beta 0.2
```
```python
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
  file_id = "your-training-file"

  response = client.fine_tuning.create(
      training_file=file_id,
      model="meta-llama/Llama-3.2-3B-Instruct",
      lora=True,
      training_method="dpo",
      dpo_beta=0.2,
      rpo_alpha=1.0,
      simpo_gamma=1.0,
  )

  print(response)
```

>   **📝 Note**
>
>   **Note**

  * For [LoRA Long-context fine-tuning](/docs/fine-tuning-models#lora-long-context-fine-tuning) we currently use half of the context length for the preferred response and half for the non-preferred response. So, if you are using a 32K model, the effective context length will be 16K.
  * Preference fine-tuning calculates loss based on the preferred and non-preferred outputs. Therefore, the `--train-on-inputs` flag is ignored with preference fine-tuning.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
