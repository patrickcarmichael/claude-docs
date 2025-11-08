---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploying your model

Once your model shows `State: READY`, create a deployment:
```bash
firectl create deployment accounts/<ACCOUNT_ID>/models/<MODEL_NAME> --wait
```
See the [On-demand deployments guide](/guides/ondemand-deployments) for configuration options like GPU types, autoscaling, and quantization.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
