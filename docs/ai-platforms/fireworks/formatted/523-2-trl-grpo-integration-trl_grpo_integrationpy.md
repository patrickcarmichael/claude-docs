---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. TRL GRPO Integration (`trl_grpo_integration.py`)

This script provides a scaffold for fine-tuning a model for tool calling using TRL GRPO.
**Note**: The script defaults to using a MOCK model and tokenizer. Using a real model requires code modifications in `trl_grpo_integration.py` and potentially `conf/trl_grpo_config.yaml`.

### Configuration

* Uses Hydra and is configured by `examples/tool_calling_example/conf/trl_grpo_config.yaml`.
* Default `dataset_file_path`: `dataset.jsonl` (assumed to be in `examples/tool_calling_example/`).
* Default `model_name`: `Qwen/Qwen2-0.5B-Instruct`.
* Includes various `grpo` training parameters.

### How to Run (with Mock Model by default)

1. Activate your virtual environment:
```bash
   source .venv/bin/activate
```
2. Execute from the repository root:
```bash
   python examples/tool_calling_example/trl_grpo_integration.py
```

### Overriding Parameters

* **Change dataset path or training epochs**:
```bash
  python examples/tool_calling_example/trl_grpo_integration.py dataset_file_path=my_tool_train.jsonl grpo.num_train_epochs=1
```

### Using a Real Model (Requires Code Changes)

1. Modify `examples/tool_calling_example/trl_grpo_integration.py` to load your desired Hugging Face model and tokenizer (remove or conditionalize the mock model parts).
2. Ensure the prompt formatting in the script is suitable for your chosen model.
3. Update `conf/trl_grpo_config.yaml` with the correct `model_name` and adjust training parameters.
4. Run the script. If you added a flag like `use_mock_model_tokenizer` in the script/config, you might run:
```bash
   python examples/tool_calling_example/trl_grpo_integration.py +use_mock_model_tokenizer=false model_name=your-hf-model-name
```
Outputs are saved to Hydra's default output directory (configured in `trl_grpo_config.yaml` as `./outputs/trl_grpo_tool_calling/${now:%Y-%m-%d}/${now:%H-%M-%S}`).

For more general information on Hydra, see the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
