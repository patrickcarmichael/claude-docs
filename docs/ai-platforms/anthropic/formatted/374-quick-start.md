---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quick start

Here's how to get started with computer use:
```python
  import anthropic

  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-sonnet-4-5",  # or another compatible model

      max_tokens=1024,
      tools=[
          {
            "type": "computer_20250124",
            "name": "computer",
            "display_width_px": 1024,
            "display_height_px": 768,
            "display_number": 1,
          },
          {
            "type": "text_editor_20250124",
            "name": "str_replace_editor"
          },
          {
            "type": "bash_20250124",
            "name": "bash"
          }
      ],
      messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
      betas=["computer-use-2025-01-24"]
  )
  print(response)
```
```bash
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: computer-use-2025-01-24" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "tools": [
        {
          "type": "computer_20250124",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1
        },
        {
          "type": "text_editor_20250124",
          "name": "str_replace_editor"
        },
        {
          "type": "bash_20250124",
          "name": "bash"
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Save a picture of a cat to my desktop."
        }
      ]
    }'
```typescript

>   **📝 Note**
>
> A beta header is only required for the computer use tool.

  The example above shows all three tools being used together, which requires the beta header because it includes the computer use tool.

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
