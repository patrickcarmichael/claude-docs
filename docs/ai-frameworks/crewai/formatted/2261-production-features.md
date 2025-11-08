---
title: "Crewai: Production Features"
description: "Production Features section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Production Features


### 1. Enhanced Observability

Portkey provides comprehensive observability for your CrewAI agents, helping you understand exactly what's happening during each execution.

<Tabs>
  <Tab title="Traces">
    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/CrewAI%20Product%2011.1.webp" />
    </Frame>

    Traces provide a hierarchical view of your crew's execution, showing the sequence of LLM calls, tool invocations, and state transitions.

    ```python  theme={null}
    # Add trace_id to enable hierarchical tracing in Portkey
    portkey_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="dummy",
        extra_headers=createHeaders(
            api_key="YOUR_PORTKEY_API_KEY",
            virtual_key="YOUR_OPENAI_VIRTUAL_KEY",
            trace_id="unique-session-id"  # Add unique trace ID
        )
    )
    ```
  </Tab>

  <Tab title="Logs">
    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/CrewAI%20Portkey%20Docs%20Metadata.png" />
    </Frame>

    Portkey logs every interaction with LLMs, including:

    * Complete request and response payloads
    * Latency and token usage metrics
    * Cost calculations
    * Tool calls and function executions

    All logs can be filtered by metadata, trace IDs, models, and more, making it easy to debug specific crew runs.
  </Tab>

  <Tab title="Metrics & Dashboards">
    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/CrewAI%20Dashboard.png" />
    </Frame>

    Portkey provides built-in dashboards that help you:

    * Track cost and token usage across all crew runs
    * Analyze performance metrics like latency and success rates
    * Identify bottlenecks in your agent workflows
    * Compare different crew configurations and LLMs

    You can filter and segment all metrics by custom metadata to analyze specific crew types, user groups, or use cases.
  </Tab>

  <Tab title="Metadata Filtering">
    <Frame>
      <img src="https://raw.githubusercontent.com/siddharthsambharia-portkey/Portkey-Product-Images/refs/heads/main/Metadata%20Filters%20from%20CrewAI.png" alt="Analytics with metadata filters" />
    </Frame>

    Add custom metadata to your CrewAI LLM configuration to enable powerful filtering and segmentation:

    ```python  theme={null}
    portkey_llm = LLM(
        model="gpt-4o",
        base_url=PORTKEY_GATEWAY_URL,
        api_key="dummy",
        extra_headers=createHeaders(
            api_key="YOUR_PORTKEY_API_KEY",
            virtual_key="YOUR_OPENAI_VIRTUAL_KEY",
            metadata={
                "crew_type": "research_crew",
                "environment": "production",
                "_user": "user_123",   # Special _user field for user analytics
                "request_source": "mobile_app"
            }
        )
    )
    ```

    This metadata can be used to filter logs, traces, and metrics on the Portkey dashboard, allowing you to analyze specific crew runs, users, or environments.
  </Tab>
</Tabs>

### 2. Reliability - Keep Your Crews Running Smoothly

When running crews in production, things can go wrong - API rate limits, network issues, or provider outages. Portkey's reliability features ensure your agents keep running smoothly even when problems occur.

It's simple to enable fallback in your CrewAI setup by using a Portkey Config:

```python  theme={null}
from crewai import LLM
from portkey_ai import createHeaders, PORTKEY_GATEWAY_URL

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Introduction](./2260-introduction.md)

**Next:** [Create LLM with fallback configuration →](./2262-create-llm-with-fallback-configuration.md)
