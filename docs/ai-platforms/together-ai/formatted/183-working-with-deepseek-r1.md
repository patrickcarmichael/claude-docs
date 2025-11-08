---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Working with DeepSeek-R1

Reasoning models like DeepSeek-R1 should be used differently than standard non-reasoning models to get optimal results.

Here are some usage guides:

* **Temperature**: Use 0.5–0.7 (recommended 0.6) to balance creativity and coherence, avoiding repetitive or nonsensical outputs.
* **System Prompts**: Omit system prompts entirely. Provide all instructions directly in the user query.

Think of DeepSeek-R1 as a senior problem-solver – provide high-level objectives (e.g., "Analyze this data and identify trends") and let it determine the methodology.

* Strengths: Excels at open-ended reasoning, multi-step logic, and inferring unstated requirements.
* Over-prompting (e.g., micromanaging steps) can limit its ability to leverage advanced reasoning.
  Under-prompting (e.g., vague goals like "Help with math") may reduce specificity – balance clarity with flexibility.

For a more detailed guide on DeepSeek-R1 usage please see [Prompting DeepSeek-R1](/docs/prompting-deepseek-r1) .

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
