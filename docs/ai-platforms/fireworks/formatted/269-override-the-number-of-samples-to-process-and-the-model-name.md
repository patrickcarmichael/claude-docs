---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Override the number of samples to process and the model name

python -m reward_kit.cli run \
  --config-path examples/math_example/conf \
  --config-name run_math_eval.yaml \
  evaluation_params.limit_samples=10 \
  generation.model_name="accounts/fireworks/models/mixtral-8x7b-instruct"
```

### Output

The `run` command typically generates:

* A timestamped output directory (e.g., `outputs/YYYY-MM-DD/HH-MM-SS/`).
* Inside this directory:
  * `.hydra/`: Contains the full Hydra configuration for the run (for reproducibility).
  * Log files.
  * Result files, often including:
    * `<config_output_name>_results.jsonl` (e.g., `math_example_results.jsonl`): Detailed evaluation results for each sample.
    * `preview_input_output_pairs.jsonl`: Generated prompts and responses, suitable for use with `reward-kit preview`.
  * Console Output:
    * A summary report is logged to the console, including:
      * Total samples processed.
      * Number of successful evaluations.
      * Number of evaluation errors.
      * Average, min, and max scores (if applicable).
      * Score distribution.
      * Details of the first few errors encountered.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
