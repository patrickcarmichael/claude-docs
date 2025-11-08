---
title: "Langgraph: Queue scalability"
description: "Queue scalability section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Queue scalability


As you add more instances to a service, they will increase run throughput linearly, as each instance is configured to handle a set number of concurrent runs (by default 10). Each attempt for each run will be handled by a single instance, with exactly-once semantics enforced through Postgres’s MVCC model (refer to section below for crash resilience details). Attempts that fail due to transient database errors are retried up to 3 times. We do not make use of long-lived transactions or locks, this enables us to make more efficient use of Postgres resources.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Server scalability](./391-server-scalability.md)

**Next:** [Resilience →](./393-resilience.md)
