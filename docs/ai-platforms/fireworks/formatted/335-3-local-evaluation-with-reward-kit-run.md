---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Local Evaluation with `reward-kit run`

The primary method for running local evaluations is the `reward-kit run` CLI command, which uses Hydra for configuration. This command handles generating model responses (if needed) and evaluating them according to your specified dataset and reward logic.

### Setting up the Configuration

You'll need a main evaluation configuration YAML file (e.g., `run_my_eval.yaml`) that specifies:

* The dataset to use (referencing configurations from `conf/dataset/`).
* Model generation parameters (model name, API keys, etc.).
* The reward function or evaluation script to use.
* Other evaluation parameters (e.g., sample limits).

Refer to the [Hydra Configuration for Examples](/evaluators/developer_guide/hydra_configuration) guide and specific examples like `examples/math_example/conf/run_math_eval.yaml`.

### Running the Evaluation

```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
