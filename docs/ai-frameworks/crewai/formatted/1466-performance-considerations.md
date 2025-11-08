---
title: "Crewai: Performance Considerations"
description: "Performance Considerations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Performance Considerations


### Impact on Execution Time

* **Validation Overhead**: Each guardrail adds \~1-3 seconds per task
* **LLM Efficiency**: Choose efficient models for evaluation (e.g., gpt-4o-mini)

### Cost Optimization

* **Model Selection**: Use smaller, efficient models for guardrail evaluation
* **Context Size**: Keep reference context concise but comprehensive
* **Caching**: Consider caching validation results for repeated content

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Best Practices](./1465-best-practices.md)

**Next:** [Troubleshooting →](./1467-troubleshooting.md)
