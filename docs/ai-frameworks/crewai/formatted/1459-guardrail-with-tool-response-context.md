---
title: "Crewai: Guardrail with tool response context"
description: "Guardrail with tool response context section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Guardrail with tool response context

weather_guardrail = HallucinationGuardrail(
    context="Current weather information for the requested location",
    llm=LLM(model="gpt-4o-mini"),
    tool_response="Weather API returned: Temperature 22°C, Humidity 65%, Clear skies"
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Strict guardrail requiring high faithfulness score](./1458-strict-guardrail-requiring-high-faithfulness-score.md)

**Next:** [How It Works →](./1460-how-it-works.md)
