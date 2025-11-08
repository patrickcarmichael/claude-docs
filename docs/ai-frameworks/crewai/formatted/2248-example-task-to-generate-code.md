---
title: "Crewai: Example task to generate code"
description: "Example task to generate code section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example task to generate code

generate_code_task = Task(
    description="Create a simple program to generate the first N numbers in the Fibonacci sequence.",
    expected_output="Program that generates the first N numbers in the Fibonacci sequence.",
    agent=coding_agent,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define an agent that uses the tool](./2247-define-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./2249-create-and-run-the-crew.md)
