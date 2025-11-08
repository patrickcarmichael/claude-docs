---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Usage

```python
  question = "Sally earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?"

  prompt_chain = [
      """Given the math problem, ONLY extract any relevant numerical information and how it can be used.""",
      """Given the numberical information extracted, ONLY express the steps you would take to solve the problem.""",
      """Given the steps, express the final answer to the problem.""",
  ]

  responses = serial_chain_workflow(question, prompt_chain)

  final_answer = responses[-1]
```
```typescript
  const question =
    "Sally earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?";

  const promptChain = [
    "Given the math problem, ONLY extract any relevant numerical information and how it can be used.",
    "Given the numberical information extracted, ONLY express the steps you would take to solve the problem.",
    "Given the steps, express the final answer to the problem.",
  ];

  async function main() {
    await serialChainWorkflow(question, promptChain);
  }

  main();
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
