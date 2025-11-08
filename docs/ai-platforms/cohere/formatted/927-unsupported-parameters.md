---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Unsupported parameters

The following parameters are not supported in the Compatibility API:

### Chat completions

* `store`
* `metadata`
* `logit_bias`
* `top_logprobs`
* `n`
* `modalities`
* `prediction`
* `audio`
* `service_tier`
* `parallel_tool_calls`

### Embeddings

* `dimensions`
* `user`

### Cohere-specific parameters

Parameters that are uniquely available on the Cohere API but not on the OpenAI SDK are not supported.

Chat endpoint:

* `connectors`
* `documents`
* `citation_options`
* ...[more here](https://docs.cohere.com/reference/chat)

Embed endpoint:

* `input_type`
* `images`
* `truncate`
* ...[more here](https://docs.cohere.com/reference/embed)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
