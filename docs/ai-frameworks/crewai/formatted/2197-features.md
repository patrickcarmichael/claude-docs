---
title: "Crewai: Features"
description: "Features section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Features


### Prompt Management

Maxim's Prompt Management capabilities enable you to create, organize, and optimize prompts for your CrewAI agents. Rather than hardcoding instructions, leverage Maxim’s SDK to dynamically retrieve and apply version-controlled prompts.

<Tabs>
  <Tab title="Prompt Playground">
    Create, refine, experiment and deploy your prompts via the playground. Organize of your prompts using folders and versions, experimenting with the real world cases by linking tools and context, and deploying based on custom logic.

    Easily experiment across models by [**configuring models**](https://www.getmaxim.ai/docs/introduction/quickstart/setting-up-workspace#add-model-api-keys) and selecting the relevant model from the dropdown at the top of the prompt playground.

    <img src="https://raw.githubusercontent.com/akmadan/crewAI/docs_maxim_observability/docs/images/maxim_playground.png" />
  </Tab>

  <Tab title="Prompt Versions">
    As teams build their AI applications, a big part of experimentation is iterating on the prompt structure. In order to collaborate effectively and organize your changes clearly, Maxim allows prompt versioning and comparison runs across versions.

    <img src="https://raw.githubusercontent.com/akmadan/crewAI/docs_maxim_observability/docs/images/maxim_versions.png" />
  </Tab>

  <Tab title="Prompt Comparisons">
    Iterating on Prompts as you evolve your AI application would need experiments across models, prompt structures, etc. In order to compare versions and make informed decisions about changes, the comparison playground allows a side by side view of results.

    ## **Why use Prompt comparison?**

    Prompt comparison combines multiple single Prompts into one view, enabling a streamlined approach for various workflows:

    1. **Model comparison**: Evaluate the performance of different models on the same Prompt.
    2. **Prompt optimization**: Compare different versions of a Prompt to identify the most effective formulation.
    3. **Cross-Model consistency**: Ensure consistent outputs across various models for the same Prompt.
    4. **Performance benchmarking**: Analyze metrics like latency, cost, and token count across different models and Prompts.
  </Tab>
</Tabs>

### Observability & Evals

Maxim AI provides comprehensive observability & evaluation for your CrewAI agents, helping you understand exactly what's happening during each execution.

<Tabs>
  <Tab title="Agent Tracing">
    Track your agent’s complete lifecycle, including tool calls, agent trajectories, and decision flows effortlessly.

    <img src="https://raw.githubusercontent.com/akmadan/crewAI/docs_maxim_observability/docs/images/maxim_agent_tracking.png" />
  </Tab>

  <Tab title="Analytics + Evals">
    Run detailed evaluations on full traces or individual nodes with support for:

    * Multi-step interactions and granular trace analysis
    * Session Level Evaluations
    * Simulations for real-world testing

    <img src="https://raw.githubusercontent.com/akmadan/crewAI/docs_maxim_observability/docs/images/maxim_trace_eval.png" />

    <CardGroup cols={3}>
      <Card title="Auto Evals on Logs" icon="e" href="https://www.getmaxim.ai/docs/observe/how-to/evaluate-logs/auto-evaluation">
        <p>
          Evaluate captured logs automatically from the UI based on filters and sampling
        </p>
      </Card>

      <Card title="Human Evals on Logs" icon="hand" href="https://www.getmaxim.ai/docs/observe/how-to/evaluate-logs/human-evaluation">
        <p>
          Use human evaluation or rating to assess the quality of your logs and evaluate them.
        </p>
      </Card>

      <Card title="Node Level Evals" icon="road" href="https://www.getmaxim.ai/docs/observe/how-to/evaluate-logs/node-level-evaluation">
        <p>
          Evaluate any component of your trace or log to gain insights into your agent’s behavior.
        </p>
      </Card>
    </CardGroup>

    ***

  </Tab>

  <Tab title="Alerting">
    Set thresholds on **error**, **cost, token usage, user feedback, latency** and get real-time alerts via Slack or PagerDuty.

    <img src="https://raw.githubusercontent.com/akmadan/crewAI/docs_maxim_observability/docs/images/maxim_alerts_1.png" />
  </Tab>

  <Tab title="Dashboards">
    Visualize Traces over time, usage metrics, latency & error rates with ease.

    <img src="https://raw.githubusercontent.com/akmadan/crewAI/docs_maxim_observability/docs/images/maxim_dashboard_1.png" />
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Maxim Overview](./2196-maxim-overview.md)

**Next:** [Getting Started →](./2198-getting-started.md)
