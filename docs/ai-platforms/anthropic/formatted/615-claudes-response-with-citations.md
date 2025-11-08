---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Claude's response with citations

Regardless of how search results are provided, Claude automatically includes citations when using information from them:
```json
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "To authenticate API requests, you need to include an API key in the Authorization header",
      "citations": [
        {
          "type": "search_result_location",
          "source": "https://docs.company.com/api-reference",
          "title": "API Reference - Authentication",
          "cited_text": "All API requests must include an API key in the Authorization header",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 0
        }
      ]
    },
    {
      "type": "text",
      "text": ". You can generate API keys from your dashboard",
      "citations": [
        {
          "type": "search_result_location",
          "source": "https://docs.company.com/api-reference",
          "title": "API Reference - Authentication",
          "cited_text": "Keys can be generated from the dashboard",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 0
        }
      ]
    },
    {
      "type": "text",
      "text": ". The rate limits are 1,000 requests per hour for the standard tier and 10,000 requests per hour for the premium tier.",
      "citations": [
        {
          "type": "search_result_location",
          "source": "https://docs.company.com/api-reference",
          "title": "API Reference - Authentication",
          "cited_text": "Rate limits: 1000 requests per hour for standard tier, 10000 for premium",
          "search_result_index": 0,
          "start_block_index": 0,
          "end_block_index": 0
        }
      ]
    }
  ]
}
```

### Citation fields

Each citation includes:

| Field                 | Type           | Description                                                   |
| --------------------- | -------------- | ------------------------------------------------------------- |
| `type`                | string         | Always `"search_result_location"` for search result citations |
| `source`              | string         | The source from the original search result                    |
| `title`               | string or null | The title from the original search result                     |
| `cited_text`          | string         | The exact text being cited                                    |
| `search_result_index` | integer        | Index of the search result (0-based)                          |
| `start_block_index`   | integer        | Starting position in the content array                        |
| `end_block_index`     | integer        | Ending position in the content array                          |

Note: The `search_result_index` refers to the index of the search result content block (0-based), regardless of how the search results were provided (tool call or top-level content).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
