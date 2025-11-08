---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API Technical Specifications

<AccordionGroup>
  <Accordion title="What authentication methods are supported?">
    OpenRouter uses three authentication methods:

    1. Cookie-based authentication for the web interface and chatroom
    2. API keys (passed as Bearer tokens) for accessing the completions API and other core endpoints
    3. [Provisioning API keys](/docs/features/provisioning-api-keys) for programmatically managing API keys through the key management endpoints
  </Accordion>

  <Accordion title="How are rate limits calculated?">
    For free models, rate limits are determined by the credits that you have purchased.
    If you have purchased at least {FREE_MODEL_CREDITS_THRESHOLD} credits, your free model rate limit will be {FREE_MODEL_HAS_CREDITS_RPD} requests per day.
    Otherwise, you will be rate limited to {FREE_MODEL_NO_CREDITS_RPD} free model API requests per day.

    You can learn more about how rate limits work for paid accounts in our [rate limits documentation](/docs/api-reference/limits).
  </Accordion>

  <Accordion title="What API endpoints are available?">
    OpenRouter implements the OpenAI API specification for /completions and
    /chat/completions endpoints, allowing you to use any model with the same
    request/response format. Additional endpoints like /api/v1/models are also
    available. See our [API documentation](/docs/api-reference/overview) for
    detailed specifications.
  </Accordion>

  <Accordion title="What are the supported formats?">
    The API supports text and images.
    [Images](/docs/api-reference/overview#images--multimodal) can be passed as
    URLs or base64 encoded images. PDF and other file types are coming soon.
  </Accordion>

  <Accordion title="How does streaming work?">
    Streaming uses server-sent events (SSE) for real-time token delivery. Set
    `stream: true` in your request to enable streaming responses.
  </Accordion>

  <Accordion title="What SDK support is available?">
    OpenRouter is a drop-in replacement for OpenAI. Therefore, any SDKs that
    support OpenAI by default also support OpenRouter. Check out our
    [docs](/docs/community/open-ai-sdk) for more details.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
