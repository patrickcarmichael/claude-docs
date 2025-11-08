---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

First, you will need to deploy the Command model on Azure via Azure AI Foundry. The deployment will create a serverless API with pay-as-you-go token based billing. You can find more information on how to deploy models in the [Azure documentation](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio).

In the example below, we are deploying the Command R+ (August 2024) model.

Once the model is deployed, you can access it via Cohere's Python SDK. Let's now install the Cohere SDK and set up our client.

To create a client, you need to provide the API key and the model's base URL for the Azure endpoint. You can get these information from the Azure AI Foundry platform where you deployed the model.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
