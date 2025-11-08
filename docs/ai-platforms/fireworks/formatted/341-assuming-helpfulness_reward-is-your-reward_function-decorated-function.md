---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Assuming 'helpfulness_reward' is your @reward_function decorated function

evaluation_id = helpfulness_reward.deploy(
    name="helpfulness-evaluator", # This will be the evaluator_id

    description="Evaluates the helpfulness of responses",
    force=True  # Overwrite if an evaluator with this name already exists

)

print(f"Deployed helpfulness evaluator with ID: {evaluation_id}")
```
You can also specify providers if needed:
```python
custom_evaluation_id = helpfulness_reward.deploy(
    name="helpfulness-evaluator-anthropic",
    description="Helpfulness evaluation using Claude model",
    force=True,
    providers=[
        {
            "providerType": "anthropic",
            "modelId": "claude-3-sonnet-20240229"
        }
    ]
)
print(f"Deployed custom provider evaluator: {custom_evaluation_id}")
```

### Using the CLI (`reward-kit deploy`)

The `reward-kit deploy` command is suitable for deploying reward functions defined in script files. The `--metrics-folders` argument should point to the directory containing your reward function script (e.g., a `main.py` with the `@reward_function` decorator).
```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
