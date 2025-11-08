---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an evaluation

evaluator = create_evaluation(
    evaluator_id="helpfulness-evaluator-low-level",
    metric_folders=["helpfulness=./path/to/your/metric_script_directory"], # Note: path to directory

    display_name="Helpfulness Evaluator (Low-Level)",
    description="Evaluates the helpfulness of responses, created via create_evaluation",
    force=True
)

print(f"Created evaluator: {evaluator['name']}")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
