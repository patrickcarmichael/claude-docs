---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Important considerations

### No resource creation

When connecting to existing deployments:

* **No new resources are created** - The SDK connects to your existing deployment
* **No `.apply()` call needed** - The deployment is already active
* **Immediate availability** - You can start making inference calls right away

### Deployment ID requirements

The `id` parameter should match exactly with your existing deployment:

* Use the deployment name/ID as shown in the Fireworks dashboard
* The ID is case-sensitive and must match exactly
* If the deployment doesn't exist, you'll receive an error when making requests

### Model specification

While you need to specify the `model` parameter, it should match the model that your deployment is actually running:
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
