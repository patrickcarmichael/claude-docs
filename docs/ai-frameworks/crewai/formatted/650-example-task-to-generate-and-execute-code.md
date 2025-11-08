---
title: "Crewai: Example task to generate and execute code"
description: "Example task to generate and execute code section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to generate and execute code

coding_task = Task(
    description="Write a Python function to calculate the Fibonacci sequence up to the 10th number and print the result.",
    expected_output="The Fibonacci sequence up to the 10th number.",
    agent=programmer_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./649-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./651-create-and-run-the-crew.md)
