---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Claude Code Analytics API

Track Claude Code usage, productivity metrics, and developer activity across your organization with the `/v1/organizations/usage_report/claude_code` endpoint.

### Key concepts

* **Daily aggregation**: Returns metrics for a single day specified by the `starting_at` parameter
* **User-level data**: Each record represents one user's activity for the specified day
* **Productivity metrics**: Track sessions, lines of code, commits, pull requests, and tool usage
* **Token and cost data**: Monitor usage and estimated costs broken down by Claude model
* **Cursor-based pagination**: Handle large datasets with stable pagination using opaque cursors
* **Data freshness**: Metrics are available with up to 1-hour delay for consistency

For complete parameter details and response schemas, see the [Claude Code Analytics API reference](/en/api/admin-api/claude-code/get-claude-code-usage-report).

### Basic examples

#### Get analytics for a specific day

```bash
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

#### Get analytics with pagination

```bash

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
