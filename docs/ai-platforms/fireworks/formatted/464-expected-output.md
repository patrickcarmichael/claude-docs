---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Expected Output

The `reward-kit run` command will:

1. Load prompts based on the `apps_full_prompts` dataset configuration (typically from `development/CODING_DATASET.jsonl`).
2. If `generation.enabled` is `true` (default), generate code solutions using the configured model. Responses are cached (default: `outputs/generated_responses_cache_apps/`).
3. Evaluate each generated solution using the `evaluate_apps_solution` reward function (checking for Python AST parsability).
4. Print a summary of results to the console.
5. Save detailed evaluation results to a JSONL file in a timestamped directory. The default output path is configured in `run_eval.yaml` as `./outputs/apps_coding_example/${now:%Y-%m-%d}/${now:%H-%M-%S}`. The results file will be named `apps_coding_example_results.jsonl` within that directory.

The results file will contain the original prompt, generated response, the parsability score (0 or 1), and other metrics from the reward function.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
