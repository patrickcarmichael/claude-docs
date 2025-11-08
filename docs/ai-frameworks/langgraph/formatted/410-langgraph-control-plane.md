---
title: "Langgraph: LangGraph Control Plane"
description: "LangGraph Control Plane section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# LangGraph Control Plane


The term "control plane" is used broadly to refer to the control plane UI where users create and update [LangGraph Servers](./langgraph_server.md) (deployments) and the control plane APIs that support the UI experience.

When a user makes an update through the control plane UI, the update is stored in the control plane state. The [LangGraph Data Plane](./langgraph_data_plane.md) "listener" application polls for these updates by calling the control plane APIs.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Visualization](./409-visualization.md)

**Next:** [Control Plane UI →](./411-control-plane-ui.md)
