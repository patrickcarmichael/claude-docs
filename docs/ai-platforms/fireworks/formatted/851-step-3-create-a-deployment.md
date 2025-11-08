---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Create a deployment

This command will create a deployment of GPT OSS 120B optimized for speed. It will take a few minutes to complete. The resulting deployment will scale up to 1 replica.
```bash
firectl create deployment accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --min-replica-count 0 \
        --max-replica-count 1 \
        --scale-to-zero-window 5m \
        --wait
```
<Tip>
  `fast` is called a [deployment shape](/guides/ondemand-deployments#deployment-shapes), which is a pre-configured deployment template created by the Fireworks team that sets sensible defaults for most deployment options (such as hardware type).

  You can also pass `throughput` or `cost` to `--deployment-shape`:

  * `throughput` creates a deployment that trades off latency for lower cost-per-token at scale
  * `cost` creates a deployment that trades off latency and throughput for lowest cost-per-token at small scale, usually for early experimentation and prototyping

  While we recommend using a deployment shape, you are also free to pass your own configuration to the deployment via our [deployment options](/guides/ondemand-deployments#deployment-options).
</Tip>

The response will look like this:
```bash
Name: accounts/<YOUR ACCOUNT ID>/deployments/<DEPLOYMENT ID>
Create Time: <CREATION_TIME>
Expire Time: <EXPIRATION_TIME>
Created By: <YOUR EMAIL>
State: CREATING
Status: OK
Min Replica Count: 0
Max Replica Count: 1
Desired Replica Count: 0
Replica Count: 0
Autoscaling Policy:
  Scale Up Window: 30s
  Scale Down Window: 5m0s
  Scale To Zero Window: 5m0s
Base Model: accounts/fireworks/models/gpt-oss-120b
...other fields...
```
Take note of the `Name:` field in the response, as it will be used in the next step to query your deployment.

[Learn more about deployment options→](/guides/ondemand-deployments#deployment-options)

[Learn more about autoscaling options→](/guides/ondemand-deployments#customizing-autoscaling-behavior)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
