---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy Command

The `deploy` command deploys a reward function as an evaluator on the Fireworks platform.

### Syntax

```bash
reward-kit deploy [options]
```

### Options

* `--id`: ID for the deployed evaluator (required)
* `--metrics-folders`: Specify metrics to use in the format "name=path" (required)
* `--display-name`: Human-readable name for the evaluator (optional)
* `--description`: Description of the evaluator (optional)
* `--force`: Overwrite if an evaluator with the same ID already exists (optional)
* `--providers`: List of model providers to use (optional)
* `--verbose`: Enable verbose output (optional)

### Examples

```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
