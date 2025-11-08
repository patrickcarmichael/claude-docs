---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Frequently asked questions

### How fresh is the analytics data?

Claude Code analytics data typically appears within 1 hour of user activity completion. To ensure consistent pagination results, only data older than 1 hour is included in responses.

### Can I get real-time metrics?

No, this API provides daily aggregated metrics only. For real-time monitoring, consider using the [OpenTelemetry integration](https://code.claude.com/docs/monitoring-usage).

### How are users identified in the data?

Users are identified through the `actor` field in two ways:

* **`user_actor`**: Contains `email_address` for users who authenticate via OAuth (most common)
* **`api_actor`**: Contains `api_key_name` for users who authenticate via API key

The `customer_type` field indicates whether the usage is from `api` customers (API PAYG) or `subscription` customers (Pro/Team plans).

### What's the data retention period?

Historical Claude Code analytics data is retained and accessible through the API. There is no specified deletion period for this data.

### Which Claude Code deployments are supported?

This API only tracks Claude Code usage on the Claude API (1st party). Usage on Amazon Bedrock, Google Vertex AI, or other third-party platforms is not included.

### What does it cost to use this API?

The Claude Code Analytics API is free to use for all organizations with access to the Admin API.

### How do I calculate tool acceptance rates?

Tool acceptance rate = `accepted / (accepted + rejected)` for each tool type. For example, if the edit tool shows 45 accepted and 5 rejected, the acceptance rate is 90%.

### What time zone is used for the date parameter?

All dates are in UTC. The `starting_at` parameter should be in YYYY-MM-DD format and represents UTC midnight for that day.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
