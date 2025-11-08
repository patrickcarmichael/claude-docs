---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting dedicated endpoints configuration

There are a number of reasons that an endpoint isn't immediately created successfully.

**Lack of availability**: If we are short on available hardware, the endpoint will still be created but rather than automatically starting the endpoint, it will be queued for the next available hardware.

**Low availability**: We may have hardware available but only enough for a small amount of replicas. If this is the case, the endpoint may start but only scale to the amount of replicas available. If the min replica is set higher than we have capacity for, we may queue the endpoint until there is enough availability. To avoid the wait, you can reduce the minimum replica count.

**Hardware unavailable error**: If you see "Hardware for endpoint not available now. please try again later", the required resources are currently unavailable. Try using a different comparable model (see [whichllm.together.ai](https://whichllm.together.ai/)) or attempt deployment at a different time when more resources may be available.

**Model not supported**: Not all models are supported on dedicated endpoints. Check the list of supported models in your [account dashboard](https://api.together.xyz/models?filter=dedicated) under Models > All Models > Dedicated toggle. Your fine-tuned model must be based on a supported base model to deploy on an endpoint.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
