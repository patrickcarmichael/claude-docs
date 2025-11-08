---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Importing fine-tuned models

In addition to models you fine-tune on the Fireworks platform, you can also upload your own custom fine-tuned models as LoRA adapters.

### Requirements

Your custom LoRA addon must contain the following files:

* `adapter_config.json` - The Hugging Face adapter configuration file
* `adapter_model.bin` or `adapter_model.safetensors` - The saved addon file

The `adapter_config.json` must contain the following fields:

* `r` - The number of LoRA ranks. Must be an integer between 4 and 64, inclusive
* `target_modules` - A list of target modules. Currently the following target modules are supported:
  * `q_proj`
  * `k_proj`
  * `v_proj`
  * `o_proj`
  * `up_proj` or `w1`
  * `down_proj` or `w2`
  * `gate_proj` or `w3`
  * `block_sparse_moe.gate`

Additional fields may be specified but are ignored.

### Enabling chat completions

To enable the chat completions API for your LoRA addon, add a `fireworks.json` file to the directory containing:
```json
{
  "conversation_config": {
    "style": "jinja",
    "args": {
      "template": "<YOUR_JINJA_TEMPLATE>"
    }
  }
}
```

### Uploading the LoRA adapter

To upload a LoRA addon, run the following command. The MODEL\_ID is an arbitrary [resource ID](/getting-started/concepts#resource-names-and-ids) to refer to the model within Fireworks.

>   **📝 Note**
>
> Only some base models support LoRA addons.
```bash
firectl create model <MODEL_ID> /path/to/files/ --base-model "accounts/fireworks/models/<BASE_MODEL_ID>"
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
