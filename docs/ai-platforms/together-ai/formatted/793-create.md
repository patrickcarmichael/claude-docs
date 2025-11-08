---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create

To start a new fine-tune job:
```shell
  together fine-tuning create --training-file <FILE-ID> -m <MODEL>
```

Other arguments:

* `--model`,`-m` (string, *required*) -- Specifies the base model to fine-tune. (See [the model page](/docs/fine-tuning-models))
* `--training-file`,`-t` (string, *required*) -- Specifies a training file with the file-id of a previously uploaded file (See [Files](/docs/python-files)). The maximum allowed file size is 25GB.
* `--validation-file`,`-t` (string, *optional*) -- Specifies a validation file with the file-id of a previously uploaded file (See [Files](/docs/python-files)). The maximum allowed file size is 25GB.
* `--suffix`,`-s` (string, *optional*) -- Up to 40 characters that will be added to your fine-tuned model name. It is recommended to add this to differentiate fine-tuned models. Default: None.
* `--n-epochs`, `-ne` (integer, *optional*) -- Number of epochs to fine-tune on the dataset. Default: 4, Min: 1, Max: 20.
* `--n-evals` (integer, *optional*) -- Number of evaluations to be run on a given validation set during training. Default: 0, Min: 0, Max: 100.
* `--n-checkpoints`, `-c` (integer, *optional*) -- The number of checkpoints to save during training. Default: 1 One checkpoint is always saved on the last epoch for the trained model. The number of checkpoints must be larger than 0, and equal to or less than the number of epochs (1 \<= n-checkpoints \<= n-epochs). If a larger number is given, the number of epochs will be used for the number of checkpoints.
* `--batch-size`,`-b` (integer, *optional*) -- The batch size to use for each training iteration. The batch size is the number of training samples/examples used in a batch. See [the model page](/docs/fine-tuning-models) for min and max batch sizes for each model. By default `--batch-size max` is used by default when not specified.
* `--learning-rate`, `-lr` (float *optional*) -- The learning rate multiplier to use for training. Default: 0.00001, Min: 0.00000001, Max: 0.01
* `--lr-scheduler-type`, (string, *optional*) -- The learning rate scheduler type. One of `"linear"` or `"cosine"`. Defaults to `"linear"`.
* `--min-lr-ratio`, (float, *optional*) -- The ratio of the final learning rate to the peak learning rate. Default: 0.0, Min: 0.0, Max: 1.0.
* `--scheduler-num-cycles`, (float, *optional*) -- The number or fraction of cycles for the cosine learning rate scheduler. Must be non-negative. Default: 0.5
* `--warmup-ratio` (float, *optional*) -- The percent of steps at the start of training to linearly increase the learning rate. Default 0.0, Min: 0.0, Max: 1.0
* `--max-grad-norm` (float, *optional*) -- Max gradient norm to be used for gradient clipping. Set to 0 to disable. Default: 1.0, Min: 0.0
* `--weight-decay` (float, *optional*) -- Weight Decay parameter for the optimizer. Default: 0.0, Min: 0.0.
* `--wandb-api-key` (string, *optional*) -- Your own Weights & Biases API key. If you provide the key, you can monitor your job progress on your Weights & Biases page. If not set WANDB\_API\_KEY environment variable is used.
* `--wandb-base-url` (string, *optional*) -- The base URL of a dedicated Weights & Biases instance. Leave empty if not using your own Weights & Biases instance.
* `--wandb-project-name` (string, *optional*) -- The Weights & Biases project for your run. If not specified, will use `together` as the project name.
* `--wandb-name` (string, *optional*) -- The Weights & Biases name for your run.
* `--train-on-inputs` (bool or 'auto') -- Whether to mask the user messages in conversational data or prompts in instruction data. `'auto'` will automatically determine whether to mask the inputs based on the data format. For datasets with the `"text"` field (general format), inputs will not be masked. For datasets with the `"messages"` field (conversational format) or `"prompt"` and `"completion"` fields (Instruction format), inputs will be masked. Defaults to "auto".
* `--from-checkpoint` (str, *optional*) -- The checkpoint identifier to continue training from a previous fine-tuning job. The format: `{$JOB_ID/$OUTPUT_MODEL_NAME}:{$STEP}`. The step value is optional, without it the final checkpoint will be used.
* `--from-hf-model` (str, *optional*) -- The Hugging Face Hub repository to start training from. Should be as close as possible to the base model (specified by the `model` argument) in terms of architecture and size
* `--hf-model-revision` (str, *optional*) -- The revision of the Hugging Face Hub model to continue training from. Example: hf\_model\_revision=None (defaults to the latest revision in `main`) or hf\_model\_revision='607a30d783dfa663caf39e06633721c8d4cfcd7e' (specific commit).
* `--hf-api-token` (str, *optional*) -- Hugging Face API token for uploading the output model to a repository on the Hub or using a model from the Hub as initialization.
* `--hf-output-repo-name` (str, *optional*) -- HF repository to upload the fine-tuned model to.

(LoRA arguments are supported with `together >= 1.2.3`)

* `--lora` (bool, *optional*) -- Whether to enable LoRA training. If not provided, full fine-tuning will be applied. Default: False.

* `--lora-r` (integer, *optional*) -- Rank for LoRA adapter weights. Default: 8, Min: 1, Max: 64.

* `--lora-alpha` (integer, *optional*) -- The alpha value for LoRA adapter training. Default: 8. Min: 1. If a value less than 1 is given, it will default to `--lora-r` value to follow the recommendation of 1:1 scaling.

* `--lora-dropout` (float, *optional*) -- The dropout probability for Lora layers. Default: 0.0, Min: 0.0, Max: 1.0.

* `--lora-trainable-modules` (string, \_*optional*) -- A list of LoRA trainable modules, separated by a comma. Default: `all-linear`(using all trainable modules). Trainable modules for each model are:

  * Mixtral 8x7B model family: `k_proj`, `w2`, `w1`, `gate`, `w3`, `o_proj`, `q_proj`, `v_proj`
  * All other models: `k_proj`, `up_proj`, `o_proj`, `q_proj`, `down_proj`, `v_proj`, `gate_proj`

The `id` field in the JSON response contains the value for the fine-tune job ID (ft-id) that can be used to get the status, retrieve logs, cancel the job, and download weights.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
