---
title: "Langgraph: Self-Hosted Control Plane"
description: "Self-Hosted Control Plane section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Self-Hosted Control Plane


The [Self-Hosted Control Plane](./langgraph_self_hosted_control_plane.md) deployment option is a fully self-hosted model for deployment where you manage the [control plane](./langgraph_control_plane.md) and [data plane](./langgraph_data_plane.md) in your cloud. This option gives you full control and responsibility of the control plane and data plane infrastructure.

|                                    | [Control plane](../concepts/langgraph_control_plane.md)                                                                                     | [Data plane](../concepts/langgraph_data_plane.md)                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is it?**                    | <ul><li>Control plane UI for creating deployments and revisions</li><li>Control plane APIs for creating deployments and revisions</li></ul> | <ul><li>Data plane "listener" for reconciling deployments with control plane state</li><li>LangGraph Servers</li><li>Postgres, Redis, etc</li></ul> |
| **Where is it hosted?**            | Your cloud                                                                                                                                  | Your cloud                                                                                                                                          |
| **Who provisions and manages it?** | You                                                                                                                                         | You                                                                                                                                                 |

### Architecture

![Self-Hosted Control Plane Architecture](./img/self_hosted_control_plane_architecture.png)

### Compute Platforms

- **Kubernetes**: The Self-Hosted Control Plane deployment option supports deploying control plane and data plane infrastructure to any Kubernetes cluster.

!!! tip
If you would like to enable this on your LangSmith instance, please follow the [Self-Hosted Control Plane deployment guide](../cloud/deployment/self_hosted_control_plane.md).

---

concepts/langgraph_cli.md

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

**Previous:** [← Requirements](./430-requirements.md)

**Next:** [LangGraph CLI →](./432-langgraph-cli.md)
