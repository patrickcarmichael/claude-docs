---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cluster Scaling

Clusters can scale flexibly in real time. By adding on-demand compute to your cluster, you can temporarily scale up to more GPUs when workload demand spikes and then scale back down as it wanes.

Scaling up or down can be performed using the UI, tcloud CLI, or REST API.

### Targeted Scale-down

If you wish to mark which node or nodes should be targeted for scale-down, you can:

* Either cordon the k8s node(s) or add the node.together.ai/delete-node-on-scale-down: "true" annotation to the k8s node(s).
  \= Then trigger scale-down via the cloud console UI (or CLI, REST API).
* Instant Clusters will ensure that cordoned + annotated nodes are prioritized for deletion above all others.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
