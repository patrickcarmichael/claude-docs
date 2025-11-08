---
title: "Langgraph: Self-Hosted Data Plane"
description: "Self-Hosted Data Plane section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Self-Hosted Data Plane


!!! info "Important"
    The Self-Hosted Data Plane deployment option requires an [Enterprise](../concepts/plans.md) plan.

The [Self-Hosted Data Plane](./langgraph_self_hosted_data_plane.md) deployment option is a "hybrid" model for deployment where we manage the [control plane](./langgraph_control_plane.md) in our cloud and you manage the [data plane](./langgraph_data_plane.md) in your cloud. This option provides a way to securely manage your data plane infrastructure, while offloading control plane management to us.

Build a Docker image using the [LangGraph CLI](./langgraph_cli.md) and deploy your LangGraph Server from the [control plane UI](./langgraph_control_plane.md#control-plane-ui).

Supported Compute Platforms: [Kubernetes](https://kubernetes.io/), [Amazon ECS](https://aws.amazon.com/ecs/) (coming soon!)

For more information, please see:

* [Self-Hosted Data Plane Conceptual Guide](./langgraph_self_hosted_data_plane.md)
* [How to deploy the Self-Hosted Data Plane](../cloud/deployment/self_hosted_data_plane.md)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Cloud SaaS](./322-cloud-saas.md)

**Next:** [Self-Hosted Control Plane →](./324-self-hosted-control-plane.md)
