---
title: "Crewai: ✅ Solution: Provide better context and specific roles"
description: "✅ Solution: Provide better context and specific roles section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# ✅ Solution: Provide better context and specific roles

Task(
    description="""Write a technical blog post about machine learning.
    
    Context: Target audience is software developers with basic ML knowledge.
    Length: 1200 words
    Include: code examples, practical applications, best practices
    
    If you need specific technical details, delegate research to the researcher.""",
    ...
)
```

### Issue: Delegation Loops

**Symptoms:** Agents delegate back and forth indefinitely

```python  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← ✅ Solution: Ensure delegation is enabled](./62-solution-ensure-delegation-is-enabled.md)

**Next:** [✅ Solution: Clear hierarchy and responsibilities →](./64-solution-clear-hierarchy-and-responsibilities.md)
