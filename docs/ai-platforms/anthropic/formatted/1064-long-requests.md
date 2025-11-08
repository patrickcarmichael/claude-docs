---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Long requests

>   **⚠️ Warning**
>
> We highly encourage using the [streaming Messages API](/en/docs/build-with-claude/streaming) or [Message Batches API](/en/api/creating-message-batches) for long running requests, especially those over 10 minutes.

We do not recommend setting a large `max_tokens` values without using our [streaming Messages API](/en/docs/build-with-claude/streaming)
or [Message Batches API](/en/api/creating-message-batches):

* Some networks may drop idle connections after a variable period of time, which
  can cause the request to fail or timeout without receiving a response from Anthropic.
* Networks differ in reliability; our [Message Batches API](/en/api/creating-message-batches) can help you
  manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, you should be aware that setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.

Our [SDKs](/en/api/client-sdks) will validate that your non-streaming Messages API requests are not expected to exceed a 10 minute timeout and
also will set a socket option for TCP keep-alive.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
