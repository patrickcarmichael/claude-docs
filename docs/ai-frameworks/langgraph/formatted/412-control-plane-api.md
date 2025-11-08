---
title: "Langgraph: Control Plane API"
description: "Control Plane API section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Control Plane API


This section describes the data model of the control plane API. The API is used to create, update, and delete deployments. See the [control plane API reference](../cloud/reference/api/api_ref_control_plane.md) for more details.

### Deployment

A deployment is an instance of a LangGraph Server. A single deployment can have many revisions.

### Revision

A revision is an iteration of a deployment. When a new deployment is created, an initial revision is automatically created. To deploy code changes or update secrets for a deployment, a new revision must be created.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Control Plane UI](./411-control-plane-ui.md)

**Next:** [Control Plane Features →](./413-control-plane-features.md)
