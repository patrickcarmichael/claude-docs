---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Pricing and Fees

<AccordionGroup>
  <Accordion title="What are the fees for using OpenRouter?">
    OpenRouter charges a {getTotalFeeString('stripe')} fee when you purchase credits. We pass through
    the pricing of the underlying model providers without any markup, so you pay
    the same rate as you would directly with the provider.

    Crypto payments are charged a fee of {getTotalFeeString('coinbase')}.
  </Accordion>

  <Accordion title="Is there a fee for using my own provider keys (BYOK)?">
    Yes, if you choose to use your own provider API keys (Bring Your Own Key -
    BYOK), the first {toHumanNumber(BYOK_FEE_MONTHLY_REQUEST_THRESHOLD)} BYOK
    requests per-month are free, and for all subsequent usage there is a fee
    of {bn(openRouterBYOKFee.fraction).times(100).toString()}% of what the same
    model and provider would normally cost on OpenRouter. This fee is deducted
    from your OpenRouter credits. This allows you to manage your rate limits and
    costs directly with the provider while still leveraging OpenRouter's unified
    interface.
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
