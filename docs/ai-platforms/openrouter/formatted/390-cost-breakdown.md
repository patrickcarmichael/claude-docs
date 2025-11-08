---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cost Breakdown

The usage response includes detailed cost information:

* `cost`: The total amount charged to your account
* `cost_details.upstream_inference_cost`: The actual cost charged by the upstream AI provider

**Note:** The `upstream_inference_cost` field only applies to BYOK (Bring Your Own Key) requests.

<Note title="Performance Impact">
  Enabling usage accounting will add a few hundred milliseconds to the last
  response as the API calculates token counts and costs. This only affects the
  final message and does not impact overall streaming performance.
</Note>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
