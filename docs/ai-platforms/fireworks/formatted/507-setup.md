---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

### `rewardkit.yaml` Configuration (Optional but Recommended)

The `reward-kit` CLI can pick up GCP settings from a `rewardkit.yaml` file located in the directory from which you run the `reward-kit deploy` command.

1. **Create `rewardkit.yaml`**:
   You can copy the `examples/gcp_cloud_run_deployment_example/rewardkit.example.yaml` to the directory where you intend to run `reward-kit deploy` (this could be the example directory itself, or your project root). Rename it to `rewardkit.yaml`.
```bash
   # If in examples/gcp_cloud_run_deployment_example/

   cp rewardkit.example.yaml rewardkit.yaml
```
2. **Customize `rewardkit.yaml`**:
   Open `rewardkit.yaml` and replace placeholders with your actual GCP Project ID and desired region.
   Example `rewardkit.yaml`:
```yaml
   gcp_cloud_run:
     project_id: "my-actual-gcp-project-123"
     region: "us-west1"
     # artifact_registry_repository: "my-custom-eval-repo" # Optional

     # default_auth_mode: "api-key" # Optional, defaults to api-key

   evaluator_endpoint_keys: {} # Managed by reward-kit for API key auth

```
**Note**: If you choose not to use a `rewardkit.yaml` file, you **must** provide all necessary GCP parameters (like `--gcp-project YOUR_PROJECT_ID`, `--gcp-region YOUR_REGION`) directly in the `reward-kit deploy` command.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
