---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Per-Request ZDR Enforcement

In addition to the global ZDR setting in your [privacy settings](/settings/privacy), you can enforce Zero Data Retention on a per-request basis using the `zdr` parameter in your API calls.

The request-level `zdr` parameter operates as an "OR" with your account-wide ZDR setting - if either is enabled, ZDR enforcement will be applied. This means the per-request parameter can only be used to ensure ZDR is enabled for a specific request, not to override or disable account-wide ZDR enforcement.

This is useful for customers who don't want to globally enforce ZDR but need to ensure specific requests only route to ZDR endpoints.

### Usage

Include the `zdr` parameter in your provider preferences:
```json
{
  "model": "gpt-4",
  "messages": [...],
  "provider": {
    "zdr": true
  }
}
```
When `zdr` is set to `true`, the request will only be routed to endpoints that have a Zero Data Retention policy. When `zdr` is `false` or not provided, ZDR enforcement will still apply if enabled in your account settings.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
