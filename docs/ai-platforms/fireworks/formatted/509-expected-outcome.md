---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Expected Outcome

If successful, `reward-kit` will:

1. Create an Artifact Registry repository (default: `reward-kit-evaluators`, or as specified in `rewardkit.yaml`).
2. Build a Docker container with your reward function and push it to Artifact Registry.
3. If `api-key` auth is used, create a GCP Secret to store the generated API key.
4. Deploy the container to Cloud Run, configured for the chosen authentication mode.
5. Register the deployed Cloud Run service URL as a remote evaluator with the Fireworks AI platform.

The output will include the Cloud Run service URL and the API key (if newly generated).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
