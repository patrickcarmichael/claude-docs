---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Why use the Build SDK?

The Fireworks Build SDK gives you a declarative way to work with Fireworks resources like deployments, fine-tuning jobs, and datasets. We've designed it to handle all the infrastructure complexity for you, letting you focus on building your application. Instead of using the web UI, CLI, or raw API calls, you can manage everything through simple Python code with smart, logical defaults without sacrificing control and customizability.

The principles of the SDK are the following:

* **Object-oriented:** Fireworks primitives are represented as Python objects. You can access their capabilities and properties through methods and attributes.

* **Declarative:** You can describe your desired state and the SDK will handle reconcilliation.

* **Smart defaults:** The SDK will infer the most logical defaults for you, prioritizing development speed and lowest cost. Here are some examples:
  * The SDK will automatically use a serverless deployment for models that are available serverlessly unless you specify otherwise.
  * When creating deployments, the SDK will also enable scale-to-zero with the shortest possible scale-down window.
  * If the SDK determines that a resource already exists by matching its signature (see below), it will re-use the existing resource instead of creating a new one.

* **Customizable:** Although we enable smart defaults, you still have full access to the configuration parameters for any Fireworks resource

>   **📝 Note**
>
> The Build SDK is currently in beta and not all functionality may be supported. Please reach out to [dhuang@fireworks.ai](mailto:dhuang@fireworks.ai) to report any issues or feedback.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
