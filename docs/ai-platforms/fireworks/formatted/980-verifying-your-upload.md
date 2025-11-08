---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Verifying your upload

After uploading, verify your model is ready to deploy:
```bash
firectl get model accounts/<ACCOUNT_ID>/models/<MODEL_NAME>
```
Look for `State: READY` in the output. Once ready, you can create a deployment.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
