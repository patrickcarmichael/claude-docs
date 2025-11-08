---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 2. Configure Together AI

Instead of using the default Qwen OAuth, you'll configure Qwen Code to use Together AI's OpenAI-compatible API.

### Method 1: Environment Variables (Recommended)

Set up your environment variables:
```bash
export OPENAI_API_KEY="your_together_api_key_here"
export OPENAI_BASE_URL="https://api.together.xyz/v1"
export OPENAI_MODEL="your_chosen_model"
```

### Method 2: Project .env File

Create a `.env` file in your project root:
```env
OPENAI_API_KEY=your_together_api_key_here
OPENAI_BASE_URL=https://api.together.xyz/v1
OPENAI_MODEL=your_chosen_model
```

### Get Your Together AI Credentials

1. **API Key**: Get your [Together AI API key](https://api.together.xyz/settings/api-keys)
2. **Base URL**: Use `https://api.together.xyz/v1` for Together AI
3. **Model**: Choose from [Together AI's model catalog](https://www.together.ai/models)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
