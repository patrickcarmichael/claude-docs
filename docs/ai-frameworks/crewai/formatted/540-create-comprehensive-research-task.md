---
title: "Crewai: Create comprehensive research task"
description: "Create comprehensive research task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create comprehensive research task

research_task = Task(
    description="""Research the impact of AI agents on business productivity.
    Include current weather impacts on remote work, financial market trends,
    and recent academic publications on AI agent frameworks.""",
    expected_output="""Comprehensive report covering:
    1. AI agent business impact analysis
    2. Weather considerations for remote work
    3. Financial market trends related to AI
    4. Academic research citations and insights
    5. Competitive landscape analysis""",
    agent=multi_source_agent
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with multiple MCP sources](./539-create-agent-with-multiple-mcp-sources.md)

**Next:** [Create and execute crew →](./541-create-and-execute-crew.md)
