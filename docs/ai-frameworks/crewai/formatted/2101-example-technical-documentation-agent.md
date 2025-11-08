---
title: "Crewai: Example: Technical Documentation Agent"
description: "Example: Technical Documentation Agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example: Technical Documentation Agent

tech_writer = Agent(
    role="API Documentation Specialist",  # Specific role for clear LLM requirements
    goal="Create comprehensive, developer-friendly API documentation",
    backstory="""
    You're a technical writer with 8+ years documenting REST APIs, GraphQL endpoints,
    and SDK integration guides. You've worked with developer tools companies and
    understand what developers need: clear examples, comprehensive error handling,
    and practical use cases. You prioritize accuracy and usability over marketing fluff.
    """,
    llm=LLM(
        model="claude-3-5-sonnet",  # Excellent for technical writing
        temperature=0.1  # Low temperature for accuracy
    ),
    tools=[code_analyzer_tool, api_scanner_tool],
    verbose=True
)
```

**Alignment Checklist:**

* ✅ **Role Specificity**: Clear domain and responsibilities
* ✅ **LLM Match**: Model strengths align with role requirements
* ✅ **Backstory Depth**: Provides domain context the LLM can leverage
* ✅ **Tool Integration**: Tools support the agent's specialized function
* ✅ **Parameter Tuning**: Temperature and settings optimize for role needs

The key is creating agents where every configuration choice reinforces your LLM selection strategy, maximizing performance while optimizing costs.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← This context enables Claude to perform like a domain expert](./2100-this-context-enables-claude-to-perform-like-a-doma.md)

**Next:** [Practical Implementation Checklist →](./2102-practical-implementation-checklist.md)
