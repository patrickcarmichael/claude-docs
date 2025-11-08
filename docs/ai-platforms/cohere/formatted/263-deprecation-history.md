---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Deprecation History

All deprecations are listed below with the most recent announcements at the top.

### 2025-09-15: Various older command models, a number of endpoints, all of fine-tuning.

Effective September 15, 2025, the following deprecatations will roll out.

Deprecated Models:

* `command-r-03-2024`  (and the alias `command-r`)
* `command-r-plus-04-2024`  (and the alias `command-r-plus`)
* `command-light`
* `command`
* `summarize` (Refer to [the migration guide](https://docs.cohere.com/docs/summarizing-text#migration-from-summarize-to-chat-endpoint) for alternatives).

For command model replacements, we recommend you use `command-r-08-2024`, `command-r-plus-08-2024`, or `command-a-03-2025` (which is the strongest-performing model across domains) instead.

Retired Fine-Tuning Capabilities:
Fine-tuning for the `command-light`, `command`, `command-r`, `classify`, and `rerank` models is being retired. This covers both the Cohere dashboard and API. Previously fine-tuned models will no longer be accessible.

Deprecated Features and API Endpoints:

* `/v1/connectors` (Managed connectors for RAG)
* `/v1/chat` parameters: `connectors`, `search_queries_only`
* `/v1/generate` (Legacy generative endpoint)
* `/v1/summarize` (Legacy summarization endpoint)
* `/v1/classify`
* Slack App integration
* Coral Web UI (chat.cohere.com and coral.cohere.com)

These changes reflect our commitment to innovation and performance optimization. We encourage users to assess their current implementations and migrate to recommended alternatives. Our support team is available at [support@cohere.com](mailto:support@cohere.com) to assist with the transition. For detailed guidance, please refer to our migration resources and technical documentation.

### 2025-03-08: Command-R-03-2024 Fine-tuned Models

On March 08, 2025, we will sunset all models fine-tuned with Command-R-03-2024. As part of our ongoing efforts to enhance our services, we are making the following changes to our fine-tuning capabilities:

* Deprecating fine-tuning with the older Command-R-03-2024 model
* All fine-tunes are now powered by the Command-R-08-2024 model.

Models fine-tuned with Command-R-03-2024 will continue to be supported until March 08, 2025. After this date, all requests to these models will return an error.

### 2025-01-31: Default Classify endpoint

After January 31st, 2025, usage of Classify endpoint via the default Embed models will be deprecated.

However, you can still use the Classify endpoint with a fine-tuned Embed model. By leveraging fine-tuning, you can achieve even better performance and accuracy in your classification tasks. Read the documentation on [Classify fine-tuning](https://docs.cohere.com/docs/classify-fine-tuning) for more information.

### 2024-12-02: Rerank v2.0

On December 2nd, 2024, we announced the release of Rerank-v3.5 along with the deprecation of the Rerank-v2.0 model family.
Fine-tuned models created from these base models are not affected by this deprecation.

| Shutdown Date | Deprecated Model           | Deprecated Model Price | Recommended Replacement |
| ------------- | -------------------------- | ---------------------- | ----------------------- |
| 2025-04-30    | `rerank-english-v2.0`      | \$1.00 / 1K searches   | `rerank-v3.5`           |
| 2025-04-30    | `rerank-multilingual-v2.0` | \$1.00 / 1K searches   | `rerank-v3.5`           |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
