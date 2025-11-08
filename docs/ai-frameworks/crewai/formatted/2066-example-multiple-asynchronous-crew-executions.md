---
title: "Crewai: Example: Multiple Asynchronous Crew Executions"
description: "Example: Multiple Asynchronous Crew Executions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example: Multiple Asynchronous Crew Executions


In this example, we'll show how to kickoff multiple crews asynchronously and wait for all of them to complete using `asyncio.gather()`:

```python Code theme={null}
import asyncio
from crewai import Crew, Agent, Task

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the async function](./2065-run-the-async-function.md)

**Next:** [Create an agent with code execution enabled →](./2067-create-an-agent-with-code-execution-enabled.md)
