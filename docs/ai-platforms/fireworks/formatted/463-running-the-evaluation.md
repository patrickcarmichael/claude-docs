---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running the Evaluation

The evaluation is configured in `examples/apps_coding_example/conf/run_eval.yaml`. This is the main configuration file used by Hydra.

To run the evaluation using the `reward-kit run` command:

1. Ensure your virtual environment is activated:
```bash
   source .venv/bin/activate
```
2. Execute the run command from the root of the repository:
```bash
   reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval
```

### Overriding Parameters

You can override parameters from the `run_eval.yaml` configuration directly from the command line. For example:

* **Limit the number of samples for a quick test**:
```bash
  reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval evaluation_params.limit_samples=2
```
* **Disable code generation (to test reward function with cached responses)**:
  If you have previously run the example and responses are cached (default cache dir: `outputs/generated_responses_cache_apps/`), you can disable new generation:
```bash
  reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval generation.enabled=false
```
* **Change the generation model**:
```bash
  reward-kit run --config-path examples/apps_coding_example/conf --config-name run_eval generation.model_name="accounts/fireworks/models/another-model"
```
Refer to the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration) for more details on Hydra.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
