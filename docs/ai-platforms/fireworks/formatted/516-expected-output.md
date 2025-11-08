---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Expected Output

The command will:

1. Load the GSM8K dataset as configured by `gsm8k_math_with_formatting_prompts.yaml`.
2. Generate model responses using the specified model (default: `qwen3-235b-a22b`).
3. Evaluate responses using the logic in `examples.math_with_formatting.main.evaluate`, which combines accuracy and format checks.
4. Print a summary to the console.
5. Save detailed results to a JSONL file (e.g., `math_with_formatting_example_results.jsonl`) in a timestamped directory under `outputs/` (the exact path is determined by Hydra, typically based on the current date/time).
6. Save prompt/response pairs to `preview_input_output_pairs.jsonl` in the same output directory.

The results file will include the overall `evaluation_score` (average of accuracy and format) and a breakdown in `evaluation_metrics` for `accuracy_reward` and `format_reward`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
