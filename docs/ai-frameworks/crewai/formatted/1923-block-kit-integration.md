---
title: "Crewai: Block Kit Integration"
description: "Block Kit Integration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Block Kit Integration


Slack's Block Kit allows you to create rich, interactive messages. Here are some examples of how to use the `blocks` parameter:

### Simple Text with Attachment

```json  theme={null}
[
  {
    "text": "I am a test message",
    "attachments": [
      {
        "text": "And here's an attachment!"
      }
    ]
  }
]
```

### Rich Formatting with Sections

```json  theme={null}
[
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*Project Update*\nStatus: ✅ Complete"
    }
  },
  {
    "type": "divider"
  },
  {
    "type": "section",
    "text": {
      "type": "plain_text",
      "text": "All tasks have been completed successfully."
    }
  }
]
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Available Tools](./1922-available-tools.md)

**Next:** [Usage Examples →](./1924-usage-examples.md)
