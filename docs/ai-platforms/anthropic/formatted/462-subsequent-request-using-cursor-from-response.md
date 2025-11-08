---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Subsequent request using cursor from response

curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&\
page=page_MjAyNS0wNS0xNFQwMDowMDowMFo=" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

### Request parameters

| Parameter     | Type    | Required | Description                                                             |
| ------------- | ------- | -------- | ----------------------------------------------------------------------- |
| `starting_at` | string  | Yes      | UTC date in YYYY-MM-DD format. Returns metrics for this single day only |
| `limit`       | integer | No       | Number of records per page (default: 20, max: 1000)                     |
| `page`        | string  | No       | Opaque cursor token from previous response's `next_page` field          |

### Available metrics

Each response record contains the following metrics for a single user on a single day:

#### Dimensions

* **date**: Date in RFC 3339 format (UTC timestamp)
* **actor**: The user or API key that performed the Claude Code actions (either `user_actor` with `email_address` or `api_actor` with `api_key_name`)
* **organization\_id**: Organization UUID
* **customer\_type**: Type of customer account (`api` for API customers, `subscription` for Pro/Team customers)
* **terminal\_type**: Type of terminal or environment where Claude Code was used (e.g., `vscode`, `iTerm.app`, `tmux`)

#### Core metrics

* **num\_sessions**: Number of distinct Claude Code sessions initiated by this actor
* **lines\_of\_code.added**: Total number of lines of code added across all files by Claude Code
* **lines\_of\_code.removed**: Total number of lines of code removed across all files by Claude Code
* **commits\_by\_claude\_code**: Number of git commits created through Claude Code's commit functionality
* **pull\_requests\_by\_claude\_code**: Number of pull requests created through Claude Code's PR functionality

#### Tool action metrics

Breakdown of tool action acceptance and rejection rates by tool type:

* **edit\_tool.accepted/rejected**: Number of Edit tool proposals that the user accepted/rejected
* **write\_tool.accepted/rejected**: Number of Write tool proposals that the user accepted/rejected
* **notebook\_edit\_tool.accepted/rejected**: Number of NotebookEdit tool proposals that the user accepted/rejected

#### Model breakdown

For each Claude model used:

* **model**: Claude model identifier (e.g., `claude-sonnet-4-5-20250929`)
* **tokens.input/output**: Input and output token counts for this model
* **tokens.cache\_read/cache\_creation**: Cache-related token usage for this model
* **estimated\_cost.amount**: Estimated cost in cents USD for this model
* **estimated\_cost.currency**: Currency code for the cost amount (currently always `USD`)

### Response structure

The API returns data in the following format:
```json
{
  "data": [
    {
      "date": "2025-09-01T00:00:00Z",
      "actor": {
        "type": "user_actor",
        "email_address": "developer@company.com"
      },
      "organization_id": "dc9f6c26-b22c-4831-8d01-0446bada88f1",
      "customer_type": "api",
      "terminal_type": "vscode",
      "core_metrics": {
        "num_sessions": 5,
        "lines_of_code": {
          "added": 1543,
          "removed": 892
        },
        "commits_by_claude_code": 12,
        "pull_requests_by_claude_code": 2
      },
      "tool_actions": {
        "edit_tool": {
          "accepted": 45,
          "rejected": 5
        },
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 2
        },
        "write_tool": {
          "accepted": 8,
          "rejected": 1
        },
        "notebook_edit_tool": {
          "accepted": 3,
          "rejected": 0
        }
      },
      "model_breakdown": [
        {
          "model": "claude-sonnet-4-5-20250929",
          "tokens": {
            "input": 100000,
            "output": 35000,
            "cache_read": 10000,
            "cache_creation": 5000
          },
          "estimated_cost": {
            "currency": "USD",
            "amount": 1025
          }
        }
      ]
    }
  ],
  "has_more": false,
  "next_page": null
}
```javascript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
