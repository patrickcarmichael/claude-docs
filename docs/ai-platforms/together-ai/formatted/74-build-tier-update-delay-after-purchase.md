---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Build Tier Update Delay After Purchase

Purchasing Together AI credits can take up to **15 minutes** for our backend to finish updating your account's Build Tier and grant any new model access that comes with it. This delay is normal and does not affect the credits themselves; they are already reserved for you.

### What you may notice while the update is in progress

* Your **credit balance** in the dashboard may still show the old amount.
* **Tier-restricted models** (for example, Flux.Kontext) remain grayed out or return "insufficient tier" errors.
* API calls that require the new tier will continue to be rejected with HTTP 403 until propagation is complete.

### What you should do

1. **Wait up to 15 minutes** after your payment confirmation email arrives.
2. **Refresh the billing page** or re-query the `/v1/models` endpoint after the 15-minute mark.
3. If nothing changes, clear your browser cache or log out and back in to rule out a stale UI state.

**Still no change?** Open a support ticket in the dashboard under **Help > Contact Support** and include the email address used for the purchase and the approximate time of purchase (including time zone). Our team will verify the payment and, if necessary, force-sync your account to the correct Build Tier.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
