---
title: "Langgraph: Server scalability"
description: "Server scalability section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Server scalability


As you add more instances to a service, they will share the HTTP load as long as an appropriate load balancer mechanism is placed in front of them. In most deployment modalities we configure a load balancer for the service automatically. In the “self-hosted without control plane” modality it’s your responsibility to add a load balancer. Since the instances are stateless any load balancing strategy will work, no session stickiness is needed, or recommended. Any instance of the server can communicate with any queue instance (through Redis PubSub), meaning that requests to cancel or stream an in-progress run can be handled by any arbitrary instance.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Scalability & Resilience](./390-scalability-resilience.md)

**Next:** [Queue scalability →](./392-queue-scalability.md)
