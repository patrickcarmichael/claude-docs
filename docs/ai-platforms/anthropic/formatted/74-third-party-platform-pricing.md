---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Third-party platform pricing

Claude models are available on [AWS Bedrock](/en/docs/build-with-claude/claude-on-amazon-bedrock) and [Google Vertex AI](/en/docs/build-with-claude/claude-on-vertex-ai). For official pricing, visit:

* [AWS Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
* [Google Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)

>   **📝 Note**
>
>   **Regional endpoint pricing for Claude 4.5 models and beyond**

  Starting with Claude Sonnet 4.5 and Haiku 4.5, AWS Bedrock and Google Vertex AI offer two endpoint types:

  * **Global endpoints**: Dynamic routing across regions for maximum availability
  * **Regional endpoints**: Data routing guaranteed within specific geographic regions

  Regional endpoints include a 10% premium over global endpoints. **The Claude API (1P) is global by default and unaffected by this change.** The Claude API is global-only (equivalent to the global endpoint offering and pricing from other providers).

  **Scope**: This pricing structure applies to Claude Sonnet 4.5, Haiku 4.5, and all future models. Earlier models (Claude Sonnet 4, Opus 4, and prior releases) retain their existing pricing.

  For implementation details and code examples:

  * [AWS Bedrock global vs regional endpoints](/en/docs/build-with-claude/claude-on-amazon-bedrock#global-vs-regional-endpoints)
  * [Google Vertex AI global vs regional endpoints](/en/docs/build-with-claude/claude-on-vertex-ai#global-vs-regional-endpoints)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
