---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Preview the outputs of a previous run

reward-kit preview \
  --samples ./outputs/YYYY-MM-DD/HH-MM-SS/preview_input_output_pairs.jsonl \
  --metrics-folders "new_metric=./path/to/new_metric_script"
  # Or --remote-url <your_deployed_evaluator_url>

```
This is useful for iterating on reward functions or comparing different evaluation approaches on the same set of generated responses.

### Programmatic Analysis

You can also load the `*.jsonl` result files programmatically (e.g., with Pandas) for custom analysis, plotting, or reporting.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
