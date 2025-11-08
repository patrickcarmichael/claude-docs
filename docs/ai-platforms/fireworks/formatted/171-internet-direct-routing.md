---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Internet direct routing

Internet direct routing bypasses our global API load balancer and directly routes your request to the machines where
your deployment is running. This can save several tens or even hundreds of milliseconds of time-to-first-token (TTFT)
latency.

To create a deployment using Internet direct routing:

>   **📝 Note**
>
> When creating a deployment with direct routing, the `--region` parameter is required to specify the deployment region.
```bash
$ firectl create deployment accounts/fireworks/models/llama-v3p1-8b-instruct \
    --direct-route-type INTERNET \
    --direct-route-api-keys <API_KEYS> \
    --region <REGION>

Name: accounts/my-account/deployments/abcd1234
...
Direct Route Handle: my-account-abcd1234.us-arizona-1.direct.fireworks.ai
Region: US_ARIZONA_1
```
If you have multiple API keys, use repeated fields, such as:
`--direct-route-api-keys=<API_KEY_1> --direct-route-api-keys=<API_KEY_2>`. These keys can
be any alpha-numeric string and are a distinct concept from the API keys provisioned via the Fireworks console. A key
provisioned in the console but not specified the list here will not be allowed when querying the model via direct
routing.

Take note of the `Direct Route Handle` to get the inference endpoint. This is what you will use access the deployment
instead of the global `https://api.fireworks.ai/inference/` endpoint. For example:
```bash
curl \
    --header 'Authorization: Bearer <FIREWORKS_API_KEY>' \
    --header 'Content-Type: application/json' \
    --data '{
        "model": "accounts/fireworks/models/llama-v3-8b-instruct",
        "prompt": "The sky is"
    }' \
    --url https://my-account-abcd1234.us-arizona-1.direct.fireworks.ai/v1/completions
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
