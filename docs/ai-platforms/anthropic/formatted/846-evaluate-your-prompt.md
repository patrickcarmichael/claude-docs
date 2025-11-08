---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Evaluate your prompt

Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate performance based on the success criteria and thresholds you established earlier.

To run your evaluation, you will need test cases to run it on. The rest of this guide assumes you have already [developed your test cases](/en/docs/test-and-evaluate/develop-tests).

### Build an evaluation function

Our example evaluation for this guide measures Claude’s performance along three key metrics:

* Accuracy
* Cost per classification

You may need to assess Claude on other axes depending on what factors that are important to you.

To assess this, we first have to modify the script we wrote and add a function to compare the predicted intent with the actual intent and calculate the percentage of correct predictions. We also have to add in cost calculation and time measurement functionality.
```python
import anthropic
import re

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
