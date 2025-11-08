---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Agent-Eval Command

The `agent-eval` command enables you to run agent evaluations using task bundles.

### Syntax

```bash
reward-kit agent-eval [options]
```typescript

### Options

#### Task Specification:

* `--task-dir`: Path to task bundle directory containing reward.py, tools.py, etc.
* `--dataset` or `-d`: Path to JSONL file containing task specifications.

#### Output and Models:

* `--output-dir` or `-o`: Directory to store evaluation runs (default: "./runs").
* `--model`: Override MODEL\_AGENT environment variable.
* `--sim-model`: Override MODEL\_SIM environment variable for simulated user.

#### Testing and Debugging:

* `--no-sim-user`: Disable simulated user (use static initial messages only).
* `--test-mode`: Run in test mode without requiring API keys.
* `--mock-response`: Use a mock agent response (works with --test-mode).
* `--debug`: Enable detailed debug logging.
* `--validate-only`: Validate task bundle structure without running evaluation.
* `--export-tools`: Export tool specifications to directory for manual testing.

#### Advanced Options:

* `--task-ids`: Comma-separated list of task IDs to run.
* `--max-tasks`: Maximum number of tasks to evaluate.
* `--registries`: Custom tool registries in format 'name=path'.
* `--registry-override`: Override all toolset paths with this registry path.
* `--evaluator`: Custom evaluator module path (overrides default).

### Examples

**Note**: The following examples use `examples/your_agent_task_bundle/` as a placeholder. You will need to replace this with the actual path to your task bundle directory.
```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
