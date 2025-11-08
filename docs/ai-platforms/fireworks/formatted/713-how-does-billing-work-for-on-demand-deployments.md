---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How does billing work for on-demand deployments?

Source: https://docs.fireworks.ai/faq-new/deployment-infrastructure/how-does-billing-work-for-on-demand-deployments


On-demand deployments come with automatic cost optimization features:

* **Default autoscaling**: Automatically scales to 0 replicas when not in use
* **Pay for what you use**: Charged only for GPU time when replicas are active
* **Flexible configuration**: Customize autoscaling behavior to match your needs

**Best practices for cost management**:

1. **Leverage default autoscaling**: The system automatically scales down deployments when not in use
2. **Customize carefully**: While you can modify autoscaling behavior using our [configuration options](https://docs.fireworks.ai/guides/ondemand-deployments#customizing-autoscaling-behavior), note that preventing scale-to-zero will result in continuous GPU charges
3. **Consider your use case**: For intermittent or low-frequency usage, serverless deployments might be more cost-effective

For detailed configuration options, see our [deployment guide](https://docs.fireworks.ai/guides/ondemand-deployments#replica-count-horizontal-scaling).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
