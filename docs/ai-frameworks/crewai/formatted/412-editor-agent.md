---
title: "Crewai: Editor Agent"
description: "Editor Agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Editor Agent

role: "Content Quality Editor"
goal: "Ensure content is accurate, well-structured, and polished while maintaining consistency"
backstory: "With years of experience in publishing, you have a keen eye for detail..."
```

### Creating Specialized Tool Users

Some agents can be designed specifically to leverage certain tools effectively:

```yaml  theme={null}
role: "Data Analysis Specialist"
goal: "Derive meaningful insights from complex datasets through statistical analysis"
backstory: "With a background in data science, you excel at working with structured and unstructured data..."
tools: [PythonREPLTool, DataVisualizationTool, CSVAnalysisTool]
```

### Tailoring Agents to LLM Capabilities

Different LLMs have different strengths. Design your agents with these capabilities in mind:

```yaml  theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Writer Agent](./411-writer-agent.md)

**Next:** [For complex reasoning tasks →](./413-for-complex-reasoning-tasks.md)
