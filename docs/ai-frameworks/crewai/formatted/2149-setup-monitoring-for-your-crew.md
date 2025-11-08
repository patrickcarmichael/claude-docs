---
title: "Crewai: setup monitoring for your crew"
description: "setup monitoring for your crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# setup monitoring for your crew

tracer_provider = register(
    endpoint="http://localhost:6006/v1/traces")
CrewAIInstrumentor().instrument(skip_dep_check=True, tracer_provider=tracer_provider)
search_tool = SerperDevTool()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set environment variables](./2148-set-environment-variables.md)

**Next:** [Define your agents with roles and goals →](./2150-define-your-agents-with-roles-and-goals.md)
