---
title: "Crewai: Maxim API Configuration"
description: "Maxim API Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Maxim API Configuration

MAXIM_API_KEY=your_api_key_here
MAXIM_LOG_REPO_ID=your_repo_id_here
```

### 2. Import the required packages

```python  theme={null}
from crewai import Agent, Task, Crew, Process
from maxim import Maxim
from maxim.logger.crewai import instrument_crewai
```

### 3. Initialise Maxim with your API key

```python {8} theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create a `.env` file in your project root:](./2199-create-a-env-file-in-your-project-root.md)

**Next:** [Instrument CrewAI with just one line →](./2201-instrument-crewai-with-just-one-line.md)
