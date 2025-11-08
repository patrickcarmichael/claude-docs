---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Events stream

In tool use, the events streamed by the endpoint follows the structure of a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events) but contains additional events for tool calling and response generation with the associated contents. This section describes the stream of events and their contents.

### Tool calling step

#### Event types

`message-start`

Same as in a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events).

`tool-plan-delta`

Emitted when the next token of the tool plan is generated.

`tool-call-start`

Emitted when the model generates tool calls that require actioning upon. The event contains a list of `tool_calls` containing the tool name and tool call ID of the tool.

`tool-call-delta`

Emitted when the next token of the the tool call is generated.

`tool-call-end`

Emitted when the tool call is finished.

When there are more than one tool calls being made (i.e. parallel tool calls), the sequence of `tool-call-start`, `tool-call-delta`, and `tool-call-end` events will repeat.

`message-end`

Same as in a [basic chat stream event](https://docs.cohere.com/v2/docs/streaming#basic-chat-stream-events).

#### Example stream

The following is an example stream in the tool calling step.
```mdx wordWrap

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
