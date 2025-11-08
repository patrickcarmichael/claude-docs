---
title: "Crewai: Assigning Processes to a Crew"
description: "Assigning Processes to a Crew section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Assigning Processes to a Crew


To assign a process to a crew, specify the process type upon crew creation to set the execution strategy. For a hierarchical process, ensure to define `manager_llm` or `manager_agent` for the manager agent.

```python  theme={null}
from crewai import Crew, Process

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The Role of Processes in Teamwork](./263-the-role-of-processes-in-teamwork.md)

**Next:** [Example: Creating a crew with a sequential process →](./265-example-creating-a-crew-with-a-sequential-process.md)
