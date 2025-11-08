---
title: "Crewai: Usage"
description: "Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage


When using the Patronus evaluation tools, you provide the model input, output, and context, and the tool returns the evaluation results from the Patronus API.

For the `PatronusEvalTool` and `PatronusPredefinedCriteriaEvalTool`, the following parameters are required when calling the tool:

* **evaluated\_model\_input**: The agent's task description in simple text.
* **evaluated\_model\_output**: The agent's output of the task.
* **evaluated\_model\_retrieved\_context**: The agent's context.

For the `PatronusLocalEvaluatorTool`, the same parameters are required, but the evaluator and gold answer are specified during initialization.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./2256-parameters.md)

**Next:** [Conclusion →](./2258-conclusion.md)
