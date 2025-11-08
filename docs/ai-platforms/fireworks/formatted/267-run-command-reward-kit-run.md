---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run Command (`reward-kit run`)

The `run` command is the primary way to execute local evaluation pipelines. It leverages Hydra for configuration, allowing you to define complex evaluation setups (including dataset loading, model generation, and reward application) in YAML files and easily override parameters from the command line.

### Syntax

```bash
python -m reward_kit.cli run [options] [HYDRA_OVERRIDES...]
```
or
```bash
reward-kit run [options] [HYDRA_OVERRIDES...]
```

### Key Options

* `--config-path TEXT`: Path to the directory containing your Hydra configuration files. (Required)
* `--config-name TEXT`: Name of the main Hydra configuration file (e.g., `run_my_eval.yaml`). (Required)
* `--multirun` or `-m`: Run multiple jobs (e.g., for sweeping over parameters). Refer to Hydra documentation for multi-run usage.
* `--help`: Show help message for the `run` command.

### Hydra Overrides

You can override any parameter defined in your Hydra configuration YAML files directly on the command line. For detailed information on how Hydra is used, refer to the [Hydra Configuration for Examples guide](/evaluators/developer_guide/hydra_configuration).

### Examples

```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
