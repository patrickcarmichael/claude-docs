---
title: "Crewai: Strict guardrail requiring high faithfulness score"
description: "Strict guardrail requiring high faithfulness score section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Strict guardrail requiring high faithfulness score

strict_guardrail = HallucinationGuardrail(
    context="Quantum computing uses qubits that exist in superposition states.",
    llm=LLM(model="gpt-4o-mini"),
    threshold=8.0  # Requires score >= 8 to pass validation
)
```

### Including Tool Response Context

When your task uses tools, you can include tool responses for more accurate validation:

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Advanced Configuration](./1457-advanced-configuration.md)

**Next:** [Guardrail with tool response context →](./1459-guardrail-with-tool-response-context.md)
