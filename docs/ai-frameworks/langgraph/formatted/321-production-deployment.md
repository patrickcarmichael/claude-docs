---
title: "Langgraph: Production deployment"
description: "Production deployment section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Production deployment


There are 4 main options for deploying with the [LangGraph Platform](langgraph_platform.md):

1. [Cloud SaaS](#cloud-saas)

1. [Self-Hosted Data Plane](#self-hosted-data-plane)

1. [Self-Hosted Control Plane](#self-hosted-control-plane)

1. [Standalone Container](#standalone-container)

A quick comparison:

|                      | **Cloud SaaS** | **Self-Hosted Data Plane** | **Self-Hosted Control Plane** | **Standalone Container** |
|----------------------|----------------|----------------------------|-------------------------------|--------------------------|
| **[Control plane UI/API](../concepts/langgraph_control_plane.md)** | Yes | Yes | Yes | No |
| **CI/CD** | Managed internally by platform | Managed externally by you | Managed externally by you | Managed externally by you |
| **Data/compute residency** | LangChain's cloud | Your cloud | Your cloud | Your cloud |
| **LangSmith compatibility** | Trace to LangSmith SaaS | Trace to LangSmith SaaS | Trace to Self-Hosted LangSmith | Optional tracing |
| **[Pricing](https://www.langchain.com/pricing-langgraph-platform)** | Plus | Enterprise | Enterprise | Enterprise |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Free deployment](./320-free-deployment.md)

**Next:** [Cloud SaaS →](./322-cloud-saas.md)
