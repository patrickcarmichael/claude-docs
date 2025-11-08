---
title: "Crewai: Viewing Your Traces"
description: "Viewing Your Traces section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Viewing Your Traces


### Access the CrewAI AMP Dashboard

1. Visit [app.crewai.com](https://app.crewai.com) and log in to your account
2. Navigate to your project dashboard
3. Click on the **Traces** tab to view execution details

### What You'll See in Traces

CrewAI tracing provides comprehensive visibility into:

* **Agent Decisions**: See how agents reason through tasks and make decisions
* **Task Execution Timeline**: Visual representation of task sequences and dependencies
* **Tool Usage**: Monitor which tools are called and their results
* **LLM Calls**: Track all language model interactions, including prompts and responses
* **Performance Metrics**: Execution times, token usage, and costs
* **Error Tracking**: Detailed error information and stack traces

### Trace Features

* **Execution Timeline**: Click through different stages of execution
* **Detailed Logs**: Access comprehensive logs for debugging
* **Performance Analytics**: Analyze execution patterns and optimize performance
* **Export Capabilities**: Download traces for further analysis

### Authentication Issues

If you encounter authentication problems:

1. Ensure you're logged in: `crewai login`
2. Check your internet connection
3. Verify your account at [app.crewai.com](https://app.crewai.com)

### Traces Not Appearing

If traces aren't showing up in the dashboard:

1. Confirm `tracing=True` is set in your Crew/Flow
2. Check that `CREWAI_TRACING_ENABLED=true` if using environment variables
3. Ensure you're authenticated with `crewai login`
4. Verify your crew/flow is actually executing

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run the flow with tracing enabled](./2281-create-and-run-the-flow-with-tracing-enabled.md)

**Next:** [TrueFoundry Integration →](./2283-truefoundry-integration.md)
