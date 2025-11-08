---
title: "Crewai: Setup Instructions"
description: "Setup Instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setup Instructions


<Steps>
  <Step title="Sign up for Langtrace">
    Sign up by visiting [https://langtrace.ai/signup](https://langtrace.ai/signup).
  </Step>

  <Step title="Create a project">
    Set the project type to `CrewAI` and generate an API key.
  </Step>

  <Step title="Install Langtrace in your CrewAI project">
    Use the following command:

    ```bash  theme={null}
    pip install langtrace-python-sdk
    ```
  </Step>

  <Step title="Import Langtrace">
    Import and initialize Langtrace at the beginning of your script, before any CrewAI imports:

    ```python  theme={null}
    from langtrace_python_sdk import langtrace
    langtrace.init(api_key='<LANGTRACE_API_KEY>')

    # Now import CrewAI modules
    from crewai import Agent, Task, Crew
    ```
  </Step>
</Steps>

### Features and Their Application to CrewAI

1. **LLM Token and Cost Tracking**

   * Monitor the token usage and associated costs for each CrewAI agent interaction.

2. **Trace Graph for Execution Steps**

   * Visualize the execution flow of your CrewAI tasks, including latency and logs.
   * Useful for identifying bottlenecks in your agent workflows.

3. **Dataset Curation with Manual Annotation**

   * Create datasets from your CrewAI task outputs for future training or evaluation.

4. **Prompt Versioning and Management**

   * Keep track of different versions of prompts used in your CrewAI agents.
   * Useful for A/B testing and optimizing agent performance.

5. **Prompt Playground with Model Comparisons**

   * Test and compare different prompts and models for your CrewAI agents before deployment.

6. **Testing and Evaluations**

   * Set up automated tests for your CrewAI agents and tasks.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Langtrace Overview](./2193-langtrace-overview.md)

**Next:** [Maxim Integration →](./2195-maxim-integration.md)
