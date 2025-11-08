---
title: "Crewai: Setup Instructions"
description: "Setup Instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setup Instructions


### Step 1: Create Your CrewAI AMP Account

Visit [app.crewai.com](https://app.crewai.com) and create your free account. This will give you access to the CrewAI AMP platform where you can view traces, metrics, and manage your crews.

### Step 2: Install CrewAI CLI and Authenticate

If you haven't already, install CrewAI with the CLI tools:

```bash  theme={null}
uv add crewai[tools]
```

Then authenticate your CLI with your CrewAI AMP account:

```bash  theme={null}
crewai login
```

This command will:

1. Open your browser to the authentication page
2. Prompt you to enter a device code
3. Authenticate your local environment with your CrewAI AMP account
4. Enable tracing capabilities for your local development

### Step 3: Enable Tracing in Your Crew

You can enable tracing for your Crew by setting the `tracing` parameter to `True`:

```python  theme={null}
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./2275-prerequisites.md)

**Next:** [Define your agents →](./2277-define-your-agents.md)
