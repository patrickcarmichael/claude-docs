---
title: "Langgraph: Redis resilience"
description: "Redis resilience section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Redis resilience


All data that requires durable storage is stored in Postgres, not Redis. Redis is used only for ephemeral metadata, and communication between instances. Therefore we place no durability requirements on Redis.

All communication with Redis implements retries for retry-able errors. If Redis is momentarily unavailable, such as during a database restart, most/all traffic should continue to succeed. Prolonged failure of Redis will render the LangGraph Server unavailable.

---

concepts/low_level.md

---

---

search:
  boost: 2

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Postgres resilience](./394-postgres-resilience.md)

**Next:** [Graph API concepts →](./396-graph-api-concepts.md)
