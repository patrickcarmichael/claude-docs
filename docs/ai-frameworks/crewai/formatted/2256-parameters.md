---
title: "Crewai: Parameters"
description: "Parameters section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Parameters


### PatronusEvalTool

The `PatronusEvalTool` does not require any parameters during initialization. It automatically fetches available evaluators and criteria from the Patronus API.

### PatronusPredefinedCriteriaEvalTool

The `PatronusPredefinedCriteriaEvalTool` accepts the following parameters during initialization:

* **evaluators**: Required. A list of dictionaries containing the evaluator and criteria to use. For example: `[{"evaluator": "judge", "criteria": "contains-code"}]`.

### PatronusLocalEvaluatorTool

The `PatronusLocalEvaluatorTool` accepts the following parameters during initialization:

* **patronus\_client**: Required. The Patronus client instance.
* **evaluator**: Optional. The name of the registered local evaluator to use. Default is an empty string.
* **evaluated\_model\_gold\_answer**: Optional. The gold answer to use for evaluation. Default is an empty string.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run the crew](./2255-create-and-run-the-crew.md)

**Next:** [Usage →](./2257-usage.md)
