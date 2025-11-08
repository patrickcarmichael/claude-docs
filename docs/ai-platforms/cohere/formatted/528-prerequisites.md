---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prerequisites

* Ensure that IAM role used has `AmazonSageMakerFullAccess`
* To deploy your model successfully, ensure that either:
  * Your IAM role has these three permissions, and you have authority to make AWS Marketplace subscriptions in the relevant AWS account:
    * `aws-marketplace:ViewSubscriptions`
    * `aws-marketplace:Unsubscribe`
    * `aws-marketplace:Subscribe`
  * Or, your AWS account has a subscription to the packages for [Cohere Bring Your Own Fine-tuning](https://aws.amazon.com/marketplace/pp/prodview-5wt5pdnw3bbq6). If so, you can skip the "subscribe to the bring your own finetuning algorithm" step below.

**NOTE:** If you're running the companion notebook, know that it contains elements which render correctly in Jupyter interface, so you should open it from an Amazon SageMaker Notebook Instance or Amazon SageMaker Studio.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
