---
title: "Crewai: Define a task for the agent"
description: "Define a task for the agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define a task for the agent

extract_task = Task(
    description='Extract the main content from the URL https://example.com using basic extraction depth.',
    expected_output='A JSON string containing the extracted content from the URL.',
    agent=extractor_agent
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent that uses the tool](./1156-create-an-agent-that-uses-the-tool.md)

**Next:** [Create and run the crew →](./1158-create-and-run-the-crew.md)
