---
title: "Langgraph: "Listener" Application"
description: ""Listener" Application section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## "Listener" Application


The data plane "listener" application periodically calls [control plane APIs](../concepts/langgraph_control_plane.md#control-plane-api) to:

- Determine if new deployments should be created.
- Determine if existing deployments should be updated (i.e. new revisions).
- Determine if existing deployments should be deleted.

In other words, the data plane "listener" reads the latest state of the control plane (desired state) and takes action to reconcile outstanding deployments (current state) to match the latest state.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Server Infrastructure](./422-server-infrastructure.md)

**Next:** [Postgres →](./424-postgres.md)
