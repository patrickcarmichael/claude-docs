---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## What is a Private Deployment?

Private deployments allow organizations to implement and run AI models within a controlled, internal environment.

In a private deployment, you manage the model deployment infrastructure (with Cohere's guidance and support). This includes ensuring hardware and driver compatibility as well as installing prerequisites to run the containers. These deployments typically run on Kubernetes, but it’s not a firm requirement.

Cohere supports two types of private deployments:

* On-premises (on-prem)
  <br />Gives you full control over both your data and the AI system on your own premises with your own hardware. You procure your own GPUs, servers and other hardware to insulate your environment from external threats.

* On the cloud, typically a virtual private cloud (VPC)
  <br />You use infrastructure needed to host AI models from a cloud provider (such as AWS, Azure, GCP, or OCI) while still retaining control of how the data is stored and processed. Cohere can support any VPC on any cloud environment, so long as the necessary hardware requirements are met.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
