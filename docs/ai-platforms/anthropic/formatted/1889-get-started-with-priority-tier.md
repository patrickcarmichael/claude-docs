---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get started with Priority Tier

You may want to commit to Priority Tier capacity if you are interested in:

* **Higher availability**: Target 99.5% uptime with prioritized computational resources
* **Cost Control**: Predictable spend and discounts for longer commitments
* **Flexible overflow**: Automatically falls back to standard tier when you exceed your committed capacity

Committing to Priority Tier will involve deciding:

* A number of input tokens per minute
* A number of output tokens per minute
* A commitment duration (1, 3, 6, or 12 months)
* A specific model version

>   **📝 Note**
>
> The ratio of input to output tokens you purchase matters. Sizing your Priority Tier capacity to align with your actual traffic patterns helps you maximize utilization of your purchased tokens.

### Supported models

Priority Tier is supported by:

* Claude Opus 4.1
* Claude Opus 4
* Claude Sonnet 4
* Claude Sonnet 3.7
* Claude Haiku 3.5

Check the [model overview page](/en/docs/about-claude/models/overview) for more details on our models.

### How to access Priority Tier

To begin using Priority Tier:

1. [Contact sales](https://claude.com/contact-sales/priority-tier) to complete provisioning
2. (Optional) Update your API requests to optionally set the `service_tier` parameter to `auto`
3. Monitor your usage through response headers and the Claude Console


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
