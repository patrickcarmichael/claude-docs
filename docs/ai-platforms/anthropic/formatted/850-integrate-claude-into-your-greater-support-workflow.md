---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Integrate Claude into your greater support workflow

Proper integration requires that you make some decisions regarding how your Claude-based ticket routing script fits into the architecture of your greater ticket routing system.There are two ways you could do this:

* **Push-based:** The support ticket system you’re using (e.g. Zendesk) triggers your code by sending a webhook event to your routing service, which then classifies the intent and routes it.
  * This approach is more web-scalable, but needs you to expose a public endpoint.
* **Pull-Based:** Your code pulls for the latest tickets based on a given schedule and routes them at pull time.
  * This approach is easier to implement but might make unnecessary calls to the support ticket system when the pull frequency is too high or might be overly slow when the pull frequency is too low.

For either of these approaches, you will need to wrap your script in a service. The choice of approach depends on what APIs your support ticketing system provides.

***

<CardGroup cols={2}>
  <Card title="Classification cookbook" icon="link" href="https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/classification">
    Visit our classification cookbook for more example code and detailed eval guidance.
  </Card>

  <Card title="Claude Console" icon="link" href="https://console.anthropic.com/dashboard">
    Begin building and evaluating your workflow on the Claude Console.
  </Card>
</CardGroup>


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
