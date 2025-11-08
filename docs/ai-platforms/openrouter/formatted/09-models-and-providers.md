---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Models and Providers

<AccordionGroup>
  <Accordion title="What LLM models does OpenRouter support?">
    OpenRouter provides access to a wide variety of LLM models, including frontier models from major AI labs.
    For a complete list of models you can visit the [models browser](https://openrouter.ai/models) or fetch the list through the [models api](https://openrouter.ai/api/v1/models).
  </Accordion>

  <Accordion title="How frequently are new models added?">
    We work on adding models as quickly as we can. We often have partnerships with
    the labs releasing models and can release models as soon as they are
    available. If there is a model missing that you'd like OpenRouter to support, feel free to message us on
    [Discord](https://discord.gg/openrouter).
  </Accordion>

  <Accordion title="What are model variants?">
    Variants are suffixes that can be added to the model slug to change its behavior.

    Static variants can only be used with specific models and these are listed in our [models api](https://openrouter.ai/api/v1/models).

    1. `:free` - The model is always provided for free and has low rate limits.
    2. `:beta` - The model is not moderated by OpenRouter.
    3. `:extended` - The model has longer than usual context length.
    4. `:exacto` - The model only uses OpenRouter-curated high-quality endpoints.
    5. `:thinking` - The model supports reasoning by default.

    Dynamic variants can be used on all models and they change the behavior of how the request is routed or used.

    1. `:online` - All requests will run a query to extract web results that are attached to the prompt.
    2. `:nitro` - Providers will be sorted by throughput rather than the default sort, optimizing for faster response times.
    3. `:floor` - Providers will be sorted by price rather than the default sort, prioritizing the most cost-effective options.
  </Accordion>

  <Accordion title="I am an inference provider, how can I get listed on OpenRouter?">
    You can read our requirements at the [Providers
    page](/docs/use-cases/for-providers). If you would like to contact us, the best
    place to reach us is over email.
  </Accordion>

  <Accordion title="What is the expected latency/response time for different models?">
    For each model on OpenRouter we show the latency (time to first token) and the token
    throughput for all providers. You can use this to estimate how long requests
    will take. If you would like to optimize for throughput you can use the
    `:nitro` variant to route to the fastest provider.
  </Accordion>

  <Accordion title="How does model fallback work if a provider is unavailable?">
    If a provider returns an error OpenRouter will automatically fall back to the
    next provider. This happens transparently to the user and allows production
    apps to be much more resilient. OpenRouter has a lot of options to configure
    the provider routing behavior. The full documentation can be found [here](/docs/features/provider-routing).
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
