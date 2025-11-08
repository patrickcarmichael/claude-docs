---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Current Model Upgrades + New Command Beta Model

> Introducing new and improved Medium and XLarge models, plus a Command model for precise responses to commands.

**New & Improved Medium & Extremely Large**

The new and improved `medium` and `x-large` outperform our existing generation models on most downstream tasks, including summarization, paraphrasing, classification, and extraction, as measured by our internal task-based benchmarks.\
At this time, all baseline calls to `x-large` and `medium` will still route to previous versions of the models (namely, xlarge-20220609 and  medium-20220926). To access the new and improved versions, you’ll need to specify the release date in the Playground or your API call: `xlarge-20221108` and `medium-20221108`.

Older versions of the models (xlarge-20220609 & medium-20220926) will be deprecated on December 2, 2022.

**NEW Command Model (Beta)**

We’re also introducing a Beta of our new Command model, a generative model that’s conditioned to respond well to single-statement commands. Learn more about how to prompt `command-xlarge-20221108`. You can expect to see `command-xlarge-20221108` evolve dramatically in performance over the coming weeks.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
