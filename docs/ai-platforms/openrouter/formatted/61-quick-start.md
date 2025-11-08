---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quick Start

1. [Create a preset](/settings/presets). For example, select a model and restrict provider routing to just a few providers.
   ![Creating a new preset](file:9200af66-cd2b-4c02-b94a-127a22a3d830 "A new preset")

2. Make an API request to the preset:
```json
{
  "model": "@preset/ravenel-bridge",
  "messages": [
    {
      "role": "user",
      "content": "What's your opinion of the Golden Gate Bridge? Isn't it beautiful?"
    }
  ]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
