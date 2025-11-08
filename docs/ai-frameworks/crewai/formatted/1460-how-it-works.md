---
title: "Crewai: How It Works"
description: "How It Works section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## How It Works


### Validation Process

1. **Context Analysis**: The guardrail compares task output against the provided reference context
2. **Faithfulness Scoring**: Uses an internal evaluator to assign a faithfulness score (0-10)
3. **Verdict Determination**: Determines if content is faithful or contains hallucinations
4. **Threshold Checking**: If a custom threshold is set, validates against that score
5. **Feedback Generation**: Provides detailed reasons when validation fails

### Validation Logic

* **Default Mode**: Uses verdict-based validation (FAITHFUL vs HALLUCINATED)
* **Threshold Mode**: Requires faithfulness score to meet or exceed the specified threshold
* **Error Handling**: Gracefully handles evaluation errors and provides informative feedback

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Guardrail with tool response context](./1459-guardrail-with-tool-response-context.md)

**Next:** [Guardrail Results →](./1461-guardrail-results.md)
