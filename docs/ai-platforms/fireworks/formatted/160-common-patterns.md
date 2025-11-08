---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Common patterns

<Tabs>
  <Tab title="Cost optimization">
    Scale to zero when idle to minimize costs:
```bash
    firectl create deployment <MODEL_NAME> \
      --min-replica-count 0 \
      --max-replica-count 3 \
      --scale-to-zero-window 1h
```
    Best for: Development, testing, or intermittent production workloads.
  </Tab>

  <Tab title="Performance-focused">
    Keep replicas running for instant response:
```bash
    firectl create deployment <MODEL_NAME> \
      --min-replica-count 2 \
      --max-replica-count 10 \
      --scale-up-window 15s \
      --load-targets concurrent_requests=5
```
    Best for: Low-latency requirements, avoiding cold starts, high-traffic applications.
  </Tab>

  <Tab title="Predictable traffic">
    Match known traffic patterns:
```bash
    firectl create deployment <MODEL_NAME> \
      --min-replica-count 3 \
      --max-replica-count 5 \
      --scale-down-window 30m \
      --load-targets tokens_generated_per_second=150
```
    Best for: Steady workloads where you know typical load ranges.
  </Tab>
</Tabs>

>   **📝 Note**
>
> Cold starts take up to a few minutes when scaling from 0→1. Deployments with min replicas = 0 are auto-deleted after 7 days of no traffic. [Reserved capacity](/deployments/reservations) guarantees availability during scale-up.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
