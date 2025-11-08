---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Command R August 2024 Release

Cohere's flagship text-generation models, Command R and Command R+, received a substantial update in August 2024. We chose to designate these models with time stamps, so in the API Command R 08-2024 is accesible with `command-r-08-2024`.

With the release, both models include the following feature improvements:

* For tool use, Command R and Command R+ have demonstrated improved decision-making around whether or not to use a tool.
* The updated models are better able to follow instructions included in the request's system message.
* Better structured data analysis for structured data manipulation.
* Improved robustness to non-semantic prompt changes like white space or new lines.
* Models will decline unanswerable questions and are now able to execute RAG workflows without citations

`command-r-08-2024` delivers around 50% higher throughput and 20% lower latencies as compared to the previous Command R version, while cutting the hardware footprint required to serve the model by half. Read more in the relevant blog post.

What's more, both these updated models can now operate in one of several safety modes, which gives developers more granular control over how models generate output in a variety of different contexts. Find more in these [safety modes docs](https://docs.cohere.com/docs/safety-modes).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
