---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Privacy and Data Logging

Please see our [Terms of Service](https://openrouter.ai/terms) and [Privacy Policy](https://openrouter.ai/privacy).

<AccordionGroup>
  <Accordion title="What data is logged during API use?">
    We log basic request metadata (timestamps, model used, token counts). Prompt
    and completion are not logged by default. We do zero logging of your prompts/completions,
    even if an error occurs, unless you opt-in to logging them.

    We have an opt-in [setting](https://openrouter.ai/settings/privacy) that
    lets users opt-in to log their prompts and completions in exchange for a 1%
    discount on usage costs.
  </Accordion>

  <Accordion title="What data is logged during Chatroom use?">
    The same data privacy applies to the chatroom as the API. All conversations
    in the chatroom are stored locally on your device. Conversations will not sync across devices.
    It is possible to export and import conversations using the settings menu in the chatroom.
  </Accordion>

  <Accordion title="What third-party sharing occurs?">
    OpenRouter is a proxy that sends your requests to the model provider for it to be completed.
    We work with all providers to, when possible, ensure that prompts and completions are not logged or used for training.
    Providers that do log, or where we have been unable to confirm their policy, will not be routed to unless the model training
    toggle is switched on in the [privacy settings](https://openrouter.ai/settings/privacy) tab.

    If you specify [provider routing](/docs/features/provider-routing) in your request, but none of the providers
    match the level of privacy specified in your account settings, you will get an error and your request will not complete.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
