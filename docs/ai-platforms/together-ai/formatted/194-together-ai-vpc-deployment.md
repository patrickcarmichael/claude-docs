---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Together AI VPC Deployment

Together AI VPC Deployment allows you to deploy the platform in your own Virtual Private Cloud (VPC) on any cloud provider (such as Google Cloud, Azure, AWS, or others). This option is ideal for enterprises that need enhanced security, control, and compliance while benefiting from Together AI's powerful AI stack.

### Key Features

* **Cloud-Agnostic**: Deploy within your VPC on any cloud platform of your choice (e.g., AWS, Azure, Google Cloud).
* **Full Control**: Complete administrative access, enabling you to manage and control ingress and egress traffic within your VPC.
* **High Performance**: Achieve up to 2x faster performance on your existing infrastructure, optimized for your environment.
* **Data Sovereignty**: Data never leaves your controlled environment, ensuring complete security and compliance.
* **Customization**: Tailor scaling, performance, and resource allocation to fit your infrastructure’s specific needs.
* **Ideal Use Case**: Perfect for enterprises with strict security, privacy, and compliance requirements who want to retain full control over their cloud infrastructure.

### Example: VPC Deployment in AWS

Below is an example of how Together AI VPC Deployment works in an AWS environment. This system diagram illustrates the architecture and flow:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7ad0b55a56e9eaecf03c80d3a90ef66f" alt="" data-og-width="1342" width="1342" data-og-height="1070" height="1070" data-path="images/guides/34.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=884013b1f58f1f732c9aab0c0c7c6e00 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=643e3f65fc16039aa2ecb0c0a41f4ac2 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f77e787d3e26b454d7e9495371aaa3e9 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d1f99a659a9952d7fba4e10780f09baf 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ecd727b0a535236a4b923831192f12ff 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7b5c6567c0e45f31f15ec4d2918359bb 2500w" />
</Frame>

1. **Secure VPC Peering**: Together AI connects to your AWS environment via secure VPC peering, ensuring data remains entirely within your AWS account.
2. **Private Subnets**: All data processing and model inference happens within private subnets, isolating resources from the internet.
3. **Control of Ingress/Egress Traffic**: You have full control over all traffic entering and leaving your VPC, including restrictions on external network access.
4. **Data Sovereignty**: Since all computations are performed within your VPC, data never leaves your controlled environment.
5. **Custom Scaling**: Leverage AWS autoscaling groups to ensure that your AI workloads scale seamlessly with demand, while maintaining complete control over resources.

Although this example uses AWS, the architecture can be adapted to other cloud providers such as Azure or Google Cloud with similar capabilities.

For more information on VPC deployment, [get in touch with us](/docs/support-ticket-portal).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
