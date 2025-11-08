---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pricing and availability

### Pricing

Claude 4.5 models maintain competitive pricing:

| Model             | Input                  | Output                  |
| ----------------- | ---------------------- | ----------------------- |
| Claude Sonnet 4.5 | \$3 per million tokens | \$15 per million tokens |
| Claude Haiku 4.5  | \$1 per million tokens | \$5 per million tokens  |

For more details, see the [pricing documentation](/en/docs/about-claude/pricing).

### Third-party platform pricing

Starting with Claude 4.5 models (Sonnet 4.5 and Haiku 4.5), AWS Bedrock and Google Vertex AI offer two endpoint types:

* **Global endpoints**: Dynamic routing for maximum availability
* **Regional endpoints**: Guaranteed data routing through specific geographic regions with a **10% pricing premium**

**This regional pricing applies to both Claude Sonnet 4.5 and Claude Haiku 4.5.**

**The Claude API (1P) is global by default and unaffected by this change.** The Claude API is global-only (equivalent to the global endpoint offering and pricing from other providers).

For implementation details and migration guidance:

* [AWS Bedrock global vs regional endpoints](/en/docs/build-with-claude/claude-on-amazon-bedrock#global-vs-regional-endpoints)
* [Google Vertex AI global vs regional endpoints](/en/docs/build-with-claude/claude-on-vertex-ai#global-vs-regional-endpoints)

### Availability

Claude 4.5 models are available on:

| Model             | Claude API                   | Amazon Bedrock                              | Google Cloud Vertex AI       |
| ----------------- | ---------------------------- | ------------------------------------------- | ---------------------------- |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` | `anthropic.claude-sonnet-4-5-20250929-v1:0` | `claude-sonnet-4-5@20250929` |
| Claude Haiku 4.5  | `claude-haiku-4-5-20251001`  | `anthropic.claude-haiku-4-5-20251001-v1:0`  | `claude-haiku-4-5@20251001`  |

Also available through Claude.ai and Claude Code platforms.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
