---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Querying dedicated deployments

For consistent performance, guaranteed capacity, or higher throughput, you can query [on-demand deployments](/guides/ondemand-deployments) instead of serverless models. Deployments use the same APIs with a deployment-specific model identifier:
```
<MODEL_NAME>#<DEPLOYMENT_NAME>
```
For example:
```python
response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1#accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
    messages=[{"role": "user", "content": "Hello"}]
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
