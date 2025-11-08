---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running the Evaluation

The primary configuration for this example is `examples/math_with_formatting/conf/run_math_with_formatting_eval.yaml`.

1. Activate your virtual environment:
```bash
   source .venv/bin/activate
```
2. Execute the `reward-kit run` command from the root of the repository:
```bash
   reward-kit run --config-path examples/math_with_formatting/conf --config-name run_math_with_formatting_eval
```

### Overriding Parameters

You can modify parameters via the command line. For instance:

* **Limit samples**:
```bash
  reward-kit run --config-path examples/math_with_formatting/conf --config-name run_math_with_formatting_eval evaluation_params.limit_samples=5
```
  (The default in the example config is `limit_samples: 2`).
* **Change generation model**:
```bash
  reward-kit run --config-path examples/math_with_formatting/conf --config-name run_math_with_formatting_eval generation.model_name="accounts/fireworks/models/mixtral-8x7b-instruct"
```
For more on Hydra, see the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
