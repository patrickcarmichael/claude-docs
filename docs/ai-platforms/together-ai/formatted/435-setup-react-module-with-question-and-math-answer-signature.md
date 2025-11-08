---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## setup ReAct module with question and math answer signature

react = dspy.ReAct(
    "question -> answer: float",
    tools=[evaluate_math, search_wikipedia],
)

pred = react(
    question="What is 9362158 divided by the year of birth of David Gregory of Kinnairdy castle?"
)

print(pred.answer)
```

Learn more in our [DSPy Guide](https://docs.together.ai/docs/dspy) and explore our [DSPy Agents notebook](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/DSPy/DSPy_Agents.ipynb).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
