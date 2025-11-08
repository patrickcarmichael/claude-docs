---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Local Evaluation (`local_eval.py`)

This script performs local evaluation of a model's tool calling.

### Configuration

* Uses Hydra and is configured by `examples/tool_calling_example/conf/local_eval_config.yaml`.
* The default configuration points to `examples/tool_calling_example/dataset.jsonl`.
* The script itself likely contains defaults for the model and reward function, or expects them as CLI overrides.

### How to Run

1. Activate your virtual environment:
```bash
   source .venv/bin/activate
```
2. Execute from the repository root:
```bash
   python examples/tool_calling_example/local_eval.py
```

### Overriding Parameters

* **Change dataset path**:
```bash
  python examples/tool_calling_example/local_eval.py dataset_file_path=path/to/your/tool_calling_dataset.jsonl
```
* Other parameters (e.g., model name, reward function parameters) would typically be added to `local_eval_config.yaml` or passed as CLI overrides if `local_eval.py` is structured to accept them via Hydra.

Outputs are saved to Hydra's default output directory (configured in `local_eval_config.yaml` as `./outputs/local_eval_tool_calling/${now:%Y-%m-%d}/${now:%H-%M-%S}`).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
