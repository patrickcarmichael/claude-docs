---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy with the CLI

reward-kit deploy \
  --id helpfulness-evaluator \
  --metrics-folders "helpfulness=./path/to/your/metric_script_directory" \
  --display-name "Helpfulness Evaluator" \
  --description "Evaluates the helpfulness of responses" \
  --force
```
For more details on `reward-kit deploy`, see the [CLI Reference](/evaluators/cli_reference/cli_overview).

### Lower-level `create_evaluation` Function

For more direct control, or if not using the `@reward_function` decorator's `deploy` method, you can use the `create_evaluation` function from `reward_kit.evaluation`. This is generally for more advanced use cases or internal tooling.
```python
from reward_kit.evaluation import create_evaluation

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
