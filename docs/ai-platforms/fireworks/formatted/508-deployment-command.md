---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deployment Command

It's recommended to run the deployment command from the directory containing the reward function script (`dummy_rewards.py`) and your `rewardkit.yaml` (if used), for example, from `examples/gcp_cloud_run_deployment_example/`.

1. Ensure your virtual environment is active:
```bash
   source .venv/bin/activate
```
2. Run the deployment command:
```bash
   reward-kit deploy \
       --id my-dummy-gcp-evaluator \
       --target gcp-cloud-run \
       --function-ref dummy_rewards.hello_world_reward \
       --gcp-auth-mode api-key \
       --verbose
       # --force # Add if overwriting an existing evaluator

       # If not using rewardkit.yaml, add required GCP params:

       # --gcp-project YOUR_PROJECT_ID --gcp-region YOUR_REGION

```typescript
**Command Explanation:**

* `--id my-dummy-gcp-evaluator`: A unique ID for your evaluator on the Fireworks AI platform.
* `--target gcp-cloud-run`: Specifies deployment to GCP Cloud Run.
* `--function-ref dummy_rewards.hello_world_reward`: The Python import path to your reward function. If `dummy_rewards.py` is in the current directory, this reference works.
* `--gcp-auth-mode api-key`: Configures the Cloud Run service with API key authentication. `reward-kit` will generate a key, store it in GCP Secret Manager, and configure the service. The key is also saved to your local `rewardkit.yaml` under `evaluator_endpoint_keys`. This is the default if not specified.
* `--verbose`: Shows detailed output, including `gcloud` commands being executed.
* `--force`: (Optional) If an evaluator with the same `--id` already exists, this flag will delete the existing one before creating the new one.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
