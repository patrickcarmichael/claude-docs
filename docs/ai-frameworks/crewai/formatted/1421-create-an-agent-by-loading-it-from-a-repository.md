---
title: "Crewai: Create an agent by loading it from a repository"
description: "Create an agent by loading it from a repository section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent by loading it from a repository

# The agent is loaded with all its predefined configurations
researcher = Agent(
    from_repository="market-research-agent"
)
```

### Overriding Repository Settings

You can override specific settings from the repository by providing them in the configuration:

```python  theme={null}
researcher = Agent(
    from_repository="market-research-agent",
    goal="Research the latest trends in AI development",  # Override the repository goal
    verbose=True  # Add a setting not in the repository
)
```

### Example: Creating a Crew with Repository Agents

```python  theme={null}
from crewai import Crew, Agent, Task

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Creating and Use Agent Repositories](./1420-creating-and-use-agent-repositories.md)

**Next:** [Load agents from repositories →](./1422-load-agents-from-repositories.md)
