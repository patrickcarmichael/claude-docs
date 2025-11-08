---
title: "Crewai: Example of guardrail result structure"
description: "Example of guardrail result structure section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example of guardrail result structure

{
    "valid": False,
    "feedback": "Content appears to be hallucinated (score: 4.2/10, verdict: HALLUCINATED). The output contains information not supported by the provided context."
}
```

### Result Properties

* **valid**: Boolean indicating whether the output passed validation
* **feedback**: Detailed explanation when validation fails, including:
  * Faithfulness score
  * Verdict classification
  * Specific reasons for failure

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Guardrail Results](./1461-guardrail-results.md)

**Next:** [Integration with Task System →](./1463-integration-with-task-system.md)
