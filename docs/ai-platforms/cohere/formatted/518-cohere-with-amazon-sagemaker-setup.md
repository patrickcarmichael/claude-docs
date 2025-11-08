---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere with Amazon SageMaker Setup

First, navigate to [Cohere’s SageMaker Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=87af0c85-6cf9-4ed8-bee0-b40ce65167e0) to view the available product offerings. Select the product offering to which you are interested in subscribing.

Next, explore the tools on the **Product Detail** page to evaluate how you want to configure your subscription. It contains information related to:

* Pricing: This section allows you to estimate the cost of running inference on different types of instances.
* Usage: This section contains the technical details around supported data formats for each model, and offers links to documentation and notebooks that will help developers scope out the effort required to integrate with Cohere’s models.
* Subscribing: This section will once again present you with both the pricing details and the EULA for final review before you accept the offer. This information is identical to the information on Product Detail page.
* Configuration: The primary goal of this section is to retrieve the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) for the product you have subscribed to.

>   **⚠️ Warning**
>
> For any Cohere 

  *software*

   version after 1.0.5 (or 

  *model*

   version after 3.0.5), the parameter 

  `InferenceAmiVersion=al2-ami-sagemaker-inference-gpu-2`

   must be specified during endpoint configuration (as a variant option) to avoid deployment errors.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
