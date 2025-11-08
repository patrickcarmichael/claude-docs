---
title: "Langgraph: Resilience"
description: "Resilience section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Resilience


While a run is being handled by a queue instance, a periodic heartbeat timestamp will be recorded in Redis by that queue worker.

When a graceful shutdown request is received (SIGINT) an instance enters shutdown mode, which

- stops accepting new HTTP requests
- gives any in-progress runs a limited number of seconds to finish (if not finished it will be put back in the queue)
- stops the instance from picking up more runs from the queue

If a hard shutdown occurs due to a server crash or an infrastructure failure, any runs that were in progress will be picked up by an internal sweeper task that looks for in-progress runs that have breached their heartbeat window. The sweeper runs every 2 minutes and will put the runs back in the queue for another instance to pick them up.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Queue scalability](./392-queue-scalability.md)

**Next:** [Postgres resilience →](./394-postgres-resilience.md)
