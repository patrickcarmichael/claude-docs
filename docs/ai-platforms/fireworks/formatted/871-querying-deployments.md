---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Querying deployments

Use completions with [on-demand deployments](/guides/ondemand-deployments) by specifying the deployment identifier:
```python
response = client.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    prompt="Your prompt here"
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
