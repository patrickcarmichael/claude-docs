---
title: "Crewai: Code Execution Process"
description: "Code Execution Process section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Code Execution Process


When an agent with code execution enabled encounters a task requiring programming:

<Steps>
  <Step title="Task Analysis">
    The agent analyzes the task and determines that code execution is necessary.
  </Step>

  <Step title="Code Formulation">
    It formulates the Python code needed to solve the problem.
  </Step>

  <Step title="Code Execution">
    The code is sent to the internal code execution tool (`CodeInterpreterTool`).
  </Step>

  <Step title="Result Interpretation">
    The agent interprets the result and incorporates it into its response or uses it for further problem-solving.
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Important Considerations](./1973-important-considerations.md)

**Next:** [Example Usage →](./1975-example-usage.md)
