---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Credit and Billing Systems

<AccordionGroup>
  <Accordion title="What purchase options exist?">
    OpenRouter uses a credit system where the base currency is US dollars. All
    of the pricing on our site and API is denoted in dollars. Users can top up
    their balance manually or set up auto top up so that the balance is
    replenished when it gets below the set threshold.
  </Accordion>

  <Accordion title="Do credits expire?">
    Per our [terms](https://openrouter.ai/terms), we reserve the right to expire
    unused credits after one year of purchase.
  </Accordion>

  <Accordion title="My credits haven't showed up in my account">
    If you paid using Stripe, sometimes there is an issue with the Stripe
    integration and credits can get delayed in showing up on your account. Please allow up to one hour.
    If your credits still have not appeared after an hour, check to confirm you have not been charged and
    that you do not have a stripe receipt email. If you do not have a receipt email or have not been charged,
    your card may have been declined. Please try again with a different card or payment method.

    If you have been charged and still do not have credits, please reach out to us via email
    at [support@openrouter.ai](mailto:support@openrouter.ai) with details of the purchase.

    If you paid using crypto, please reach out to us via email at [support@openrouter.ai](mailto:support@openrouter.ai)
    and we will look into it.
  </Accordion>

  <Accordion title="What's the refund policy?">
    Refunds for unused Credits may be requested within twenty-four (24) hours from the time the transaction was processed. If no refund request is received within twenty-four (24) hours following the purchase, any unused Credits become non-refundable. To request a refund within the eligible period, you can use the refund button on the [Credits](https://openrouter.ai/settings/credits) page. The unused credit amount will be refunded to your payment method; the platform fees are non-refundable. Note that cryptocurrency payments are never refundable.
  </Accordion>

  <Accordion title="How to monitor credit usage?">
    The [Activity](https://openrouter.ai/activity) page allows users to view
    their historic usage and filter the usage by model, provider and api key.

    We also provide a [credits api](/docs/api-reference/get-credits) that has
    live information about the balance and remaining credits for the account.
  </Accordion>

  <Accordion title="What free tier options exist?">
    All new users receive a very small free allowance to be able to test out OpenRouter.
    There are many [free models](https://openrouter.ai/models?max_price=0) available
    on OpenRouter, it is important to note that these models have low rate limits ({FREE_MODEL_NO_CREDITS_RPD} requests per day total)
    and are usually not suitable for production use. If you have purchased at least {FREE_MODEL_CREDITS_THRESHOLD} credits,
    the free models will be limited to {FREE_MODEL_HAS_CREDITS_RPD} requests per day.
  </Accordion>

  <Accordion title="How do volume discounts work?">
    OpenRouter does not currently offer volume discounts, but you can reach out to us
    over email if you think you have an exceptional use case.
  </Accordion>

  <Accordion title="What payment methods are accepted?">
    We accept all major credit cards, AliPay and cryptocurrency payments in
    USDC. We are working on integrating PayPal soon, if there are any payment
    methods that you would like us to support please reach out on [Discord](https://discord.gg/openrouter).
  </Accordion>

  <Accordion title="How does OpenRouter make money?">
    We charge a small [fee](/docs/faq#pricing-and-fees) when purchasing credits. We never mark-up the pricing
    of the underlying providers, and you'll always pay the same as the provider's
    listed price.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
