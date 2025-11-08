---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Provider Routing

> Route AI model requests across multiple providers intelligently. Learn how to optimize for cost, performance, and reliability with OpenRouter's provider routing.

OpenRouter routes requests to the best available providers for your model. By default, [requests are load balanced](#price-based-load-balancing-default-strategy) across the top providers to maximize uptime.

You can customize how your requests are routed using the `provider` object in the request body for [Chat Completions](/docs/api-reference/chat-completion) and [Completions](/docs/api-reference/completion).

<Tip>
  For a complete list of valid provider names to use in the API, see the [full
  provider schema](#json-schema-for-provider-preferences).
</Tip>

The `provider` object can contain the following fields:

| Field                      | Type              | Default | Description                                                                                                                       |
| -------------------------- | ----------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `order`                    | string\[]         | -       | List of provider slugs to try in order (e.g. `["anthropic", "openai"]`). [Learn more](#ordering-specific-providers)               |
| `allow_fallbacks`          | boolean           | `true`  | Whether to allow backup providers when the primary is unavailable. [Learn more](#disabling-fallbacks)                             |
| `require_parameters`       | boolean           | `false` | Only use providers that support all parameters in your request. [Learn more](#requiring-providers-to-support-all-parameters-beta) |
| `data_collection`          | "allow" \| "deny" | "allow" | Control whether to use providers that may store data. [Learn more](#requiring-providers-to-comply-with-data-policies)             |
| `zdr`                      | boolean           | -       | Restrict routing to only ZDR (Zero Data Retention) endpoints. [Learn more](#zero-data-retention-enforcement)                      |
| `enforce_distillable_text` | boolean           | -       | Restrict routing to only models that allow text distillation. [Learn more](#distillable-text-enforcement)                         |
| `only`                     | string\[]         | -       | List of provider slugs to allow for this request. [Learn more](#allowing-only-specific-providers)                                 |
| `ignore`                   | string\[]         | -       | List of provider slugs to skip for this request. [Learn more](#ignoring-providers)                                                |
| `quantizations`            | string\[]         | -       | List of quantization levels to filter by (e.g. `["int4", "int8"]`). [Learn more](#quantization)                                   |
| `sort`                     | string            | -       | Sort providers by price or throughput. (e.g. `"price"` or `"throughput"`). [Learn more](#provider-sorting)                        |
| `max_price`                | object            | -       | The maximum pricing you want to pay for this request. [Learn more](#maximum-price)                                                |

<Note title="EU data residency (Enterprise)">
  OpenRouter supports EU in-region routing for enterprise customers. When enabled, prompts and completions are processed entirely within the EU. Learn more in our [Privacy docs here](/docs/features/privacy-and-logging#enterprise-eu-in-region-routing). To contact our enterprise team, [fill out this form](https://openrouter.ai/enterprise/form).
</Note>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
