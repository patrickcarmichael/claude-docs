---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Prerequisites

Whether you're using Command or Embed, the initial set up is the same. You'll need:

* An Azure subscription with a valid payment method. Free or trial Azure subscriptions won't work. If you don't have an Azure subscription, create a [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) to begin.
* An [Azure AI hub resource](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/create-azure-ai-resource). Note: for Cohere models, the pay-as-you-go deployment offering is only available with AI hubs created in the `East US`, `East US 2`, `North Central US`, `South Central US`, `Sweden Central`, `West US` or `West US 3` regions.
* An [Azure AI project](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/create-projects) in Azure AI Studio.
* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure AI Studio. To perform the required steps, your user account must be assigned the Azure AI Developer role on the resource group. For more information on permissions, see [Role-based access control in Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/rbac-ai-studio).

For workflows based around Command, Embed, or Rerank, you'll also need to create a deployment and consume the model. Here are links for more information:

* **Command:** [create a Command deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command#create-a-new-deployment) and then [consume the Command model](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command#create-a-new-deployment).
* **Embed:** [create an Embed deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-embed#create-a-new-deployment) and [consume the Embed model](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-embed#consume-the-cohere-embed-models-as-a-service).
* **Rerank**: [create a Rerank deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-rerank) and [consume the Rerank model](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-rerank#consume-the-cohere-rerank-models-as-a-service).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
