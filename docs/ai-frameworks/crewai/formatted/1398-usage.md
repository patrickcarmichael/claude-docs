---
title: "Crewai: Usage"
description: "Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage


### Basic Implementation

The StagehandTool can be implemented in two ways:

#### 1. Using Context Manager (Recommended)

<Tip>
  The context manager approach is recommended as it ensures proper cleanup of resources even if exceptions occur.
</Tip>

```python  theme={null}
from crewai import Agent, Task, Crew
from crewai_tools import StagehandTool
from stagehand.schemas import AvailableModel

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./1397-prerequisites.md)

**Next:** [Initialize the tool with your API keys using a context manager →](./1399-initialize-the-tool-with-your-api-keys-using-a-con.md)
