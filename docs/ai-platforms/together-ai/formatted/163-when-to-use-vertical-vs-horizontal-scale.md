---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## When to use vertical vs horizontal scale?

In other words, when to add GPUs per replica or add more replicas?

### Vertical scaling

Multiple GPUs, or vertical scaling, increases the generation speed, time to first token and max QPS. You should increase GPUs if your workload meets the following conditions:

**Compute-bound** If your workload is compute-intensive and bottlenecked by GPU processing power, adding more GPUs to a single endpoint can significantly improve performance.

**Memory-intensive** If your workload requires large amounts of memory, adding more GPUs to a single endpoint can provide more memory and improve performance.

**Single-node scalability** If your workload can scale well within a single node (e.g., using data parallelism or model parallelism), adding more GPUs to a single endpoint can be an effective way to increase throughput.

**Low-latency requirements** If your application requires low latency, increasing the number of GPUs on a single endpoint can help reduce latency by processing requests in parallel.

### Horizontal scaling

The number of replicas (horizontal scaling) increases the max number of QPS. You should increase the number of replicas if your workload meets the following conditions:

**I/O-bound workloads** If your workload is I/O-bound (e.g., waiting for data to be loaded or written), increasing the number of replicas can help spread the I/O load across multiple nodes.

**Request concurrency** If your application receives a high volume of concurrent requests, increasing the number of replicas can help distribute the load and improve responsiveness.

**Fault tolerance**: Increasing the number of replicas can improve fault tolerance by ensuring that if one node fails, others can continue to process requests.

**Scalability across multiple nodes** If your workload can scale well across multiple nodes (e.g., using data parallelism or distributed training), increasing the number of replicas can be an effective way to increase throughput.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
