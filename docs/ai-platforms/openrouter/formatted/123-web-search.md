---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Web Search

> Enable real-time web search capabilities in your AI model responses. Add factual, up-to-date information to any model's output with OpenRouter's web search feature.

You can incorporate relevant web search results for *any* model on OpenRouter by activating and customizing the `web` plugin, or by appending `:online` to the model slug:
```json
{
  "model": "openai/gpt-4o:online"
}
```
This is a shortcut for using the `web` plugin, and is exactly equivalent to:
```json
{
  "model": "openrouter/auto",
  "plugins": [{ "id": "web" }]
}
```
The web search plugin is powered by native search for Anthropic and OpenAI natively and by [Exa](https://exa.ai) for other models. For Exa, it uses their ["auto"](https://docs.exa.ai/reference/how-exa-search-works#combining-neural-and-keyword-the-best-of-both-worlds-through-exa-auto-search) method (a combination of keyword search and embeddings-based web search) to find the most relevant results and augment/ground your prompt.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
