---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy the function to Fireworks

evaluation_id = clarity_reward.deploy(
    name="clarity-evaluator",
    description="Evaluates the clarity of responses",
    force=True  # Overwrite if it already exists

)

print(f"Deployed evaluator with ID: {evaluation_id}")
```

### Using with Custom Providers

```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
