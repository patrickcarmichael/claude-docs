---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Key concepts

### Resource types

The SDK supports the following resource types:

* `LLM` - Represents a model running on a deployment
* `Dataset` - Represents a dataset used to create a fine-tuning job
* `SupervisedFineTuningJob` - Represents a fine-tuning job

### Deployment type selection

The SDK tries to be parsimonious with the way it deploys resources. We provide two types of deployment options on Fireworks:

* `serverless` hosting is enabled for some commonly-used state of the art models. The pricing for these models is per-token, i.e. you only pay for the tokens you use, and subject to rate limits.
* `on-demand` hosting is enabled for all other models. The pricing for these models is per GPU-second. This hosting is required for models that are not available serverlessly or workloads that exceed serverless rate limits.

For non-finetuned models, you can always specify the deployment type of `LLM()` by passing either `"serverless"` or `"on-demand"` as the `deployment_type` parameter to the constructor. If the model is not available for the deployment type you selected, the SDK will throw an error. The SDK can also decide the best deployment strategy on your behalf, just pass `deployment_type="auto"`. If the model is available serverlessly, the SDK will use serverless hosting, otherwise the SDK will create an on-demand deployment.

>   **📝 Note**
>
> When using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`, you must call `.apply()` to apply the deployment configuration to Fireworks. This is not required for serverless deployments. When using `deployment_type="auto"`, the SDK will automatically handle deployment creation, but if it falls back to on-demand deployment, you may need to call `.apply()` explicitly. If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments).

>   **⚠️ Warning**
>
> Be careful with the `deployment_type` parameter, especially for `"auto"` and `"on-demand"` deployments. While the SDK will try to make the most cost effective choice for you and put sensible autoscaling policies in place, it is possible to unintentionally create many deployments that lead to unwanted spend, especially when working with non-serverless models.

>   **⚠️ Warning**
>
> When using `deployment_type="on-demand"`, you must provide an `id` parameter to uniquely identify your deployment. This is required to prevent accidental creation of multiple deployments.

For finetuned (LoRA) models, passing `deployment_type="serverless" ` will try to deploy the finetuned model to serverless hosting, `deployment_type="on-demand"` will create an on-demand deployment of your base model and merge in your LoRA weights, `deployment_type="on-demand-lora"` will create an on-demand deployment with Multi-LoRA enabled, and `deployment_type="auto"` will try to use `serverless` if available, otherwise fall back to `on-demand-lora`.

#### Deploying Fine-tuned Models with On-Demand

When deploying a fine-tuned model using `deployment_type="on-demand"`, you need to provide:

* `model` - Your fine-tuned model ID (e.g., `"accounts/your-account/models/your-fine-tuned-model-id"`)
* `id` - A unique deployment identifier (can be any simple string like `"my-fine-tuned-deployment"`)
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
