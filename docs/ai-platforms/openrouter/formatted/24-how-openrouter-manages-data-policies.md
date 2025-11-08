---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How OpenRouter Manages Data Policies

OpenRouter works with providers to understand each of their data policies and structures the policy data in a way that gives you control over which providers you want to route to.

Note that a provider's general policy may differ from the specific policy for a given endpoint. OpenRouter keeps track of the specific policy for each endpoint, works with providers to keep these policies up to date, and in some cases creates special agreements with providers to ensure data retention or training policies that are more privacy-focused than their default policies.

>   **📝 Note**
>
> If OpenRouter is not able to establish or ascertain a clear policy for a provider or endpoint, we take a conservative stance and assume that the endpoint both retains and trains on data and mark it as such.

A full list of providers and their data policies can be found [here](/docs/features/privacy-and-logging#data-retention--logging). Note that this list shows the default policy for each provider; if there is a particular endpoint that has a policy that differs from the provider default, it may not be available if "ZDR Only" is enabled.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
