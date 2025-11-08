---
title: "Crewai: Initialize the tool with the custom evaluator"
description: "Initialize the tool with the custom evaluator section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool with the custom evaluator

patronus_eval_tool = PatronusLocalEvaluatorTool(
    patronus_client=client,
    evaluator="random_evaluator",
    evaluated_model_gold_answer="example label",
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Register a custom evaluator](./2251-register-a-custom-evaluator.md)

**Next:** [Define an agent that uses the tool →](./2253-define-an-agent-that-uses-the-tool.md)
