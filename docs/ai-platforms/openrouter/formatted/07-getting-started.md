---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting started

<AccordionGroup>
  <Accordion title="Why should I use OpenRouter?">
    OpenRouter provides a unified API to access all the major LLM models on the
    market. It also allows users to aggregate their billing in one place and
    keep track of all of their usage using our analytics.

    OpenRouter passes through the pricing of the underlying providers, while pooling their uptime,
    so you get the same pricing you'd get from the provider directly, with a
    unified API and fallbacks so that you get much better uptime.
  </Accordion>

  <Accordion title="How do I get started with OpenRouter?">
    To get started, create an account and add credits on the
    [Credits](https://openrouter.ai/settings/credits) page. Credits are simply
    deposits on OpenRouter that you use for LLM inference.
    When you use the API or chat interface, we deduct the request cost from your
    credits. Each model and provider has a different price per million tokens.

    Once you have credits you can either use the chat room, or create API keys
    and start using the API. You can read our [quickstart](/docs/quickstart)
    guide for code samples and more.
  </Accordion>

  <Accordion title="How do I get support?">
    The best way to get technical support is to join our
    [Discord](https://discord.gg/openrouter) and ask the community in the #help forum.

    For billing and account management questions, please contact us at [support@openrouter.ai](mailto:support@openrouter.ai).
  </Accordion>

  <Accordion title="How do I get billed for my usage on OpenRouter?">
    For each model we have the pricing displayed per million tokens. There is
    usually a different price for prompt and completion tokens. There are also
    models that charge per request, for images and for reasoning tokens. All of
    these details will be visible on the models page.

    When you make a request to OpenRouter, we receive the total number of tokens processed
    by the provider. We then calculate the corresponding cost and deduct it from your credits.
    You can review your complete usage history in the [Activity tab](https://openrouter.ai/activity).

    You can also add the `usage: {include: true}` parameter to your chat request
    to get the usage information in the response.

    We pass through the pricing of the underlying providers; there is no markup
    on inference pricing (however we do charge a [fee](/docs/faq#pricing-and-fees) when purchasing credits).
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
