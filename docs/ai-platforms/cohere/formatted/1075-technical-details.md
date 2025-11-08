---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Technical Details

`command-r-08-2024` shows improved performance for multilingual retrieval-augmented generation (RAG) and tool use. More broadly, `command-r-08-2024` is better at math, code and reasoning and is competitive with the previous version of the larger Command R+ model.

`command-r-08-2024` delivers around 50% higher throughput and 20% lower latencies as compared to the previous Command R version, while cutting the hardware footprint required to serve the model by half. Similarly, `command-r-plus-08-2024` delivers roughly 50% higher throughput and 25% lower latencies as compared to the previous Command R+ version, while keeping the hardware footprint the same.

Both models include the following feature improvements:

* For tool use, `command-r-08-2024` and `command-r-plus-08-2024` have demonstrated improved decision-making around which tool to use in which context, and whether or not to use a tool.
* Improved instruction following in the preamble.
* Improved multilingual RAG searches in the language of the user with improved responses.
* Better structured data analysis for structured data manipulation.
* Better structured data creation from unstructured natural language instructions.
* Improved robustness to non-semantic prompt changes like white space or new lines.
* The models will decline unanswerable questions.
* The models have improved citation quality and users can now turn off citations for RAG workflows.
* For `command-r-08-2024` there are meaningful improvements on length and formatting control.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
