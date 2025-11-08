---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Configuring OpenAI to use Together's API

To start using Together with OpenAI's client libraries, pass in your Together API key to the `api_key` option, and change the `base_url` to `https://api.together.xyz/v1`:
```python
  import os
  import openai

  client = openai.OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )
```
```typescript
  import OpenAI from "openai";

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: "https://api.together.xyz/v1",
  });
```

You can find your API key in [your settings page](https://api.together.xyz/settings/api-keys). If you don't have an account, you can [register for free](https://api.together.ai/).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
