---
title: "Crewai: crewai_agent.py"
description: "crewai_agent.py section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# crewai_agent.py

from crewai import Agent, Task, Crew

from crewai_tools import (
    WebsiteSearchTool
)

web_rag_tool = WebsiteSearchTool()

writer = Agent(
    role="Writer",
    goal="You make math engaging and understandable for young children through poetry",
    backstory="You're an expert in writing haikus but you know nothing of math.",
    tools=[web_rag_tool],
)

task = Task(
    description=("What is {multiplication}?"),
    expected_output=("Compose a haiku that includes the answer."),
    agent=writer
)

crew = Crew(
    agents=[writer],
    tasks=[task],
    share_crew=False
)

output = crew.kickoff(dict(multiplication="2 * 2"))
```

### Run the Application with Datadog Auto-Instrumentation

With the [environment variables](#set-environment-variables) set, you can now run the application with Datadog auto-instrumentation.

```shell  theme={null}
ddtrace-run python crewai_agent.py
```

### View the Traces in Datadog

After running the application, you can view the traces in [Datadog LLM Observability's Traces View](https://app.datadoghq.com/llm/traces), selecting the ML Application name you chose from the top-left dropdown.

Clicking on a trace will show you the details of the trace, including total tokens used, number of LLM calls, models used, and estimated cost. Clicking into a specific span will narrow down these details, and show related input, output, and metadata.

<Frame>
  <img src="https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-1.png?fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=12b76bf2631c8b24ed6828053b125074" alt="Datadog LLM Observability Trace View" data-og-width="2678" width="2678" data-og-height="1572" height="1572" data-path="images/datadog-llm-observability-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-1.png?w=280&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=1862b54dec692db71de36087c425b3e6 280w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-1.png?w=560&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=a3d32811584412edba3c66c1024c28d2 560w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-1.png?w=840&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=fc6ed7c46b781e9c4a6f393150c99399 840w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-1.png?w=1100&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=2488ea5cbb8b2b852f03efa9f58de19c 1100w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-1.png?w=1650&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=9f541b37cbd11c65251eeaf2e91259aa 1650w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-1.png?w=2500&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=31fb1902fd6a4c3703167674644f4a8a 2500w" />
</Frame>

Additionally, you can view the execution graph view of the trace, which shows the control and data flow of the trace, which will scale with larger agents to show handoffs and relationships between LLM calls, tool calls, and agent interactions.

<Frame>
  <img src="https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-2.png?fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=01a94c3f9f162ce0b918fa6039f6fa8e" alt="Datadog LLM Observability Agent Execution Flow View" data-og-width="4774" width="4774" data-og-height="2566" height="2566" data-path="images/datadog-llm-observability-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-2.png?w=280&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=68d556845570e0aa0df070d1de7067ce 280w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-2.png?w=560&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=f5b67e3fb8beb9acd769042e188d04a6 560w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-2.png?w=840&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=3d045e43cc2846acaae17fd0d741ef90 840w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-2.png?w=1100&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=b1802677a2e3403247a3b789c65cf9b6 1100w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-2.png?w=1650&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=9bbcb20ebbad420307e1f4cdb836c1c8 1650w, https://mintcdn.com/crewai/YHPIyIjbLg-0Yd_V/images/datadog-llm-observability-2.png?w=2500&fit=max&auto=format&n=YHPIyIjbLg-0Yd_V&q=85&s=2d98c2f8224f78bfe8bc2a3ee99464f1 2500w" />
</Frame>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Getting Started](./2165-getting-started.md)

**Next:** [References →](./2167-references.md)
