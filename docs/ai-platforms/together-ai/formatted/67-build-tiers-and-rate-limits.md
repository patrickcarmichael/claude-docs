---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Build Tiers and Rate Limits

Together AI uses a system of Build Tiers to reward customers as they continue to use our service. The more you do on Together, the higher your limits are!

There are 5 build tiers. If you find yourself running into rate limits once you're on Build Tier 5, a Scale or Enterprise plan may be a better fit for your needs.

### Required Spend and Rate Limits

You can move up to the next build tier by paying your monthly bill, or by purchasing credits.

Build Tiers are based on lifetime spend.

| Build Tiers  | Total Spend | LLMs     | Embeddings | Re-rank   |
| ------------ | ----------- | -------- | ---------- | --------- |
| Build Tier 1 | \$5.00      | 600 RPM  | 3000 RPM   | 500,000   |
| Build Tier 2 | \$50.00     | 1800 RPM | 5000 RPM   | 1,500,000 |
| Build Tier 3 | \$100.00    | 3000 RPM | 5000 RPM   | 2,000,000 |
| Build Tier 4 | \$250.00    | 4500 RPM | 10,000 RPM | 3,000,000 |
| Build Tier 5 | \$1000.00   | 6000 RPM | 10,000 RPM | 5,000,000 |

### Model Access by Build Tier

Some models have minimum Build Tier requirements beyond the standard rate limits.

#### Image Models

* **Build Tier 1 and above:** Access to Flux.1 \[schnell] (free and Turbo), Flux.1 Dev, Flux.1 Canny, Flux.1 Depth, Flux.1 Redux, and Flux.1 Kontext \[dev]

* **Build Tier 2 and above:** Access to Flux Pro models, including Flux.1 \[pro] and Flux1.1 \[pro]

**Note:** Model access requirements may change based on demand and availability. Check the model documentation for the most current access requirements.

### Important Note About Build Tier Access Restrictions

Even with a positive balance and no usage limit set, you may still encounter access restrictions due to Build Tier requirements. Build tiers are determined by actual account spend (purchased credits or platform usage), not free credits.

**Key points to remember:**

* Free credits don't count toward tier upgrades

* Build Tier 1 requires \$5 of actual account spend

* Build Tier 2 requires \$50 of actual account spend

* Some premium models (including Flux Pro 1.1, Flux Pro 1, and other high-end models) are restricted to Build Tier 2 or higher

* Access restrictions apply regardless of your credit balance or usage limit settings

**Common scenarios:**

* If you're seeing "Free tier" access errors despite having credits, you may need to purchase credits to upgrade to Build Tier 1

* If you encounter "tier access" errors for premium models, you may need Build Tier 2 status (\$50 total spend)

If you're experiencing access issues with a positive balance, check whether your credits are free credits or purchased credits and verify your account tier in your billing settings.

### Exceptions

Sometimes due to the popularity of a model we may need to implement custom rate limits or access restrictions. These exceptions will be listed in our documentation.

Keep in mind that once the limit is hit and enforced, any usage of Together AI services will be blocked until you increase the limit or buy a credit pack.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
