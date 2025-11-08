---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Price-Based Load Balancing (Default Strategy)

For each model in your request, OpenRouter's default behavior is to load balance requests across providers, prioritizing price.

If you are more sensitive to throughput than price, you can use the `sort` field to explicitly prioritize throughput.

<Tip>
  When you send a request with `tools` or `tool_choice`, OpenRouter will only
  route to providers that support tool use. Similarly, if you set a
  `max_tokens`, then OpenRouter will only route to providers that support a
  response of that length.
</Tip>

Here is OpenRouter's default load balancing strategy:

1. Prioritize providers that have not seen significant outages in the last 30 seconds.
2. For the stable providers, look at the lowest-cost candidates and select one weighted by inverse square of the price (example below).
3. Use the remaining providers as fallbacks.

<Note title="A Load Balancing Example">
  If Provider A costs \$1 per million tokens, Provider B costs \$2, and Provider C costs \$3, and Provider B recently saw a few outages.

  * Your request is routed to Provider A. Provider A is 9x more likely to be first routed to Provider A than Provider C because $(1 / 3^2 = 1/9)$ (inverse square of the price).
  * If Provider A fails, then Provider C will be tried next.
  * If Provider C also fails, Provider B will be tried last.
</Note>

If you have `sort` or `order` set in your provider preferences, load balancing will be disabled.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
