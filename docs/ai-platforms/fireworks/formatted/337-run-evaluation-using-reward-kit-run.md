---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run evaluation using reward-kit run

python -m reward_kit.cli run \
  --config-path ./path/to/your/example/conf \
  --config-name run_my_eval.yaml \
  evaluation_params.limit_samples=50 # Example override

```
This command will:

* Load the dataset as per your configuration.
* Generate responses from the specified model.
* Apply the configured reward function(s).
* Save detailed results (e.g., `run_my_eval_results.jsonl`) and prompt/response pairs (e.g., `preview_input_output_pairs.jsonl`) to a timestamped output directory (usually under `outputs/`).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
