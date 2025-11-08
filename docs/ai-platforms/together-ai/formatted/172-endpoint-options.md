---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Endpoint options

### Replica count

Replicas provide horizontal scaling, ensuring better handling of high traffic, reduced latency, and resiliency in the event of instance failure. They are set with the `--min-replicas`and `--max-replicas`options. The default min and max replica is set to 1. When the max replica is increased, the endpoint will automatically scale based on server load.

### Auto-shutdown

If an endpoint is inactive for an hour, it will shutdown automatically. This window of inactivity can be customized when configuring a deployment in the web interface or by setting `--inactive-timeout` to the desired value.

### Choosing hardware and GPU count

A hardware configuration for a given model follows this format: \[gpu-count]-\[hardware]-\[gpu-type]-\[gpu-link]

Example:`2x_nvidia_h100_80gb_sxm`

When configuring the hardware on the CLI, you can specify which version of the hardware you would like by listing the `--gpu`(or hardware), `--gpu-count`and `gpu-type`

#### Multiple GPUs

Increasing the `gpu-count` will increase the GPUs per replica. This will result in higher generation speed, lower time-to-first-token and higher max QPS.

#### Availability zone

If you have specific latency or geographic needs, select an availability zone when creating your endpoint. It is important to note that restricting to an availability zone can limit hardware availability.

To get the list of availability zones, run:
```bash
  together endpoints availability-zones
```

### Speculative decoding

Speculative decoding is an optimization technique used to improve the efficiency of text generation and decoding processes. Using speculators can improve performance, increase throughput and improve the handling of uncertain or ambiguous input.

Customers who require consistently low tail latencies—such as those running real-time or mission-critical applications—may want to avoid speculative decoding. While this technique can improve average performance, it also introduces the risk of occasional extreme delays, which may be unacceptable in latency-sensitive workloads.

By default, speculative decoding is not enabled. To enable speculative decoding, remove the `--no-speculative-decoding` flag from the create command.

### Prompt caching

Prompt caching stores the results of previously executed prompts, allowing your model to quickly retrieve and return cached responses instead of reprocessing the same input. This significantly improves performance by reducing redundant computations.

By default, caching is not enabled. To turn on prompt caching, remove `--no-prompt-cache` from the create command.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
