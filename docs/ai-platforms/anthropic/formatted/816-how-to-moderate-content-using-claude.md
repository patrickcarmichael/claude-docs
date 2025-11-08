---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to moderate content using Claude

### Select the right Claude model

When selecting a model, it’s important to consider the size of your data. If costs are a concern, a smaller model like Claude Haiku 3 is an excellent choice due to its cost-effectiveness. Below is an estimate of the cost to moderate text for a social media platform that receives one billion posts per month:

* **Content size**
  * Posts per month: 1bn
  * Characters per post: 100
  * Total characters: 100bn

* **Estimated tokens**
  * Input tokens: 28.6bn (assuming 1 token per 3.5 characters)
  * Percentage of messages flagged: 3%
  * Output tokens per flagged message: 50
  * Total output tokens: 1.5bn

* **Claude Haiku 3 estimated cost**
  * Input token cost: 2,860 MTok \* \$0.25/MTok = \$715
  * Output token cost: 1,500 MTok \* \$1.25/MTok = \$1,875
  * Monthly cost: \$715 + \$1,875 = \$2,590

* **Claude Sonnet 4.5 estimated cost**
  * Input token cost: 2,860 MTok \* \$3.00/MTok = \$8,580
  * Output token cost: 1,500 MTok \* \$15.00/MTok = \$22,500
  * Monthly cost: \$8,580 + \$22,500 = \$31,080

<Tip>Actual costs may differ from these estimates. These estimates are based on the prompt highlighted in the section on [batch processing](#consider-batch-processing). Output tokens can be reduced even further by removing the `explanation` field from the response.</Tip>

### Build a strong prompt

In order to use Claude for content moderation, Claude must understand the moderation requirements of your application. Let’s start by writing a prompt that allows you to define your moderation needs:
```python
import anthropic
import json

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
