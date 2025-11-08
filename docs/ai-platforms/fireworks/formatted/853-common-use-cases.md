---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common use cases

### Autoscale based on requests per second

```bash
firectl create deployment accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets requests_per_second=5 \
        --wait
```

### Autoscale based on concurrent requests

```bash
firectl create deployment accounts/fireworks/models/gpt-oss-120b \
        --deployment-shape fast \
        --scale-down-window 5m \
        --scale-up-window 30s \
        --scale-to-zero-window 5m \
        --min-replica-count 0 \
        --max-replica-count 4 \
        --load-targets concurrent_requests=5 \
        --wait
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
