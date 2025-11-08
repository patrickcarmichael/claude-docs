---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting Started

Jump straight into the API with these [docs](/reference/listendpoints) or create an endpoint with this guide below.

### 1. Select a model

Explore the list of supported models for dedicated endpoints on our [models list](https://api.together.ai/models?filter=dedicated).

You can also upload your own [model](/docs/custom-models) .

### 2. Create a dedicated endpoint

To create a dedicated endpoint, first identify the hardware options for your specific model.

To do this, run:
```bash
  together endpoints hardware --model <MODEL_ID>
```

You will get a response like:
```bash
  together endpoints hardware --model mistralai/Mixtral-8x7B-Instruct-v0.1

  All hardware options:
    2x_nvidia_a100_80gb_sxm
    2x_nvidia_h100_80gb_sxm
    4x_nvidia_a100_80gb_sxm
    4x_nvidia_h100_80gb_sxm
    8x_nvidia_a100_80gb_sxm
    8x_nvidia_h100_80gb_sxm
```

From this list, you can identify which of the GPUs can be listed in your command. For example, in this list, the following combinations are possible:

1. `--gpu a100 --gpu-count 2`, `--gpu a100 --gpu-count 4`, `--gpu a100 --gpu-count 8`
2. `--gpu h100 --gpu-count 2`, `--gpu h100 --gpu-count 4`, `--gpu h100 --gpu-count 8`

You can now create a dedicated endpoint by running:
```bash
  together endpoints create \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --gpu h100 \
  --gpu-count 2 \
  --no-speculative-decoding \
  --no-prompt-cache \
  --wait
```

This command will finish when the endpoint is `READY`. To let it run asynchronously, remove the `--wait`flag.

You can optionally start an endpoint in a specific availability zone (e.g., us-central-4b). To get the list of availability zones, run:
```bash
  together endpoints availability-zones
```

Then specify the availability zone when creating your endpoint. Only specify an availability zone if you have specific latency or geographic needs as selecting one can limit hardware availability.
```bash
  together endpoints create \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --gpu h100 \
  --gpu-count 2 \
  --availability-zone us-east-1a
  --no-speculative-decoding \
  --no-prompt-cache \
  --wait
```

### 3. Get endpoint status

You can check on the deployment status by running:
```bash
  together endpoints get <ENDPOINT_ID>
```

A sample response will look like the following:
```bash
  ID:		endpoint-e6c6b82f-90f7-45b7-af39-3ca3b51d08xx
  Name:		tester/mistralai/Mixtral-8x7B-Instruct-v0.1-bb04c904
  Display Name:	My Endpoint
  Hardware:	2x_nvidia_h100_80gb_sxm
  Autoscaling:	Min=1, Max=1
  Model:		mistralai/Mixtral-8x7B-Instruct-v0.1
  Type:		dedicated
  Owner:		tester
  State:		READY
  Created:	2025-02-18 11:55:50.686000+00:00
```

### 4. Start, stop & delete endpoint

If you added the `--wait`flag on creation or previously stopped the endpoint, you can start it again by running:
```bash
  together endpoints start <ENDPOINT_ID>
```

Stopping the endpoint follows the same pattern:
```bash
  together endpoints stop <ENDPOINT_ID>
```

To fully delete the endpoint, run:
```bash
  together endpoints delete <ENDPOINT_ID>
```

### 5. List your endpoints

You can get a list of all your dedicated endpoints by running:
```bash
  together endpoints list --mine true 
```

To filter dedicated endpoints by usage type:
```bash
  together endpoints list --mine true --type dedicated --usage-type on-demand
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
