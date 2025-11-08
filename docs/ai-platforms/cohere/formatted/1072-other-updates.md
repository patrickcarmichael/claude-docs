---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Other updates

We are simplifying the Chat API by removing support for the following parameters available in V1:

* `search_queries_only`, which generates only a search query given a user’s message input. `search_queries_only` is not supported in the V2 Chat API today, but will be supported at a later date.
* `connectors`, which enables users to register a data source with Cohere for RAG queries. To use the Chat V2 API with web search, see our [migration guide](/v2/docs/migrating-v1-to-v2#) for instructios to implement a web search tool.
* `conversation_id`, used to manage chat history on behalf of the developer. This will not be supported in the V2 Chat API.
* `prompt_truncation`, used to automatically rerank and remove documents if the query did not fit in the model’s context limit. This will not be supported in the V2 Chat API.
* `force_single_step`, which forced the model to finish tool calling in one set of turns. This will not be supported in the V2 Chat API.
* `preamble`, used for giving the model task, context, and style instructions. Use a system turn at the beginning of your `messages` array in V2.
* `citation_quality`, for users to select between `fast` citations, `accurate` citations (slightly higher latency than fast), or citations `off`. In V2 Chat, we are introducing a top level `citation_options` parameter for all citation settings. `citation_quality` will be replaced by a `mode` parameter within `citation_options`.

See our Chat API [migration guide](/v2/docs/migrating-v1-to-v2) for detailed instructions to update your implementation.

These APIs are in Beta and are subject to updates. We welcome feedback in our [Discord](https://discord.com/invite/co-mmunity) channel.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
