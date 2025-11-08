---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Optimize your Inference Latencies

By default, SageMaker endpoints have a random routing strategy. This means that requests coming to the model endpoints are forwarded to the machine learning instances randomly, which can cause latency issues in applications focused on generative AI. In 2023, the SageMaker platform introduced a `RoutingStrategy` parameter allowing you to use the ‘least outstanding requests’ (LOR) approach to routing. With LOR, SageMaker monitors the load of the instances behind your endpoint as well as the models or inference components that are deployed on each instance, then optimally routes requests to the instance that is best suited to serve it.

LOR has shown an improvement in latency under various conditions, and you can find more details [here](https://aws.amazon.com/blogs/machine-learning/minimize-real-time-inference-latency-by-using-amazon-sagemaker-routing-strategies/).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
