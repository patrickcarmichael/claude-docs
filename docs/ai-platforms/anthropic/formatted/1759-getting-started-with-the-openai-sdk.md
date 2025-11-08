---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting started with the OpenAI SDK

To use the OpenAI SDK compatibility feature, you'll need to:

1. Use an official OpenAI SDK
2. Change the following
   * Update your base URL to point to the Claude API
   * Replace your API key with an [Claude API key](https://console.anthropic.com/settings/keys)
   * Update your model name to use a [Claude model](/en/docs/about-claude/models/overview)
3. Review the documentation below for what features are supported

### Quick start example

```Python
  from openai import OpenAI

  client = OpenAI(
      api_key="ANTHROPIC_API_KEY",  # Your Claude API key

      base_url="https://api.anthropic.com/v1/"  # the Claude API endpoint

  )

  response = client.chat.completions.create(
      model="claude-sonnet-4-5", # Anthropic model name

      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Who are you?"}
      ],
  )

  print(response.choices[0].message.content)
```
```TypeScript
  import OpenAI from 'openai';

  const openai = new OpenAI({
      apiKey: "ANTHROPIC_API_KEY",   // Your Claude API key
      baseURL: "https://api.anthropic.com/v1/",  // Claude API endpoint
  });

  const response = await openai.chat.completions.create({
      messages: [
          { role: "user", content: "Who are you?" }
      ],
      model: "claude-sonnet-4-5", // Claude model name
  });

  console.log(response.choices[0].message.content);
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
