---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How it works

Search results can be provided in two ways:

1. **From tool calls** - Your custom tools return search results, enabling dynamic RAG applications
2. **As top-level content** - You provide search results directly in user messages for pre-fetched or cached content

In both cases, Claude can automatically cite information from the search results with proper source attribution.

### Search result schema

Search results use the following structure:
```json
{
  "type": "search_result",
  "source": "https://example.com/article",  // Required: Source URL or identifier
  "title": "Article Title",                  // Required: Title of the result
  "content": [                               // Required: Array of text blocks
    {
      "type": "text",
      "text": "The actual content of the search result..."
    }
  ],
  "citations": {                             // Optional: Citation configuration
    "enabled": true                          // Enable/disable citations for this result
  }
}
```

### Required fields

| Field     | Type   | Description                                           |
| --------- | ------ | ----------------------------------------------------- |
| `type`    | string | Must be `"search_result"`                             |
| `source`  | string | The source URL or identifier for the content          |
| `title`   | string | A descriptive title for the search result             |
| `content` | array  | An array of text blocks containing the actual content |

### Optional fields

| Field           | Type   | Description                                            |
| --------------- | ------ | ------------------------------------------------------ |
| `citations`     | object | Citation configuration with `enabled` boolean field    |
| `cache_control` | object | Cache control settings (e.g., `{"type": "ephemeral"}`) |

Each item in the `content` array must be a text block with:

* `type`: Must be `"text"`
* `text`: The actual text content (non-empty string)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
