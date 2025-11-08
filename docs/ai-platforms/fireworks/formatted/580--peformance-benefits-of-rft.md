---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 🚀 Peformance Benefits of RFT

Before diving in to the tutorial, here's a summary of the accuracy we achieved, using the [OpenFlights dataset](https://openflights.org/data.html) as a base, across various models:

| Model                          | Accuracy on Test Set | Size  | Speed |
| ------------------------------ | -------------------- | ----- | ----- |
| **Qwen 2.5 7B (base)**         | 23.91%               | Small | Fast  |
| **DeepSeek V3**                | 27.17%               | Large | Slow  |
| **Kimi K2 Instruct**           | 28.26%               | Large | Slow  |
| **OpenAI GPT-4o**              | 23.91%               | Large | Slow  |
| **Anthropic Claude Sonnet 4**  | 29.35%               | Large | Slow  |
| **Qwen3 Coder 480B**           | 34.78%               | Large | Slow  |
| **Our Fine-Tuned Qwen 2.5 7B** | **56.52%** ✨         | Small | Fast  |

<div style={{ fontSize: '0.8em' }}>
  > Note on methodology: to compare accuracy across the above models, we created a synthetic dataset that mirrors the OpenFlights schema, an initial set of synthetic queries written by Qwen3 Coder 480B,
  > and a synthetic set of natural language questions (also written by Qwen3 Coder 480B) corresponding to those queries. The task above is for the LLM to translate each natural language question into SQL, and then execute the SQL query against the synthetic dataset.
  > Accuracy is computed as the percent of queries that return the correct result (N = 92). "Correct" is defined as the query returning the same result on the synthetic dataset as each initial synthetic query did.
  > Thus, the relative performance between these models is a more meaningful metric than the absolute performance. More details on the data and evaluation process can be found throughout the tutorial below.
</div>

**Key takeaway**: Our fine-tuned 7B model outperforms models that are 50-200x larger, while being faster and cheaper to run.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
