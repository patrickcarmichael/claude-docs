---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a new project using create-mastra

npx create-mastra@latest
```
You'll be guided through prompts to set up your project. For this example, select:

* Name your project: my-mastra-openrouter-app
* Components: Agents (recommended)
* For default provider, select OpenAI (recommended) - we'll configure OpenRouter manually later
* Optionally include example code

For detailed instructions on setting up a Mastra project manually or adding Mastra to an existing project, refer to the [official Mastra documentation](https://mastra.ai/en/docs/getting-started/installation).

### Step 2: Configure your environment variables

After creating your project with `create-mastra`, you'll find a `.env.development` file in your project root. Since we selected OpenAI during setup but will be using OpenRouter instead:

1. Open the `.env.development` file
2. Remove or comment out the `OPENAI_API_KEY` line
3. Add your OpenRouter API key:
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
