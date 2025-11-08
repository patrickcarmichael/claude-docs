---
title: "Langgraph: Overview"
description: "Overview section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Overview


The Standalone Container deployment option is the least restrictive model for deployment. There is no [control plane](./langgraph_control_plane.md). [Data plane](./langgraph_data_plane.md) infrastructure is managed by you.

|                   | [Control plane](../concepts/langgraph_control_plane.md) | [Data plane](../concepts/langgraph_data_plane.md) |
|-------------------|-------------------|------------|
| **What is it?** | n/a | <ul><li>LangGraph Servers</li><li>Postgres, Redis, etc</li></ul> |
| **Where is it hosted?** | n/a | Your cloud |
| **Who provisions and manages it?** | n/a | You |

!!! warning

      LangGraph Platform should not be deployed in serverless environments. Scale to zero may cause task loss and scaling up will not work reliably.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Standalone Container](./282-standalone-container.md)

**Next:** [Architecture →](./284-architecture.md)
