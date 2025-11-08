---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Authentication and Billing

When using Together AI through Hugging Face, you have two options for authentication:

* Direct Requests: Use your Together AI API key in your Hugging Face user account settings. In this mode, inference requests are sent directly to Together AI, and billing is handled by your Together AI account.
* Routed Requests: If you don't configure a Together AI API key, your requests will be routed through Hugging Face. In this case, you can use a Hugging Face token for authentication. Billing for routed requests is applied to your Hugging Face account at standard provider API rates.You don’t need an account on Together AI to do this, just use your HF one!

To add a Together AI api key to your Hugging Face settings, follow these steps:

1. Go to your [Hugging Face user account settings](https://huggingface.co/settings/inference-providers).
2. Locate the "Inference Providers" section.
3. You can add your API keys for different providers, including Together AI
4. You can also set your preferred provider order, which will influence the display order in model widgets and code snippets.

>   **ℹ️ Info**
>
> You can search for all [Together AI models](https://huggingface.co/models?inference_provider=together\&sort=trending) on the hub and directly try out the available models via the Model Page widget too.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
