---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Get the merged weights

Assuming you use HuggingFace's [PEFT](https://github.com/huggingface/peft) to finetune [CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) and get the adapter weights, you can then merge your adapter weights to the base model weights to get the merged weights as shown below. Skip this step if you have already got the merged weights.
```python
import torch

from peft import PeftModel
from transformers import CohereForCausalLM


def load_and_merge_model(
    base_model_name_or_path: str, adapter_weights_dir: str
):
    """
    Load the base model and the model finetuned by PEFT, and merge the adapter weights to the base weights to get a model with merged weights
    """
    base_model = CohereForCausalLM.from_pretrained(
        base_model_name_or_path
    )
    peft_model = PeftModel.from_pretrained(
        base_model, adapter_weights_dir
    )
    merged_model = peft_model.merge_and_unload()
    return merged_model


def save_hf_model(output_dir: str, model, tokenizer=None, args=None):
    """
    Save a HuggingFace model (and optionally tokenizer as well as additional args) to a local directory
    """
    os.makedirs(output_dir, exist_ok=True)
    model.save_pretrained(
        output_dir, state_dict=None, safe_serialization=True
    )
    if tokenizer is not None:
        tokenizer.save_pretrained(output_dir)
    if args is not None:
        torch.save(
            args, os.path.join(output_dir, "training_args.bin")
        )
```
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
