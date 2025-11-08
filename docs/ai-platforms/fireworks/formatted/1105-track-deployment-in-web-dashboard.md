---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Track deployment in web dashboard

print(f"Track at: {fine_tuned_llm.deployment_url}")
```typescript
>   **📝 Note**
>
> The `id` parameter can be any simple string - it does not need to follow the format `"accounts/account_id/deployments/model_id"`.

### Resource signatures

Each resource has a signature, which is the set of properties that are used to identify the resource. The SDK will use the signature to determine if a resource already exists and can be re-used.

| Resource                  | Signature                   |
| ------------------------- | --------------------------- |
| `LLM`                     | `id`                        |
| `Dataset`                 | `hash(data)` and `filename` |
| `SupervisedFineTuningJob` | `name` and `model`          |

For `LLM` resources, the resource signature is based on the `id` parameter. When using `deployment_type="on-demand"`, you must provide a unique `id` to identify your deployment.

For `Dataset` resources, the resource signature is derived from the `filename` of your dataset (if created via `from_file()`) and the hash of the data itself.

For `SupervisedFineTuningJob` resources, you are required to pass a `name` when creating the resource.

### Resource management

The SDK also tries to be parsimonious with the *number* of resources it creates. Before creating a resource, the SDK will first check if a resource with the same signature already exists. If so, the SDK will re-use the existing resource instead of creating a new one. This could mean updating the resource with new configuration parameters, or re-using the existing resource.

A new resource will be created in the following cases for each resource type:

| Resource                  | Created by SDK if...                                                               |
| ------------------------- | ---------------------------------------------------------------------------------- |
| `LLM`                     | You pass a unique `id` to the constructor                                          |
| `Dataset`                 | You change the `filename` of the data or modify the data itself                    |
| `SupervisedFineTuningJob` | You pass a unique `name` when creating the fine-tuning job or use a unique `model` |


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
