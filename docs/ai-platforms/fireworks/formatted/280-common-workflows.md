---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common Workflows

### Iterative Development Workflow

A typical development workflow using the CLI now often involves `reward-kit run` first:

1. **Configure**: Set up your dataset and evaluation parameters in Hydra YAML files (e.g., `conf/dataset/my_data.yaml`, `conf/run_my_eval.yaml`). Define or reference your reward function logic.
2. **Run**: Execute the evaluation pipeline using `reward-kit run`. This generates model responses and initial scores.
```bash
   python -m reward_kit.cli run --config-path ./conf --config-name run_my_eval.yaml
```
3. **Analyze & Iterate**:
   * Examine the detailed results (`*_results.jsonl`) and the `preview_input_output_pairs.jsonl` from the output directory.
   * If iterating on reward logic, you can use `reward-kit preview` with the `preview_input_output_pairs.jsonl` and your updated local metric script.
```bash
   reward-kit preview \
     --samples ./outputs/YYYY-MM-DD/HH-MM-SS/preview_input_output_pairs.jsonl \
     --metrics-folders "my_refined_metric=./path/to/refined_metric"
```
   * Refine your reward function code or Hydra configurations.
4. **Re-run**: If configurations changed significantly or you need new model generations, re-run `reward-kit run`.
5. **Deploy**: Once satisfied with the evaluator's performance and configuration:
```bash
   reward-kit deploy --id my-evaluator-id \
     --metrics-folders "my_final_metric=./path/to/final_metric" \
     --display-name "My Final Evaluator" \
     --description "Description of my evaluator" \
     --force
```
   *(Note: The `--metrics-folders` for `deploy` should point to the finalized reward function script(s) you intend to deploy as the evaluator.)*

### Comparing Multiple Metrics

You can preview multiple metrics to compare their performance:
```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
