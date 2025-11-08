---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Storage Management

Instant Clusters supports long-lived, resizable in-DC shared storage.

You can dynamically create and attach volumes to your cluster at cluster creation time, and resize as your data grows.

All shared storage is backed by multi-NIC bare metal paths, ensuring high-throughput and low-latency performance for shared storage.

### Upload Your Data

To upload data to the cluster from your local machine, follow these steps:

* Create a PVC using the `shared-rdma` storage class as well as a pod to mount the volume
* Run `kubectl cp LOCAL_FILENAME YOUR_POD_NAME:/data/`
* Note: This method is suitable for smaller datasets, for larger datasets we recommend scheduling a pod on the cluster that can download from S3.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
