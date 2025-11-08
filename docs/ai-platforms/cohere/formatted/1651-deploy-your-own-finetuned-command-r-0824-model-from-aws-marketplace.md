---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deploy Your Own Finetuned Command-R-0824 Model from AWS Marketplace

This sample notebook shows you how to deploy your own finetuned HuggingFace Command-R model [CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) using Amazon SageMaker. More specifically, assuming you already have the adapter weights or merged weights from your own finetuning of [CohereForAI/c4ai-command-r-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024), we will show you how to

1. Merge the adapter weights to the weights of the base model, if you bring only the adapter weights
2. Export the merged weights to the TensorRT-LLM inference engine using Amazon SageMaker
3. Deploy the engine as a SageMaker endpoint to serve your business use cases

>   **Note**: This is a reference notebook and it cannot run unless you make changes suggested in the notebook.

### Pre-requisites:

1. **Note: This notebook contains elements which render correctly in Jupyter interface. Open this notebook from an Amazon SageMaker Notebook Instance or Amazon SageMaker Studio.**
2. Ensure that IAM role used has **AmazonSageMakerFullAccess**
3. To deploy this ML model successfully, ensure that:
   1. Either your IAM role has these three permissions and you have authority to make AWS Marketplace subscriptions in the AWS account used:
      1. **aws-marketplace:ViewSubscriptions**
      2. **aws-marketplace:Unsubscribe**
      3. **aws-marketplace:Subscribe**
   2. or your AWS account has a subscription to the packages for [Cohere Bring Your Own Fine-tuning](https://aws.amazon.com/marketplace/pp/prodview-5wt5pdnw3bbq6). If so, skip step: [Subscribe to the bring your own finetuning algorithm](#subscribe)

### Contents:

1. [Subscribe to the bring your own finetuning algorithm](#subscribe)
2. [Preliminary setup](#setup)
3. [Get the merged weights](#merge)
4. [Upload the merged weights to S3](#upload)
5. [Export the merged weights to the TensorRT-LLM inference engine](#export)
6. [Create an endpoint for inference from the exported engine](#endpoint)
7. [Perform real-time inference by calling the endpoint](#inference)
8. [Delete the endpoint (optional)](#delete)
9. [Unsubscribe to the listing (optional)](#unsubscribe)

### Usage instructions:

You can run this notebook one cell at a time (By using Shift+Enter for running a cell).

<a name="subscribe" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
