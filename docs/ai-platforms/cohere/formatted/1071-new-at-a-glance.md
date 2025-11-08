---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## New at a glance

* V2 Chat, Classify, Embed, and Rerank: `model` is a required parameter
* V2 Embed: `embedding_types` is a required parameter
* V2 Chat: Message and chat history are [combined](/v2/docs/migrating-v1-to-v2#messages-and-preamble) in a single `messages` array
* V2 Chat: [Tools](/v2/docs/parameter-types-in-tool-use) are defined in JSON schema
* V2 Chat: Introduces `tool_call_ids` to [match tool calls with tool results](/v2/docs/migrating-v1-to-v2#tool-call-id)
* V2 Chat: `documents` [supports a list of strings or a list of objects](/v2/docs/migrating-v1-to-v2#documents) with document metadata
* V2 Chat streaming: Uses [server-sent events](/v2/docs/migrating-v1-to-v2#streaming)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
