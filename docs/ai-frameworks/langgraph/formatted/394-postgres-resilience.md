---
title: "Langgraph: Postgres resilience"
description: "Postgres resilience section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Postgres resilience


For deployment modalities where we manage the Postgres database, we have periodic backups and continuously replicated standby replicas for automatic failover. This Postgres configuration is available in the [Cloud SaaS deployment option](../concepts/langgraph_cloud.md) for [`Production` deployment types](../concepts/langgraph_control_plane.md#deployment-types) only.

All communication with Postgres implements retries for retry-able errors. If Postgres is momentarily unavailable, such as during a database restart, most/all traffic should continue to succeed. Prolonged failure of Postgres will render the LangGraph Server unavailable.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Resilience](./393-resilience.md)

**Next:** [Redis resilience →](./395-redis-resilience.md)
