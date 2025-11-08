---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy the function to Fireworks

evaluation_id = my_reward_function.deploy(
    name="my-evaluator",
    description="Evaluates responses based on custom criteria",
    force=True  # Overwrite if already exists

)
```

### Deploy Method Parameters

* **`name`**: ID for the deployed evaluator (required)
* **`description`**: Human-readable description (optional)
* **`force`**: Whether to overwrite an existing evaluator with the same name (optional)
* **`providers`**: List of model providers to use for evaluation (optional)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
