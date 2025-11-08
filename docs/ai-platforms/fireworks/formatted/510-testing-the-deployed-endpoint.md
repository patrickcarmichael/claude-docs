---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Testing the Deployed Endpoint

You can test the deployed endpoint using `curl` or `reward-kit preview --remote-url <your-cloud-run-url>`.

If using `curl` with API key authentication:

1. Retrieve the API key. It's printed during deployment and saved in `rewardkit.yaml` (if one is used in the command's directory) under `evaluator_endpoint_keys: { "my-dummy-gcp-evaluator": "YOUR_KEY" }`.
2. Get your Cloud Run service URL from the deployment output.
```bash
API_KEY="your_generated_api_key"
SERVICE_URL="your_cloud_run_service_url"

curl -X POST "$SERVICE_URL/evaluate" \
     -H "Content-Type: application/json" \
     -H "X-Api-Key: $API_KEY" \
     -d '{
           "messages": [{"role": "user", "content": "Test"}],
           "kwargs": {}
         }'
```
This should return a JSON response from your `hello_world_reward` function.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
