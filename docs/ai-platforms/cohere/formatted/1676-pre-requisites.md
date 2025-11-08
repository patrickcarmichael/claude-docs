---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pre-requisites:

1. **Note: This notebook contains elements which render correctly in Jupyter interface. Open this notebook from an Amazon SageMaker Notebook Instance or Amazon SageMaker Studio.**
2. Ensure that IAM role used has **AmazonSageMakerFullAccess**
3. To deploy this ML model successfully, ensure that:
   1. Either your IAM role has these three permissions and you have authority to make AWS Marketplace subscriptions in the AWS account used:
      1. **aws-marketplace:ViewSubscriptions**
      2. **aws-marketplace:Unsubscribe**
      3. **aws-marketplace:Subscribe**
   2. or your AWS account has a subscription to the packages for [Cohere Command R Finetuning](https://aws.amazon.com/marketplace/ai/configuration?productId=1762e582-e7df-47f0-a49f-98e22302a702). If so, skip step: [Subscribe to the finetune algorithm](#1.-Subscribe-to-the-finetune-algorithm)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
