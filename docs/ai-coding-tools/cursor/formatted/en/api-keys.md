---
title: "API Keys"
source: "https://docs.cursor.com/en/settings/api-keys"
language: "en"
language_name: "English"
---

# API Keys
Source: https://docs.cursor.com/en/settings/api-keys

Bring your own LLM provider

Use your own API keys to send unlimited AI messages at your own cost. When configured, Cursor will use your API keys to call LLM providers directly.

To use your API key, go to `Cursor Settings` > `Models` and enter your API keys. Click **Verify**. Once validated, your API key is enabled.

<Warning>
  Custom API keys only work with standard chat models. Features requiring specialized models (like Tab Completion) will continue using Cursor's built-in models.
</Warning>

## Supported providers

* **OpenAI** - Standard, non-reasoning chat models only. The model picker will show the OpenAI models available.
* **Anthropic** - All Claude models available through the Anthropic API.
* **Google** - Gemini models available through the Google AI API.
* **Azure OpenAI** - Models deployed in your Azure OpenAI Service instance.
* **AWS Bedrock** - Use AWS access keys, secret keys, or IAM roles. Works with models available in your Bedrock configuration.

A unique external ID is generated after validating your Bedrock IAM role, which can be added to your IAM role trust policy for additional security.

## FAQ

<AccordionGroup>
  <Accordion title="Will my API key be stored or leave my device?">
    Your API key won't be stored but is sent to our server with every request. All requests are routed through our backend for final prompt building.
  </Accordion>
</AccordionGroup>

---

← Previous: [Models](./models.md) | [Index](./index.md) | Next: [Tab](./tab.md) →