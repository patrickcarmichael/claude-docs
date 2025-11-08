# Traces

**Navigation:** [← Previous](./06-website-rag-search.md) | [Index](./index.md) | [Next →](./08-create-an-agent-with-asana-capabilities.md)

---

# Traces
Source: https://docs.crewai.com/en/enterprise/features/traces

Using Traces to monitor your Crews


## Overview

Traces provide comprehensive visibility into your crew executions, helping you monitor performance, debug issues, and optimize your AI agent workflows.


## What are Traces?

Traces in CrewAI AMP are detailed execution records that capture every aspect of your crew's operation, from initial inputs to final outputs. They record:

* Agent thoughts and reasoning
* Task execution details
* Tool usage and outputs
* Token consumption metrics
* Execution times
* Cost estimates

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9c02d5b7306bf7adaeadd77a018f8fea" alt="Traces Overview" data-og-width="2244" width="2244" data-og-height="1422" height="1422" data-path="images/enterprise/traces-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e66e7c56a8848b69266563ea8cddfc4e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f590b3901aaa5994042c79426d78bd6c 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0ecb9dcb307e8f130f53393bd3abc12d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fc6fcfc51c4e8f4ce16d237228043d6 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=253eaed4ec34a35798dad42e9a388859 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/traces-overview.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ec818e09bc20b3f72b1bcf1970804d13 2500w" />
</Frame>


## Accessing Traces

<Steps>
  <Step title="Navigate to the Traces Tab">
    Once in your CrewAI AMP dashboard, click on the **Traces** to view all execution records.
  </Step>

  <Step title="Select an Execution">
    You'll see a list of all crew executions, sorted by date. Click on any execution to view its detailed trace.
  </Step>
</Steps>


## Understanding the Trace Interface

The trace interface is divided into several sections, each providing different insights into your crew's execution:

### 1. Execution Summary

The top section displays high-level metrics about the execution:

* **Total Tokens**: Number of tokens consumed across all tasks
* **Prompt Tokens**: Tokens used in prompts to the LLM
* **Completion Tokens**: Tokens generated in LLM responses
* **Requests**: Number of API calls made
* **Execution Time**: Total duration of the crew run
* **Estimated Cost**: Approximate cost based on token usage

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6a26eda2add26a6f649b1727bf90d8d" alt="Execution Summary" data-og-width="2576" width="2576" data-og-height="916" height="916" data-path="images/enterprise/trace-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=52f47a0c5d9f2dc1d0c93d1c2446cb10 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=584cdc9fded1e3875799da73e60cdebd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2e4f500438545badfa9b3bb3704786ce 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c3e0987a95638f9512ba6c64a5927eda 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d80e2d9de9db7449368151ccaac8106b 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-summary.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=39ccb1a6b12aecd0f6863f2783b1bfc6 2500w" />
</Frame>

### 2. Tasks & Agents

This section shows all tasks and agents that were part of the crew execution:

* Task name and agent assignment
* Agents and LLMs used for each task
* Status (completed/failed)
* Individual execution time of the task

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f0358b4a17e78532500b4a14964bc30c" alt="Task List" data-og-width="1778" width="1778" data-og-height="594" height="594" data-path="images/enterprise/trace-tasks.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a775268b18c71e0ffa497c9a4e1ad179 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3dadaad60870c3841f859857d5d6f53d 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a0a1d24573dd32cb9d5a3f089536c547 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2ccc370f5e0b6b38521a5ed39e02b062 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4d717a70fd61ce713f7d5d91ccf867fe 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-tasks.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2c577a5f8e1acea3942de29c5ca49343 2500w" />
</Frame>

### 3. Final Output

Displays the final result produced by the crew after all tasks are completed.

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5ca9ef8e4071ee570c3e0c8f93ff4253" alt="Final Output" data-og-width="2212" width="2212" data-og-height="1572" height="1572" data-path="images/enterprise/final-output.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ab97b6b386304f03fe21c6ba2393c683 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3839e312b2a9caa45f3f4b72345ea87b 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b032c2c57ffcd5fb558c43915d385f9a 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=63390d70d70f1a2265a224e8c20d0204 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=abc4a7b81c51049ca606130a0dd543f7 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/final-output.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9fc40fc5f8ad52996aba482d62348f0f 2500w" />
</Frame>

### 4. Execution Timeline

A visual representation of when each task started and ended, helping you identify bottlenecks or parallel execution patterns.

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c860975d3e15e3a6988bedc7d1bf6ba4" alt="Execution Timeline" data-og-width="2210" width="2210" data-og-height="1406" height="1406" data-path="images/enterprise/trace-timeline.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b74d67bda34ce88ea23c30c580dfb2fc 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=99c6688c1d290548cc480232bb13b0e0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4876c794ddde894e1e2cf15f1926efcb 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c44f7eec8f0998e488bc951eee8961ea 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c25e4827f5a83172483c38f40e6685de 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-timeline.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b3b2f72954e565f7177b5175d89dfe79 2500w" />
</Frame>

### 5. Detailed Task View

When you click on a specific task in the timeline or task list, you'll see:

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=74f5e92354196325edca8d62c29363c7" alt="Detailed Task View" data-og-width="2036" width="2036" data-og-height="1572" height="1572" data-path="images/enterprise/trace-detailed-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d260407501639bcd1a45da51762f488e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e577e06eb7658f045e56f2e40e03cf94 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fcafbac3507eb800e08153352016bf14 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9b2b0decb758802aaa2d8b0b2bd39e6f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=66a9362f6d8f2edd5a2dad353700e440 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trace-detailed-task.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=faadd7f3c9e9176060e21c2987c3d8c9 2500w" />
</Frame>

* **Task Key**: Unique identifier for the task
* **Task ID**: Technical identifier in the system
* **Status**: Current state (completed/running/failed)
* **Agent**: Which agent performed the task
* **LLM**: Language model used for this task
* **Start/End Time**: When the task began and completed
* **Execution Time**: Duration of this specific task
* **Task Description**: What the agent was instructed to do
* **Expected Output**: What output format was requested
* **Input**: Any input provided to this task from previous tasks
* **Output**: The actual result produced by the agent


## Using Traces for Debugging

Traces are invaluable for troubleshooting issues with your crews:

<Steps>
  <Step title="Identify Failure Points">
    When a crew execution doesn't produce the expected results, examine the trace to find where things went wrong. Look for:

    * Failed tasks
    * Unexpected agent decisions
    * Tool usage errors
    * Misinterpreted instructions

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c892a75b7a22a57949a2641a0fe45bfa" alt="Failure Points" data-og-width="820" width="820" data-og-height="924" height="924" data-path="images/enterprise/failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ecbcbd312dd467cb5cc1dae4a443c56d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c0452a9db1f339e63686941a533d8946 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ded3f2fff055c8d16bcad99ad537da46 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f871feb85f88ba397a259ee8392aef3e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2acf042b2e6b185f1fbc41100751e03f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/failure.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1e9fc9104e6b55b586a9b13e120de908 2500w" />
    </Frame>
  </Step>

  <Step title="Optimize Performance">
    Use execution metrics to identify performance bottlenecks:

    * Tasks that took longer than expected
    * Excessive token usage
    * Redundant tool operations
    * Unnecessary API calls
  </Step>

  <Step title="Improve Cost Efficiency">
    Analyze token usage and cost estimates to optimize your crew's efficiency:

    * Consider using smaller models for simpler tasks
    * Refine prompts to be more concise
    * Cache frequently accessed information
    * Structure tasks to minimize redundant operations
  </Step>
</Steps>


## Performance and batching

CrewAI batches trace uploads to reduce overhead on high-volume runs:

* A TraceBatchManager buffers events and sends them in batches via the Plus API client
* Reduces network chatter and improves reliability on flaky connections
* Automatically enabled in the default trace listener; no configuration needed

This yields more stable tracing under load while preserving detailed task/agent telemetry.

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with trace analysis or any other CrewAI AMP features.
</Card>



# Webhook Streaming
Source: https://docs.crewai.com/en/enterprise/features/webhook-streaming

Using Webhook Streaming to stream events to your webhook


## Overview

Enterprise Event Streaming lets you receive real-time webhook updates about your crews and flows deployed to
CrewAI AMP, such as model calls, tool usage, and flow steps.


## Usage

When using the Kickoff API, include a `webhooks` object to your request, for example:

```json  theme={null}
{
  "inputs": {"foo": "bar"},
  "webhooks": {
    "events": ["crew_kickoff_started", "llm_call_started"],
    "url": "https://your.endpoint/webhook",
    "realtime": false,
    "authentication": {
      "strategy": "bearer",
      "token": "my-secret-token"
    }
  }
}
```

If `realtime` is set to `true`, each event is delivered individually and immediately, at the cost of crew/flow performance.


## Webhook Format

Each webhook sends a list of events:

```json  theme={null}
{
  "events": [
    {
      "id": "event-id",
      "execution_id": "crew-run-id",
      "timestamp": "2025-02-16T10:58:44.965Z",
      "type": "llm_call_started",
      "data": {
        "model": "gpt-4",
        "messages": [
          {"role": "system", "content": "You are an assistant."},
          {"role": "user", "content": "Summarize this article."}
        ]
      }
    }
  ]
}
```

The `data` object structure varies by event type. Refer to the [event list](https://github.com/crewAIInc/crewAI/tree/main/src/crewai/utilities/events) on GitHub.

As requests are sent over HTTP, the order of events can't be guaranteed. If you need ordering, use the `timestamp` field.


## Supported Events

CrewAI supports both system events and custom events in Enterprise Event Streaming. These events are sent to your configured webhook endpoint during crew and flow execution.

### Flow Events:

* `flow_created`
* `flow_started`
* `flow_finished`
* `flow_plot`
* `method_execution_started`
* `method_execution_finished`
* `method_execution_failed`

### Agent Events:

* `agent_execution_started`
* `agent_execution_completed`
* `agent_execution_error`
* `lite_agent_execution_started`
* `lite_agent_execution_completed`
* `lite_agent_execution_error`
* `agent_logs_started`
* `agent_logs_execution`
* `agent_evaluation_started`
* `agent_evaluation_completed`
* `agent_evaluation_failed`

### Crew Events:

* `crew_kickoff_started`
* `crew_kickoff_completed`
* `crew_kickoff_failed`
* `crew_train_started`
* `crew_train_completed`
* `crew_train_failed`
* `crew_test_started`
* `crew_test_completed`
* `crew_test_failed`
* `crew_test_result`

### Task Events:

* `task_started`
* `task_completed`
* `task_failed`
* `task_evaluation`

### Tool Usage Events:

* `tool_usage_started`
* `tool_usage_finished`
* `tool_usage_error`
* `tool_validate_input_error`
* `tool_selection_error`
* `tool_execution_error`

### LLM Events:

* `llm_call_started`
* `llm_call_completed`
* `llm_call_failed`
* `llm_stream_chunk`

### LLM Guardrail Events:

* `llm_guardrail_started`
* `llm_guardrail_completed`

### Memory Events:

* `memory_query_started`
* `memory_query_completed`
* `memory_query_failed`
* `memory_save_started`
* `memory_save_completed`
* `memory_save_failed`
* `memory_retrieval_started`
* `memory_retrieval_completed`

### Knowledge Events:

* `knowledge_search_query_started`
* `knowledge_search_query_completed`
* `knowledge_search_query_failed`
* `knowledge_query_started`
* `knowledge_query_completed`
* `knowledge_query_failed`

### Reasoning Events:

* `agent_reasoning_started`
* `agent_reasoning_completed`
* `agent_reasoning_failed`

Event names match the internal event bus. See GitHub for the full list of events.

You can emit your own custom events, and they will be delivered through the webhook stream alongside system events.

<CardGroup>
  <Card title="GitHub" icon="github" href="https://github.com/crewAIInc/crewAI/tree/main/src/crewai/utilities/events">
    Full list of events
  </Card>

  <Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
    Contact our support team for assistance with webhook integration or troubleshooting.
  </Card>
</CardGroup>



# Triggers Overview
Source: https://docs.crewai.com/en/enterprise/guides/automation-triggers

Understand how CrewAI AMP triggers work, how to manage them, and where to find integration-specific playbooks

CrewAI AMP triggers connect your automations to real-time events across the tools your teams already use. Instead of polling systems or relying on manual kickoffs, triggers listen for changes—new emails, calendar updates, CRM status changes—and immediately launch the crew or flow you specify.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c31a4b9031f0f517fdce3baa48471f58" alt="Automation Triggers Overview" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/enterprise/crew_connectors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9e592d155e388bb67d003b26884dc081 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=0c8aa20b2dc82de9ea3d2da6920e4195 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=782fe13ea53120f6d2f8e643a7a7b838 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=780cd735280c569e6e93caa8262b12d1 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=08bfe86a58ca08ec36ae67dca4aa5cf9 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e2bbe3b0fe0234001e030b501fa4d76c 2500w" />
</Frame>

### Integration Playbooks

Deep-dive guides walk through setup and sample workflows for each integration:

<CardGroup cols={2}>
  <Card title="Gmail Trigger" icon="envelope">
    <a href="/en/enterprise/guides/gmail-trigger">Enable crews when emails arrive or threads update.</a>
  </Card>

  <Card title="Google Calendar Trigger" icon="calendar-days">
    <a href="/en/enterprise/guides/google-calendar-trigger">React to calendar events as they are created, updated, or cancelled.</a>
  </Card>

  <Card title="Google Drive Trigger" icon="folder-open">
    <a href="/en/enterprise/guides/google-drive-trigger">Handle Drive file uploads, edits, and deletions.</a>
  </Card>

  <Card title="Outlook Trigger" icon="envelope-open">
    <a href="/en/enterprise/guides/outlook-trigger">Automate responses to new Outlook messages and calendar updates.</a>
  </Card>

  <Card title="OneDrive Trigger" icon="cloud">
    <a href="/en/enterprise/guides/onedrive-trigger">Audit file activity and sharing changes in OneDrive.</a>
  </Card>

  <Card title="Microsoft Teams Trigger" icon="comments">
    <a href="/en/enterprise/guides/microsoft-teams-trigger">Kick off workflows when new Teams chats start.</a>
  </Card>

  <Card title="HubSpot Trigger" icon="hubspot">
    <a href="/en/enterprise/guides/hubspot-trigger">Launch automations from HubSpot workflows and lifecycle events.</a>
  </Card>

  <Card title="Salesforce Trigger" icon="salesforce">
    <a href="/en/enterprise/guides/salesforce-trigger">Connect Salesforce processes to CrewAI for CRM automation.</a>
  </Card>

  <Card title="Slack Trigger" icon="slack">
    <a href="/en/enterprise/guides/slack-trigger">Start crews directly from Slack slash commands.</a>
  </Card>

  <Card title="Zapier Trigger" icon="bolt">
    <a href="/en/enterprise/guides/zapier-trigger">Bridge CrewAI with thousands of Zapier-supported apps.</a>
  </Card>
</CardGroup>


## Trigger Capabilities

With triggers, you can:

* **Respond to real-time events** - Automatically execute workflows when specific conditions are met
* **Integrate with external systems** - Connect with platforms like Gmail, Outlook, OneDrive, JIRA, Slack, Stripe and more
* **Scale your automation** - Handle high-volume events without manual intervention
* **Maintain context** - Access trigger data within your crews and flows


## Managing Triggers

### Viewing Available Triggers

To access and manage your automation triggers:

1. Navigate to your deployment in the CrewAI dashboard
2. Click on the **Triggers** tab to view all available trigger integrations

<Frame caption="Example of available automation triggers for a Gmail deployment">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5de0e753bcb9db2e7f2e126354741de8" alt="List of available automation triggers" data-og-width="2012" width="2012" data-og-height="862" height="862" data-path="images/enterprise/list-available-triggers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0b860cce01d60455055d5de942eaf93d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10d7cb945ddb53606092a0206e415e2e 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f522f52cf2749038b5654ece72450589 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f5d89c0da9816cf78e15004f0c82018f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bc4ed659f02b96f8312170a00a7ee7f0 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18ed2c13e60731bfb784abd2f403ef01 2500w" />
</Frame>

This view shows all the trigger integrations available for your deployment, along with their current connection status.

### Enabling and Disabling Triggers

Each trigger can be easily enabled or disabled using the toggle switch:

<Frame caption="Enable or disable triggers with toggle">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10b3ee6296f323168473593b64a1e4c8" alt="Enable or disable triggers with toggle" data-og-width="1984" width="1984" data-og-height="866" height="866" data-path="images/enterprise/trigger-selected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27137c8d8c072ece3319e9f4c8ee0185 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=842109fa147a6a91b9f9480e450a8ee0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5f2cbab1be7662c99854f88496f42b4b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fa4240b233d980059d3db96c493fda4 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37f3001a39aab6400b8df45fad9b5cfa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b2959938cb0f239a6113c9a8b7aa0356 2500w" />
</Frame>

* **Enabled (blue toggle)**: The trigger is active and will automatically execute your deployment when the specified events occur
* **Disabled (gray toggle)**: The trigger is inactive and will not respond to events

Simply click the toggle to change the trigger state. Changes take effect immediately.

### Monitoring Trigger Executions

Track the performance and history of your triggered executions:

<Frame caption="List of executions triggered by automation">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>


## Building Trigger-Driven Automations

Before building your automation, it's helpful to understand the structure of trigger payloads that your crews and flows will receive.

### Trigger Setup Checklist

Before wiring a trigger into production, make sure you:

* Connect the integration under **Tools & Integrations** and complete any OAuth or API key steps
* Enable the trigger toggle on the deployment that should respond to events
* Provide any required environment variables (API tokens, tenant IDs, shared secrets)
* Create or update tasks that can parse the incoming payload within the first crew task or flow step
* Decide whether to pass trigger context automatically using `allow_crewai_trigger_context`
* Set up monitoring—webhook logs, CrewAI execution history, and optional external alerting

### Testing Triggers Locally with CLI

The CrewAI CLI provides powerful commands to help you develop and test trigger-driven automations without deploying to production.

#### List Available Triggers

View all available triggers for your connected integrations:

```bash  theme={null}
crewai triggers list
```

This command displays all triggers available based on your connected integrations, showing:

* Integration name and connection status
* Available trigger types
* Trigger names and descriptions

#### Simulate Trigger Execution

Test your crew with realistic trigger payloads before deployment:

```bash  theme={null}
crewai triggers run <trigger_name>
```

For example:

```bash  theme={null}
crewai triggers run microsoft_onedrive/file_changed
```

This command:

* Executes your crew locally
* Passes a complete, realistic trigger payload
* Simulates exactly how your crew will be called in production

<Warning>
  **Important Development Notes:**

  * Use `crewai triggers run <trigger>` to simulate trigger execution during development
  * Using `crewai run` will NOT simulate trigger calls and won't pass the trigger payload
  * After deployment, your crew will be executed with the actual trigger payload
  * If your crew expects parameters that aren't in the trigger payload, execution may fail
</Warning>

### Triggers with Crew

Your existing crew definitions work seamlessly with triggers, you just need to have a task to parse the received payload:

```python  theme={null}
@CrewBase
class MyAutomatedCrew:
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
        )

    @task
    def parse_trigger_payload(self) -> Task:
        return Task(
            config=self.tasks_config['parse_trigger_payload'],
            agent=self.researcher(),
        )

    @task
    def analyze_trigger_content(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_trigger_data'],
            agent=self.researcher(),
        )
```

The crew will automatically receive and can access the trigger payload through the standard CrewAI context mechanisms.

<Note>
  Crew and Flow inputs can include `crewai_trigger_payload`. CrewAI automatically injects this payload:

  * Tasks: appended to the first task's description by default ("Trigger Payload: {crewai_trigger_payload}")
  * Control via `allow_crewai_trigger_context`: set `True` to always inject, `False` to never inject
  * Flows: any `@start()` method that accepts a `crewai_trigger_payload` parameter will receive it
</Note>

### Integration with Flows

For flows, you have more control over how trigger data is handled:

#### Accessing Trigger Payload

All `@start()` methods in your flows will accept an additional parameter called `crewai_trigger_payload`:

```python  theme={null}
from crewai.flow import Flow, start, listen

class MyAutomatedFlow(Flow):
    @start()
    def handle_trigger(self, crewai_trigger_payload: dict = None):
        """
        This start method can receive trigger data
        """
        if crewai_trigger_payload:
            # Process the trigger data
            trigger_id = crewai_trigger_payload.get('id')
            event_data = crewai_trigger_payload.get('payload', {})

            # Store in flow state for use by other methods
            self.state.trigger_id = trigger_id
            self.state.trigger_type = event_data

            return event_data

        # Handle manual execution
        return None

    @listen(handle_trigger)
    def process_data(self, trigger_data):
        """
        Process the data from the trigger
        """
        # ... process the trigger
```

#### Triggering Crews from Flows

When kicking off a crew within a flow that was triggered, pass the trigger payload as it:

```python  theme={null}
@start()
def delegate_to_crew(self, crewai_trigger_payload: dict = None):
    """
    Delegate processing to a specialized crew
    """
    crew = MySpecializedCrew()

    # Pass the trigger payload to the crew
    result = crew.crew().kickoff(
        inputs={
            'a_custom_parameter': "custom_value",
            'crewai_trigger_payload': crewai_trigger_payload
        },
    )

    return result
```


## Troubleshooting

**Trigger not firing:**

* Verify the trigger is enabled in your deployment's Triggers tab
* Check integration connection status under Tools & Integrations
* Ensure all required environment variables are properly configured

**Execution failures:**

* Check the execution logs for error details
* Use `crewai triggers run <trigger_name>` to test locally and see the exact payload structure
* Verify your crew can handle the `crewai_trigger_payload` parameter
* Ensure your crew doesn't expect parameters that aren't included in the trigger payload

**Development issues:**

* Always test with `crewai triggers run <trigger>` before deploying to see the complete payload
* Remember that `crewai run` does NOT simulate trigger calls—use `crewai triggers run` instead
* Use `crewai triggers list` to verify which triggers are available for your connected integrations
* After deployment, your crew will receive the actual trigger payload, so test thoroughly locally first

Automation triggers transform your CrewAI deployments into responsive, event-driven systems that can seamlessly integrate with your existing business processes and tools.



# Azure OpenAI Setup
Source: https://docs.crewai.com/en/enterprise/guides/azure-openai-setup

Configure Azure OpenAI with Crew Studio for enterprise LLM connections

This guide walks you through connecting Azure OpenAI with Crew Studio for seamless enterprise AI operations.


## Setup Process

<Steps>
  <Step title="Access Azure AI Foundry">
    1. In Azure, go to [Azure AI Foundry](https://ai.azure.com/) > select your Azure OpenAI deployment.
    2. On the left menu, click `Deployments`. If you don't have one, create a deployment with your desired model.
    3. Once created, select your deployment and locate the `Target URI` and `Key` on the right side of the page. Keep this page open, as you'll need this information.
       <Frame>
         <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a7136eae05529c674ddbda6e8f58eee8" alt="Azure AI Foundry" data-og-width="670" width="670" data-og-height="502" height="502" data-path="images/enterprise/azure-openai-studio.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=79abbdeb76fa4f38ef6614438651744c 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c60da2c7f702a15162111d45996d97ff 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=46d5ab75f601b9a14c53c93e51aa57b4 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=67e2c20ec9785d24bf69279102f564a7 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=342a5e6abe1f0a4b1dadf7865ac4cf27 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/azure-openai-studio.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=44d5e6cf8120262a1637a4e24858dfcb 2500w" />
       </Frame>
  </Step>

  <Step title="Configure CrewAI AMP Connection">
    4. In another tab, open `CrewAI AMP > LLM Connections`. Name your LLM Connection, select Azure as the provider, and choose the same model you selected in Azure.
    5. On the same page, add environment variables from step 3:
       * One named `AZURE_DEPLOYMENT_TARGET_URL` (using the Target URI). The URL should look like this: [https://your-deployment.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview](https://your-deployment.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview)
       * Another named `AZURE_API_KEY` (using the Key).
    6. Click `Add Connection` to save your LLM Connection.
  </Step>

  <Step title="Set Default Configuration">
    7. In `CrewAI AMP > Settings > Defaults > Crew Studio LLM Settings`, set the new LLM Connection and model as defaults.
  </Step>

  <Step title="Configure Network Access">
    8. Ensure network access settings:
       * In Azure, go to `Azure OpenAI > select your deployment`.
       * Navigate to `Resource Management > Networking`.
       * Ensure that `Allow access from all networks` is enabled. If this setting is restricted, CrewAI may be blocked from accessing your Azure OpenAI endpoint.
  </Step>
</Steps>


## Verification

You're all set! Crew Studio will now use your Azure OpenAI connection. Test the connection by creating a simple crew or task to ensure everything is working properly.


## Troubleshooting

If you encounter issues:

* Verify the Target URI format matches the expected pattern
* Check that the API key is correct and has proper permissions
* Ensure network access is configured to allow CrewAI connections
* Confirm the deployment model matches what you've configured in CrewAI



# Build Crew
Source: https://docs.crewai.com/en/enterprise/guides/build-crew

A Crew is a group of agents that work together to complete a task.


## Overview

[CrewAI AMP](https://app.crewai.com) streamlines the process of **creating**, **deploying**, and **managing** your AI agents in production environments.


## Getting Started

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/-kSOTtYzgEw" title="Building crews with the CrewAI CLI" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### Installation and Setup

<Card title="Follow Standard Installation" icon="wrench" href="/en/installation">
  Follow our standard installation guide to set up CrewAI CLI and create your first project.
</Card>

### Building Your Crew

<Card title="Quickstart Tutorial" icon="rocket" href="/en/quickstart">
  Follow our quickstart guide to create your first agent crew using YAML configuration.
</Card>


## Support and Resources

For Enterprise-specific support or questions, contact our dedicated support team at [support@crewai.com](mailto:support@crewai.com).

<Card title="Schedule a Demo" icon="calendar" href="mailto:support@crewai.com">
  Book time with our team to learn more about Enterprise features and how they can benefit your organization.
</Card>



# Open Telemetry Logs
Source: https://docs.crewai.com/en/enterprise/guides/capture_telemetry_logs

Understand how to capture telemetry logs from your CrewAI AMP deployments

CrewAI AMP provides a powerful way to capture telemetry logs from your deployments. This allows you to monitor the performance of your agents and workflows, and to debug issues that may arise.


## Prerequisites

<CardGroup cols={2}>
  <Card title="ENTERPRISE OTEL SETUP enabled" icon="users">
    Your organization should have ENTERPRISE OTEL SETUP enabled
  </Card>

  <Card title="OTEL collector setup" icon="server">
    Your organization should have an OTEL collector setup or a provider like Datadog log intake setup
  </Card>
</CardGroup>


## How to capture telemetry logs

1. Go to settings/organization tab
2. Configure your OTEL collector setup
3. Save

Example to setup OTEL log collection capture to Datadog.

<Frame>
    <img src="https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=5bb359765661a61f7012824fe35b0978" alt="Capture Telemetry Logs" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/crewai-otel-export.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=280&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=2bee9ddb6077fca900cc42e98c1c1c77 280w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=560&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=ceae34948ba9b7daeff1a277d78f8991 560w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=840&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=3e86994eb05fe4c9005a8a62f272b618 840w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=1100&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=3b498ed5c28cb90d415721f636e16ac3 1100w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=1650&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=35463fcfaa322eacbb1e862ce638a093 1650w, https://mintcdn.com/crewai/oe9EA0HJn5xQ9z71/images/crewai-otel-export.png?w=2500&fit=max&auto=format&n=oe9EA0HJn5xQ9z71&q=85&s=fa9f64fe474823fedc93cfdf66d36b4b 2500w" />
</Frame>



# Deploy Crew
Source: https://docs.crewai.com/en/enterprise/guides/deploy-crew

Deploying a Crew on CrewAI AMP

<Note>
  After creating a crew locally or through Crew Studio, the next step is deploying it to the CrewAI AMP platform. This guide covers multiple deployment methods to help you choose the best approach for your workflow.
</Note>


## Prerequisites

<CardGroup cols={2}>
  <Card title="Crew Ready for Deployment" icon="users">
    You should have a working crew either built locally or created through Crew Studio
  </Card>

  <Card title="GitHub Repository" icon="github">
    Your crew code should be in a GitHub repository (for GitHub integration method)
  </Card>
</CardGroup>


## Option 1: Deploy Using CrewAI CLI

The CLI provides the fastest way to deploy locally developed crews to the Enterprise platform.

<Steps>
  <Step title="Install CrewAI CLI">
    If you haven't already, install the CrewAI CLI:

    ```bash  theme={null}
    pip install crewai[tools]
    ```

    <Tip>
      The CLI comes with the main CrewAI package, but the `[tools]` extra ensures you have all deployment dependencies.
    </Tip>
  </Step>

  <Step title="Authenticate with the Enterprise Platform">
    First, you need to authenticate your CLI with the CrewAI AMP platform:

    ```bash  theme={null}
    # If you already have a CrewAI AMP account, or want to create one:
    crewai login
    ```

    When you run either command, the CLI will:

    1. Display a URL and a unique device code
    2. Open your browser to the authentication page
    3. Prompt you to confirm the device
    4. Complete the authentication process

    Upon successful authentication, you'll see a confirmation message in your terminal!
  </Step>

  <Step title="Create a Deployment">
    From your project directory, run:

    ```bash  theme={null}
    crewai deploy create
    ```

    This command will:

    1. Detect your GitHub repository information
    2. Identify environment variables in your local `.env` file
    3. Securely transfer these variables to the Enterprise platform
    4. Create a new deployment with a unique identifier

    On successful creation, you'll see a message like:

    ```shell  theme={null}
    Deployment created successfully!
    Name: your_project_name
    Deployment ID: 01234567-89ab-cdef-0123-456789abcdef
    Current Status: Deploy Enqueued
    ```
  </Step>

  <Step title="Monitor Deployment Progress">
    Track the deployment status with:

    ```bash  theme={null}
    crewai deploy status
    ```

    For detailed logs of the build process:

    ```bash  theme={null}
    crewai deploy logs
    ```

    <Tip>
      The first deployment typically takes 10-15 minutes as it builds the container images. Subsequent deployments are much faster.
    </Tip>
  </Step>
</Steps>


## Additional CLI Commands

The CrewAI CLI offers several commands to manage your deployments:

```bash  theme={null}

# List all your deployments
crewai deploy list


# Get the status of your deployment
crewai deploy status


# View the logs of your deployment
crewai deploy logs


# Push updates after code changes
crewai deploy push


# Remove a deployment
crewai deploy remove <deployment_id>
```


## Option 2: Deploy Directly via Web Interface

You can also deploy your crews directly through the CrewAI AMP web interface by connecting your GitHub account. This approach doesn't require using the CLI on your local machine.

<Steps>
  <Step title="Pushing to GitHub">
    You need to push your crew to a GitHub repository. If you haven't created a crew yet, you can [follow this tutorial](/en/quickstart).
  </Step>

  <Step title="Connecting GitHub to CrewAI AMP">
    1. Log in to [CrewAI AMP](https://app.crewai.com)
    2. Click on the button "Connect GitHub"

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e622053d392d9ca0033bb88b34d82f8d" alt="Connect GitHub Button" data-og-width="1021" width="1021" data-og-height="327" height="327" data-path="images/enterprise/connect-github.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=67a2ba40e2c5dabacfafcb2359e569cf 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=533ddd0da6106dc71b9cbcd010f89a5c 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d8a3f55321172ab1e4179c6d05f30b4d 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=5dc5f7c278ecc22125a1f641454cec2d 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1d8f3da31bd39d97f37b7f405ef3b048 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connect-github.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7ce7bda27a7f94bb173f25fe9845a1cb 2500w" />
    </Frame>
  </Step>

  <Step title="Select the Repository">
    After connecting your GitHub account, you'll be able to select which repository to deploy:

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=937cf62f283090f134e299aa157aad22" alt="Select Repository" data-og-width="3366" width="3366" data-og-height="956" height="956" data-path="images/enterprise/select-repo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3f5167362c6836f644ab356b61c7f8db 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c1293a61ff1fba1b19b8669b942595da 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ac1c94be313ab5c3c3f64741e3696be 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7991df0620583adeb443551dfbf8eeb8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1bf91d7875849fb251fa92c24c1564aa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/select-repo.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=17ab305443f30d6f4796b2415564a3dc 2500w" />
    </Frame>
  </Step>

  <Step title="Set Environment Variables">
    Before deploying, you'll need to set up your environment variables to connect to your LLM provider or other services:

    1. You can add variables individually or in bulk
    2. Enter your environment variables in `KEY=VALUE` format (one per line)

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=84aa7644b9a1e20eb2e38309ce274ccb" alt="Set Environment Variables" data-og-width="3386" width="3386" data-og-height="606" height="606" data-path="images/enterprise/set-env-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c5521837a0ea86776e2ac13883f72750 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=98882c7ba545f4a09bc2248af54bc1ac 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=884ffc4ddc80104657dd60429f262254 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6f811c643a2268d264d95a3701a4d151 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=efd5564b6b4ffe6d68654cbdc8e515cc 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/set-env-variables.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=51fb85358802539cb78c5dc7cf997b92 2500w" />
    </Frame>
  </Step>

  <Step title="Deploy Your Crew">
    1. Click the "Deploy" button to start the deployment process
    2. You can monitor the progress through the progress bar
    3. The first deployment typically takes around 10-15 minutes; subsequent deployments will be faster

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=2eb5fa4cf040c65462a372b6667adc60" alt="Deploy Progress" data-og-width="3386" width="3386" data-og-height="1170" height="1170" data-path="images/enterprise/deploy-progress.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=91d47e6e3edc1df183acb360cbc6af1f 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f917ef44ece66ef051db174b4dea47d8 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=dfc99edd2ff1678afa564ae33cb9c784 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=522b1ce917f9ecd15aee60c0e2241965 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=62ab85baa7a80d6fb98c50fdb7d588c7 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/deploy-progress.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3190fa0b08cfbcdc75d385bde06535fa 2500w" />
    </Frame>

    Once deployment is complete, you'll see:

    * Your crew's unique URL
    * A Bearer token to protect your crew API
    * A "Delete" button if you need to remove the deployment
  </Step>
</Steps>


## ⚠️ Environment Variable Security Requirements

<Warning>
  **Important**: CrewAI AMP has security restrictions on environment variable names that can cause deployment failures if not followed.
</Warning>

### Blocked Environment Variable Patterns

For security reasons, the following environment variable naming patterns are **automatically filtered** and will cause deployment issues:

**Blocked Patterns:**

* Variables ending with `_TOKEN` (e.g., `MY_API_TOKEN`)
* Variables ending with `_PASSWORD` (e.g., `DB_PASSWORD`)
* Variables ending with `_SECRET` (e.g., `API_SECRET`)
* Variables ending with `_KEY` in certain contexts

**Specific Blocked Variables:**

* `GITHUB_USER`, `GITHUB_TOKEN`
* `AWS_REGION`, `AWS_DEFAULT_REGION`
* Various internal CrewAI system variables

### Allowed Exceptions

Some variables are explicitly allowed despite matching blocked patterns:

* `AZURE_AD_TOKEN`
* `AZURE_OPENAI_AD_TOKEN`
* `ENTERPRISE_ACTION_TOKEN`
* `CREWAI_ENTEPRISE_TOOLS_TOKEN`

### How to Fix Naming Issues

If your deployment fails due to environment variable restrictions:

```bash  theme={null}

# ❌ These will cause deployment failures
OPENAI_TOKEN=sk-...
DATABASE_PASSWORD=mypassword
API_SECRET=secret123


# ✅ Use these naming patterns instead
OPENAI_API_KEY=sk-...
DATABASE_CREDENTIALS=mypassword
API_CONFIG=secret123
```

### Best Practices

1. **Use standard naming conventions**: `PROVIDER_API_KEY` instead of `PROVIDER_TOKEN`
2. **Test locally first**: Ensure your crew works with the renamed variables
3. **Update your code**: Change any references to the old variable names
4. **Document changes**: Keep track of renamed variables for your team

<Tip>
  If you encounter deployment failures with cryptic environment variable errors, check your variable names against these patterns first.
</Tip>

### Interact with Your Deployed Crew

Once deployment is complete, you can access your crew through:

1. **REST API**: The platform generates a unique HTTPS endpoint with these key routes:
   * `/inputs`: Lists the required input parameters
   * `/kickoff`: Initiates an execution with provided inputs
   * `/status/{kickoff_id}`: Checks the execution status

2. **Web Interface**: Visit [app.crewai.com](https://app.crewai.com) to access:
   * **Status tab**: View deployment information, API endpoint details, and authentication token
   * **Run tab**: Visual representation of your crew's structure
   * **Executions tab**: History of all executions
   * **Metrics tab**: Performance analytics
   * **Traces tab**: Detailed execution insights

### Trigger an Execution

From the Enterprise dashboard, you can:

1. Click on your crew's name to open its details
2. Select "Trigger Crew" from the management interface
3. Enter the required inputs in the modal that appears
4. Monitor progress as the execution moves through the pipeline

### Monitoring and Analytics

The Enterprise platform provides comprehensive observability features:

* **Execution Management**: Track active and completed runs
* **Traces**: Detailed breakdowns of each execution
* **Metrics**: Token usage, execution times, and costs
* **Timeline View**: Visual representation of task sequences

### Advanced Features

The Enterprise platform also offers:

* **Environment Variables Management**: Securely store and manage API keys
* **LLM Connections**: Configure integrations with various LLM providers
* **Custom Tools Repository**: Create, share, and install tools
* **Crew Studio**: Build crews through a chat interface without writing code

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with deployment issues or questions about the Enterprise platform.
</Card>



# Enable Crew Studio
Source: https://docs.crewai.com/en/enterprise/guides/enable-crew-studio

Enabling Crew Studio on CrewAI AMP

<Tip>
  Crew Studio is a powerful **no-code/low-code** tool that allows you to quickly scaffold or build Crews through a conversational interface.
</Tip>


## What is Crew Studio?

Crew Studio is an innovative way to create AI agent crews without writing code.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c4f5428b111816273b3b53d9cef14fad" alt="Crew Studio Interface" data-og-width="2654" width="2654" data-og-height="1710" height="1710" data-path="images/enterprise/crew-studio-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=35ea9140f0b9e57da5f45adbc7e2f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ae6f0c18ef3679b5466177710fbc4a94 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6c3e2fe013ab4826da90c937a9855635 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=7f1474dd7f983532dc910363b96f783a 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f1a6d7e744e6862af5e72dce4deb0fd1 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-studio-interface.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=74aeb1ccd8e2c8f84d4247b8d0259737 2500w" />
</Frame>

With Crew Studio, you can:

* Chat with the Crew Assistant to describe your problem
* Automatically generate agents and tasks
* Select appropriate tools
* Configure necessary inputs
* Generate downloadable code for customization
* Deploy directly to the CrewAI AMP platform


## Configuration Steps

Before you can start using Crew Studio, you need to configure your LLM connections:

<Steps>
  <Step title="Set Up LLM Connection">
    Go to the **LLM Connections** tab in your CrewAI AMP dashboard and create a new LLM connection.

    <Note>
      Feel free to use any LLM provider you want that is supported by CrewAI.
    </Note>

    Configure your LLM connection:

    * Enter a `Connection Name` (e.g., `OpenAI`)
    * Select your model provider: `openai` or `azure`
    * Select models you'd like to use in your Studio-generated Crews
      * We recommend at least `gpt-4o`, `o1-mini`, and `gpt-4o-mini`
    * Add your API key as an environment variable:
      * For OpenAI: Add `OPENAI_API_KEY` with your API key
      * For Azure OpenAI: Refer to [this article](https://blog.crewai.com/configuring-azure-openai-with-crewai-a-comprehensive-guide/) for configuration details
    * Click `Add Connection` to save your configuration

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c06fcdb008733c7e1d6ec7fcd055ff2c" alt="LLM Connection Configuration" data-og-width="2526" width="2526" data-og-height="1794" height="1794" data-path="images/enterprise/llm-connection-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=929f529b52c50511a773f2ec0791cd9a 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3f922308dfa3d65a392d5ebecec593dd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=df92dce860921dac542382ca3882decb 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1772f4775c3f02e17d152bc00a08ba45 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=508cb4812120d6bc6b3010415f118a4a 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-connection-config.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2eb75a3247fbc61ab727978b8a6ce371 2500w" />
    </Frame>
  </Step>

  <Step title="Verify Connection Added">
    Once you complete the setup, you'll see your new connection added to the list of available connections.

    <Frame>
            <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3726ffaa33f0bfdf221dd542ae729f69" alt="Connection Added" data-og-width="1966" width="1966" data-og-height="532" height="532" data-path="images/enterprise/connection-added.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=4acf6c926c288b5d32f9c537329b4611 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9bdfd3df0a3d3f3ba1d2f91472471ba0 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1658dc464f8869ad3f0eb0595faf4048 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=a0e1b1b559acc03bfbc3a40f17920e40 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=837c27260c5c258d9da4c306e4d16ae0 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/connection-added.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=649700c55072c94135d7a44e07b5f0df 2500w" />
    </Frame>
  </Step>

  <Step title="Configure LLM Defaults">
    In the main menu, go to **Settings → Defaults** and configure the LLM Defaults settings:

    * Select default models for agents and other components
    * Set default configurations for Crew Studio

    Click `Save Settings` to apply your changes.

    <Frame>
            <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b773c2d7e8338e8dbf609ff45ce16eda" alt="LLM Defaults Configuration" data-og-width="2534" width="2534" data-og-height="1128" height="1128" data-path="images/enterprise/llm-defaults.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b08470ddaeb12d378083dff2e852934b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e58e547acb63b13b01fdf52c1771d42d 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c9b45ef41f6b3068580a4085c5c914cf 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=4366e6bb2207f83d10b825a6e5393743 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1a48e293ccbcb1c990cfb0a56d386b32 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/llm-defaults.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f11e748fbc1d3ef89abfef88b95ba9fb 2500w" />
    </Frame>
  </Step>
</Steps>


## Using Crew Studio

Now that you've configured your LLM connection and default settings, you're ready to start using Crew Studio!

<Steps>
  <Step title="Access Studio">
    Navigate to the **Studio** section in your CrewAI AMP dashboard.
  </Step>

  <Step title="Start a Conversation">
    Start a conversation with the Crew Assistant by describing the problem you want to solve:

    ```md  theme={null}
    I need a crew that can research the latest AI developments and create a summary report.
    ```

    The Crew Assistant will ask clarifying questions to better understand your requirements.
  </Step>

  <Step title="Review Generated Crew">
    Review the generated crew configuration, including:

    * Agents and their roles
    * Tasks to be performed
    * Required inputs
    * Tools to be used

    This is your opportunity to refine the configuration before proceeding.
  </Step>

  <Step title="Deploy or Download">
    Once you're satisfied with the configuration, you can:

    * Download the generated code for local customization
    * Deploy the crew directly to the CrewAI AMP platform
    * Modify the configuration and regenerate the crew
  </Step>

  <Step title="Test Your Crew">
    After deployment, test your crew with sample inputs to ensure it performs as expected.
  </Step>
</Steps>

<Tip>
  For best results, provide clear, detailed descriptions of what you want your crew to accomplish. Include specific inputs and expected outputs in your description.
</Tip>


## Example Workflow

Here's a typical workflow for creating a crew with Crew Studio:

<Steps>
  <Step title="Describe Your Problem">
    Start by describing your problem:

    ```md  theme={null}
    I need a crew that can analyze financial news and provide investment recommendations
    ```
  </Step>

  <Step title="Answer Questions">
    Respond to clarifying questions from the Crew Assistant to refine your requirements.
  </Step>

  <Step title="Review the Plan">
    Review the generated crew plan, which might include:

    * A Research Agent to gather financial news
    * An Analysis Agent to interpret the data
    * A Recommendations Agent to provide investment advice
  </Step>

  <Step title="Approve or Modify">
    Approve the plan or request changes if necessary.
  </Step>

  <Step title="Download or Deploy">
    Download the code for customization or deploy directly to the platform.
  </Step>

  <Step title="Test and Refine">
    Test your crew with sample inputs and refine as needed.
  </Step>
</Steps>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Crew Studio or any other CrewAI AMP features.
</Card>



# Gmail Trigger
Source: https://docs.crewai.com/en/enterprise/guides/gmail-trigger

Trigger automations when Gmail events occur (e.g., new emails, labels).


## Overview

Use the Gmail Trigger to kick off your deployed crews when Gmail events happen in connected accounts, such as receiving a new email or messages matching a label/filter.

<Tip>
  Make sure Gmail is connected in Tools & Integrations and the trigger is enabled for your deployment.
</Tip>


## Enabling the Gmail Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Gmail** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10b3ee6296f323168473593b64a1e4c8" alt="Enable or disable triggers with toggle" data-og-width="1984" width="1984" data-og-height="866" height="866" data-path="images/enterprise/trigger-selected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27137c8d8c072ece3319e9f4c8ee0185 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=842109fa147a6a91b9f9480e450a8ee0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5f2cbab1be7662c99854f88496f42b4b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fa4240b233d980059d3db96c493fda4 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37f3001a39aab6400b8df45fad9b5cfa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b2959938cb0f239a6113c9a8b7aa0356 2500w" />
</Frame>


## Example: Process new emails

When a new email arrives, the Gmail Trigger will send the payload to your Crew or Flow. Below is a Crew example that parses and processes the trigger payload.

```python  theme={null}
@CrewBase
class GmailProcessingCrew:
    @agent
    def parser(self) -> Agent:
        return Agent(
            config=self.agents_config['parser'],
        )

    @task
    def parse_gmail_payload(self) -> Task:
        return Task(
            config=self.tasks_config['parse_gmail_payload'],
            agent=self.parser(),
        )

    @task
    def act_on_email(self) -> Task:
        return Task(
            config=self.tasks_config['act_on_email'],
            agent=self.parser(),
        )
```

The Gmail payload will be available via the standard context mechanisms.

### Testing Locally

Test your Gmail trigger integration locally using the CrewAI CLI:

```bash  theme={null}

# View all available triggers
crewai triggers list


# Simulate a Gmail trigger with realistic payload
crewai triggers run gmail/new_email
```

The `crewai triggers run` command will execute your crew with a complete Gmail payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run gmail/new_email` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>


## Monitoring Executions

Track history and performance of triggered runs:

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>


## Troubleshooting

* Ensure Gmail is connected in Tools & Integrations
* Verify the Gmail Trigger is enabled on the Triggers tab
* Test locally with `crewai triggers run gmail/new_email` to see the exact payload structure
* Check the execution logs and confirm the payload is passed as `crewai_trigger_payload`
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution



# Google Calendar Trigger
Source: https://docs.crewai.com/en/enterprise/guides/google-calendar-trigger

Kick off crews when Google Calendar events are created, updated, or cancelled


## Overview

Use the Google Calendar trigger to launch automations whenever calendar events change. Common use cases include briefing a team before a meeting, notifying stakeholders when a critical event is cancelled, or summarizing daily schedules.

<Tip>
  Make sure Google Calendar is connected in **Tools & Integrations** and enabled for the deployment you want to automate.
</Tip>


## Enabling the Google Calendar Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Google Calendar** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e6594f439112ba76a399585e3e69e166" alt="Enable or disable triggers with toggle" data-og-width="2228" width="2228" data-og-height="1000" height="1000" data-path="images/enterprise/calendar-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=fa2e4f7da20c86c5ad7a6b7e2ab96116 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c3f8a6638774eadefa5a5924328d5787 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=a2b8c83efc9a11a156877a8f061ca39c 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c772c71eda91c64d2db474c2ecb74159 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=35c5f5fe2de12a82aa0f1f798380def1 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/calendar-trigger.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=1fefaff8a0a2cf8e9d7d4c11203ed0eb 2500w" />
</Frame>


## Example: Summarize meeting details

The snippet below mirrors the `calendar-event-crew.py` example in the trigger repository. It parses the payload, analyses the attendees and timing, and produces a meeting brief for downstream tools.

```python  theme={null}
from calendar_event_crew import GoogleCalendarEventTrigger

crew = GoogleCalendarEventTrigger().crew()
result = crew.kickoff({
    "crewai_trigger_payload": calendar_payload,
})
print(result.raw)
```

Use `crewai_trigger_payload` exactly as it is delivered by the trigger so the crew can extract the proper fields.


## Testing Locally

Test your Google Calendar trigger integration locally using the CrewAI CLI:

```bash  theme={null}

# View all available triggers
crewai triggers list


# Simulate a Google Calendar trigger with realistic payload
crewai triggers run google_calendar/event_changed
```

The `crewai triggers run` command will execute your crew with a complete Calendar payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run google_calendar/event_changed` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>


## Monitoring Executions

The **Executions** list in the deployment dashboard tracks every triggered run and surfaces payload metadata, output summaries, and errors.

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>


## Troubleshooting

* Ensure the correct Google account is connected and the trigger is enabled
* Test locally with `crewai triggers run google_calendar/event_changed` to see the exact payload structure
* Confirm your workflow handles all-day events (payloads use `start.date` and `end.date` instead of timestamps)
* Check execution logs if reminders or attendee arrays are missing—calendar permissions can limit fields in the payload
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution



# Google Drive Trigger
Source: https://docs.crewai.com/en/enterprise/guides/google-drive-trigger

Respond to Google Drive file events with automated crews


## Overview

Trigger your automations when files are created, updated, or removed in Google Drive. Typical workflows include summarizing newly uploaded content, enforcing sharing policies, or notifying owners when critical files change.

<Tip>
  Connect Google Drive in **Tools & Integrations** and confirm the trigger is enabled for the automation you want to monitor.
</Tip>


## Enabling the Google Drive Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Google Drive** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=caef65990821bbc38454b46ca8f7bc46" alt="Enable or disable triggers with toggle" data-og-width="2208" width="2208" data-og-height="1540" height="1540" data-path="images/enterprise/gdrive-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=26fc4c3542735f7ff2f8723a7bec0265 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=67b08f32c76c711734916902a4df35a3 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=5d0695c5d0f5ebd51d6413c0334a0ce6 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6b2600ca253c042e06f2108c68d5cff3 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=62541a717c8dee05cee7310561882f58 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/gdrive-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ac92f2d61bf065c81a2ce6f02cac5d9d 2500w" />
</Frame>


## Example: Summarize file activity

The drive example crews parse the payload to extract file metadata, evaluate permissions, and publish a summary.

```python  theme={null}
from drive_file_crew import GoogleDriveFileTrigger

crew = GoogleDriveFileTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": drive_payload,
})
```


## Testing Locally

Test your Google Drive trigger integration locally using the CrewAI CLI:

```bash  theme={null}

# View all available triggers
crewai triggers list


# Simulate a Google Drive trigger with realistic payload
crewai triggers run google_drive/file_changed
```

The `crewai triggers run` command will execute your crew with a complete Drive payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run google_drive/file_changed` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>


## Monitoring Executions

Track history and performance of triggered runs with the **Executions** list in the deployment dashboard.

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>


## Troubleshooting

* Verify Google Drive is connected and the trigger toggle is enabled
* Test locally with `crewai triggers run google_drive/file_changed` to see the exact payload structure
* If a payload is missing permission data, ensure the connected account has access to the file or folder
* The trigger sends file IDs only; use the Drive API if you need to fetch binary content during the crew run
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution



# HubSpot Trigger
Source: https://docs.crewai.com/en/enterprise/guides/hubspot-trigger

Trigger CrewAI crews directly from HubSpot Workflows

This guide provides a step-by-step process to set up HubSpot triggers for CrewAI AMP, enabling you to initiate crews directly from HubSpot Workflows.


## Prerequisites

* A CrewAI AMP account
* A HubSpot account with the [HubSpot Workflows](https://knowledge.hubspot.com/workflows/create-workflows) feature


## Setup Steps

<Steps>
  <Step title="Connect your HubSpot account with CrewAI AMP">
    * Log in to your `CrewAI AMP account > Triggers`
    * Select `HubSpot` from the list of available triggers
    * Choose the HubSpot account you want to connect with CrewAI AMP
    * Follow the on-screen prompts to authorize CrewAI AMP access to your HubSpot account
    * A confirmation message will appear once HubSpot is successfully connected with CrewAI AMP
  </Step>

  <Step title="Create a HubSpot Workflow">
    * Log in to your `HubSpot account > Automations > Workflows > New workflow`
    * Select the workflow type that fits your needs (e.g., Start from scratch)
    * In the workflow builder, click the Plus (+) icon to add a new action.
    * Choose `Integrated apps > CrewAI > Kickoff a Crew`.
    * Select the Crew you want to initiate.
    * Click `Save` to add the action to your workflow

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d53acad518d2e330bd4a69ca76808b11" alt="HubSpot Workflow 1" data-og-width="670" width="670" data-og-height="556" height="556" data-path="images/enterprise/hubspot-workflow-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=54aa0bc6e1080e9dfbd5184e23ebefe3 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9eaec24db82ba8a59ac9c43047ce2d1 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f100f688d3f1961f0328d4141f04ad99 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c2147f9de1f60270ef81c5d271acd272 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=aec4cc0e27775dd21cbfb35fad7c6634 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-1.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=24d1d4bb9cc84719f78166c6bfa5de81 2500w" />
    </Frame>
  </Step>

  <Step title="Use Crew results with other actions">
    * After the Kickoff a Crew step, click the Plus (+) icon to add a new action.
    * For example, to send an internal email notification, choose `Communications > Send internal email notification`
    * In the Body field, click `Insert data`, select `View properties or action outputs from > Action outputs > Crew Result` to include Crew data in the email
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a096e4d667b63a65b1061bdc5f659199" alt="HubSpot Workflow 2" data-og-width="670" width="670" data-og-height="437" height="437" data-path="images/enterprise/hubspot-workflow-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ffe8190dbfdc46039f7ddfb586566ac2 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=066a379f6f677a48a07d66a61b192722 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=871c51f5376163d894e0945665a17b37 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=eb6be36a9c8432789077b82465038c16 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=448437694af0fd88f3d0667ecd6e9ef9 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-2.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0a1ef821542f93d1d51601eb3954273a 2500w" />
      </Frame>
    * Configure any additional actions as needed
    * Review your workflow steps to ensure everything is set up correctly
    * Activate the workflow
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b8e6f426200408867d0a09526a93f32f" alt="HubSpot Workflow 3" data-og-width="670" width="670" data-og-height="647" height="647" data-path="images/enterprise/hubspot-workflow-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0b59d6e2251da148d974ec0605a78acd 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=04629b326d956c53658267c418818165 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=eae451ae67430e9283936cd3d06edb26 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=389235975e0ca14bbb3a6b1b307d7508 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0863f7fdf8ef41628ab5b2093700f25f 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/hubspot-workflow-3.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=89186e6b7ebc362512ea3dc05407dcec 2500w" />
      </Frame>
  </Step>
</Steps>

For more detailed information on available actions and customization options, refer to the [HubSpot Workflows Documentation](https://knowledge.hubspot.com/workflows/create-workflows).



# Kickoff Crew
Source: https://docs.crewai.com/en/enterprise/guides/kickoff-crew

Kickoff a Crew on CrewAI AMP


## Overview

Once you've deployed your crew to the CrewAI AMP platform, you can kickoff executions through the web interface or the API. This guide covers both approaches.


## Method 1: Using the Web Interface

### Step 1: Navigate to Your Deployed Crew

1. Log in to [CrewAI AMP](https://app.crewai.com)
2. Click on the crew name from your projects list
3. You'll be taken to the crew's detail page

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-dashboard.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=6dfd552914d3ed5ec24abb1ba606ff7d" alt="Crew Dashboard" data-og-width="1492" width="1492" data-og-height="872" height="872" data-path="images/enterprise/crew-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-dashboard.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=1739393031a256a20e480601b516f166 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-dashboard.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=d771e6e346daa641591c5dfaed250526 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-dashboard.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=249cdd195f22e4e1be51481394cd6429 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-dashboard.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9495b452ab0adaf89ae863017ee4a263 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-dashboard.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=af151b37c275e4a2b1bdcab7c58912b3 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew-dashboard.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=678a00a07d5d341e7c96fb540838ed7c 2500w" />
</Frame>

### Step 2: Initiate Execution

From your crew's detail page, you have two options to kickoff an execution:

#### Option A: Quick Kickoff

1. Click the `Kickoff` link in the Test Endpoints section
2. Enter the required input parameters for your crew in the JSON editor
3. Click the `Send Request` button

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-endpoint.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=39603fac859ca2a602c51c585c2a4861" alt="Kickoff Endpoint" data-og-width="2794" width="2794" data-og-height="1390" height="1390" data-path="images/enterprise/kickoff-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-endpoint.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=97c5cbd4f5479503aaa9e84cf6887999 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-endpoint.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b619f306030ded60e9ff407427f55eef 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-endpoint.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ab157bd45c1e0ce88a7d0c88a77b4be 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-endpoint.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8547e269937b1ff517e39bd12e331b3e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-endpoint.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=193d48bee71f83154abfde44a5ddc832 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-endpoint.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=867e83c10f3c141d710eb364928fea1d 2500w" />
</Frame>

#### Option B: Using the Visual Interface

1. Click the `Run` tab in the crew detail page
2. Enter the required inputs in the form fields
3. Click the `Run Crew` button

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/run-crew.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=87b09919c9210c7ca8fb0b0952d99005" alt="Run Crew" data-og-width="2808" width="2808" data-og-height="1764" height="1764" data-path="images/enterprise/run-crew.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/run-crew.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b12804d306d40eb61e4e4652f6ccc92e 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/run-crew.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2a2654d625865e0b52f70b55c544c160 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/run-crew.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8df82b35aff39cedda1db84dab9f1218 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/run-crew.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1f3beb1e779c5335e7e2ab5b001977a9 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/run-crew.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=414273765a6d9e1c440f17528b016117 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/run-crew.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d68137f3cfc9d6596a47522bd1598c93 2500w" />
</Frame>

### Step 3: Monitor Execution Progress

After initiating the execution:

1. You'll receive a response containing a `kickoff_id` - **copy this ID**
2. This ID is essential for tracking your execution

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/copy-task-id.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=f5d6e458d4773fb94590d7accdde8499" alt="Copy Task ID" data-og-width="2790" width="2790" data-og-height="1040" height="1040" data-path="images/enterprise/copy-task-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/copy-task-id.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=106491ef8ba9b0bac48212d837ff222b 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/copy-task-id.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=dc3c8d2d45b6ab8cfc725cbd633b80b1 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/copy-task-id.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=ce1dbcd4aef6f2e2a8b26aa1159b0901 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/copy-task-id.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=3856219b389380be1edb4c44780af528 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/copy-task-id.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=77fe0191cc30085da4d0c219066cae40 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/copy-task-id.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c92039468d636c655e0db602bab300ff 2500w" />
</Frame>

### Step 4: Check Execution Status

To monitor the progress of your execution:

1. Click the "Status" endpoint in the Test Endpoints section
2. Paste the `kickoff_id` into the designated field
3. Click the "Get Status" button

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/get-status.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f8c8f553fd5797fab5fbec2993f5d745" alt="Get Status" data-og-width="2774" width="2774" data-og-height="452" height="452" data-path="images/enterprise/get-status.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/get-status.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=594fac15c90f574d250a4fafa6d641be 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/get-status.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=995fac2247e5db9ec52c24ab65e39e8e 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/get-status.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d16d09a460213237b0210c3bc0b19b06 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/get-status.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18907b2ed5c2dac72f9136f372c10e0a 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/get-status.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0592dce31df3bbb19fe62461066ed72a 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/get-status.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fc2f61587694f6a8045894c0a72dbdb7 2500w" />
</Frame>

The status response will show:

* Current execution state (`running`, `completed`, etc.)
* Details about which tasks are in progress
* Any outputs produced so far

### Step 5: View Final Results

Once execution is complete:

1. The status will change to `completed`
2. You can view the full execution results and outputs
3. For a more detailed view, check the `Executions` tab in the crew detail page


## Method 2: Using the API

You can also kickoff crews programmatically using the CrewAI AMP REST API.

### Authentication

All API requests require a bearer token for authentication:

```bash  theme={null}
curl -H "Authorization: Bearer YOUR_CREW_TOKEN" https://your-crew-url.crewai.com
```

Your bearer token is available on the Status tab of your crew's detail page.

### Checking Crew Health

Before executing operations, you can verify that your crew is running properly:

```bash  theme={null}
curl -H "Authorization: Bearer YOUR_CREW_TOKEN" https://your-crew-url.crewai.com
```

A successful response will return a message indicating the crew is operational:

```
Healthy%
```

### Step 1: Retrieve Required Inputs

First, determine what inputs your crew requires:

```bash  theme={null}
curl -X GET \
  -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  https://your-crew-url.crewai.com/inputs
```

The response will be a JSON object containing an array of required input parameters, for example:

```json  theme={null}
{"inputs":["topic","current_year"]}
```

This example shows that this particular crew requires two inputs: `topic` and `current_year`.

### Step 2: Kickoff Execution

Initiate execution by providing the required inputs:

```bash  theme={null}
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  -d '{"inputs": {"topic": "AI Agent Frameworks", "current_year": "2025"}}' \
  https://your-crew-url.crewai.com/kickoff
```

The response will include a `kickoff_id` that you'll need for tracking:

```json  theme={null}
{"kickoff_id":"abcd1234-5678-90ef-ghij-klmnopqrstuv"}
```

### Step 3: Check Execution Status

Monitor the execution progress using the kickoff\_id:

```bash  theme={null}
curl -X GET \
  -H "Authorization: Bearer YOUR_CREW_TOKEN" \
  https://your-crew-url.crewai.com/status/abcd1234-5678-90ef-ghij-klmnopqrstuv
```


## Handling Executions

### Long-Running Executions

For executions that may take a long time:

1. Consider implementing a polling mechanism to check status periodically
2. Use webhooks (if available) for notification when execution completes
3. Implement error handling for potential timeouts

### Execution Context

The execution context includes:

* Inputs provided at kickoff
* Environment variables configured during deployment
* Any state maintained between tasks

### Debugging Failed Executions

If an execution fails:

1. Check the "Executions" tab for detailed logs
2. Review the "Traces" tab for step-by-step execution details
3. Look for LLM responses and tool usage in the trace details

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with execution issues or questions about the Enterprise platform.
</Card>



# Microsoft Teams Trigger
Source: https://docs.crewai.com/en/enterprise/guides/microsoft-teams-trigger

Kick off crews from Microsoft Teams chat activity


## Overview

Use the Microsoft Teams trigger to start automations whenever a new chat is created. Common patterns include summarizing inbound requests, routing urgent messages to support teams, or creating follow-up tasks in other systems.

<Tip>
  Confirm Microsoft Teams is connected under **Tools & Integrations** and enabled in the **Triggers** tab for your deployment.
</Tip>


## Enabling the Microsoft Teams Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Microsoft Teams** and switch the toggle to enable

<Frame caption="Microsoft Teams trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=21eced4a8a635d17e32dccbeaf4ac217" alt="Enable or disable triggers with toggle" data-og-width="2192" width="2192" data-og-height="492" height="492" data-path="images/enterprise/msteams-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=3acc624c7b67651b5cd41df314902c41 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=1270b8fb54dc348f6cd242d2f3fd6480 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=76c96b3b169dd164c31e7bf88d4fdd8c 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=04b9e72848e035c107a0857ae708a0f3 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=bee29617f472e6d4709d74c764d201c8 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/msteams-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=c73be9f59015ab22173857ce635a2be9 2500w" />
</Frame>


## Example: Summarize a new chat thread

```python  theme={null}
from teams_chat_created_crew import MicrosoftTeamsChatTrigger

crew = MicrosoftTeamsChatTrigger().crew()
result = crew.kickoff({
    "crewai_trigger_payload": teams_payload,
})
print(result.raw)
```

The crew parses thread metadata (subject, created time, roster) and generates an action plan for the receiving team.


## Testing Locally

Test your Microsoft Teams trigger integration locally using the CrewAI CLI:

```bash  theme={null}

# View all available triggers
crewai triggers list


# Simulate a Microsoft Teams trigger with realistic payload
crewai triggers run microsoft_teams/teams_message_created
```

The `crewai triggers run` command will execute your crew with a complete Teams payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run microsoft_teams/teams_message_created` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>


## Troubleshooting

* Ensure the Teams connection is active; it must be refreshed if the tenant revokes permissions
* Test locally with `crewai triggers run microsoft_teams/teams_message_created` to see the exact payload structure
* Confirm the webhook subscription in Microsoft 365 is still valid if payloads stop arriving
* Review execution logs for payload shape mismatches—Graph notifications may omit fields when a chat is private or restricted
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution



# OneDrive Trigger
Source: https://docs.crewai.com/en/enterprise/guides/onedrive-trigger

Automate responses to OneDrive file activity


## Overview

Start automations when files change inside OneDrive. You can generate audit summaries, notify security teams about external sharing, or update downstream line-of-business systems with new document metadata.

<Tip>
  Connect OneDrive in **Tools & Integrations** and toggle the trigger on for your deployment.
</Tip>


## Enabling the OneDrive Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **OneDrive** and switch the toggle to enable

<Frame caption="Microsoft OneDrive trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=55774f3aee2c024ee81e8d543d9391be" alt="Enable or disable triggers with toggle" data-og-width="2166" width="2166" data-og-height="478" height="478" data-path="images/enterprise/onedrive-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=82cf038f92dfd9771c87ff44d364c42b 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=d79a78258619bcc517c9bcbf0e1b42f4 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=6e5fc33aaebcffe573195b7b7a85986e 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=bbd2f96f33f12988c8c52f36e178e553 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=ef16d274ea3fe359655c8ac163b3c97a 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/onedrive-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=0efecea63f338e2cdf7372a627993bac 2500w" />
</Frame>


## Example: Audit file permissions

```python  theme={null}
from onedrive_file_crew import OneDriveFileTrigger

crew = OneDriveFileTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": onedrive_payload,
})
```

The crew inspects file metadata, user activity, and permission changes to produce a compliance-friendly summary.


## Testing Locally

Test your OneDrive trigger integration locally using the CrewAI CLI:

```bash  theme={null}

# View all available triggers
crewai triggers list


# Simulate a OneDrive trigger with realistic payload
crewai triggers run microsoft_onedrive/file_changed
```

The `crewai triggers run` command will execute your crew with a complete OneDrive payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run microsoft_onedrive/file_changed` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>


## Troubleshooting

* Ensure the connected account has permission to read the file metadata included in the webhook
* Test locally with `crewai triggers run microsoft_onedrive/file_changed` to see the exact payload structure
* If the trigger fires but the payload is missing `permissions`, confirm the site-level sharing settings allow Graph to return this field
* For large tenants, filter notifications upstream so the crew only runs on relevant directories
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution



# Outlook Trigger
Source: https://docs.crewai.com/en/enterprise/guides/outlook-trigger

Launch automations from Outlook emails and calendar updates


## Overview

Automate responses when Outlook delivers a new message or when an event is removed from the calendar. Teams commonly route escalations, file tickets, or alert attendees of cancellations.

<Tip>
  Connect Outlook in **Tools & Integrations** and ensure the trigger is enabled for your deployment.
</Tip>


## Enabling the Outlook Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Outlook** and switch the toggle to enable

<Frame caption="Microsoft Outlook trigger connection">
  <img src="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f8a739ad0963ccddafeed60f21366628" alt="Enable or disable triggers with toggle" data-og-width="2186" width="2186" data-og-height="508" height="508" data-path="images/enterprise/outlook-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=280&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=03b5121587c619936c87f05e15992f08 280w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=560&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=651d2efd933f7109b216d343e6d6a6ce 560w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=840&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=a7a27424bf507c739280376fd57ea80d 840w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=1100&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=481164952ea35f62566b09d392a0910b 1100w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=1650&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=f4d3db361e699578e9ce44bde1e683fd 1650w, https://mintcdn.com/crewai/oMMe1eXJrzmWf3MN/images/enterprise/outlook-trigger.png?w=2500&fit=max&auto=format&n=oMMe1eXJrzmWf3MN&q=85&s=aaabf7a26259291cf3b8545a4c3a996d 2500w" />
</Frame>


## Example: Summarize a new email

```python  theme={null}
from outlook_message_crew import OutlookMessageTrigger

crew = OutlookMessageTrigger().crew()
crew.kickoff({
    "crewai_trigger_payload": outlook_payload,
})
```

The crew extracts sender details, subject, body preview, and attachments before generating a structured response.


## Testing Locally

Test your Outlook trigger integration locally using the CrewAI CLI:

```bash  theme={null}

# View all available triggers
crewai triggers list


# Simulate an Outlook trigger with realistic payload
crewai triggers run microsoft_outlook/email_received
```

The `crewai triggers run` command will execute your crew with a complete Outlook payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run microsoft_outlook/email_received` (not `crewai run`) to simulate trigger execution during development. After deployment, your crew will automatically receive the trigger payload.
</Warning>


## Troubleshooting

* Verify the Outlook connector is still authorized; the subscription must be renewed periodically
* Test locally with `crewai triggers run microsoft_outlook/email_received` to see the exact payload structure
* If attachments are missing, confirm the webhook subscription includes the `includeResourceData` flag
* Review execution logs when events fail to match—cancellation payloads lack attendee lists by design and the crew should account for that
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution



# Salesforce Trigger
Source: https://docs.crewai.com/en/enterprise/guides/salesforce-trigger

Trigger CrewAI crews from Salesforce workflows for CRM automation

CrewAI AMP can be triggered from Salesforce to automate customer relationship management workflows and enhance your sales operations.


## Overview

Salesforce is a leading customer relationship management (CRM) platform that helps businesses streamline their sales, service, and marketing operations. By setting up CrewAI triggers from Salesforce, you can:

* Automate lead scoring and qualification
* Generate personalized sales materials
* Enhance customer service with AI-powered responses
* Streamline data analysis and reporting


## Demo

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/oJunVqjjfu4" title="CrewAI + Salesforce trigger demo" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />


## Getting Started

To set up Salesforce triggers:

1. **Contact Support**: Reach out to CrewAI AMP support for assistance with Salesforce trigger setup
2. **Review Requirements**: Ensure you have the necessary Salesforce permissions and API access
3. **Configure Connection**: Work with the support team to establish the connection between CrewAI and your Salesforce instance
4. **Test Triggers**: Verify the triggers work correctly with your specific use cases


## Use Cases

Common Salesforce + CrewAI trigger scenarios include:

* **Lead Processing**: Automatically analyze and score incoming leads
* **Proposal Generation**: Create customized proposals based on opportunity data
* **Customer Insights**: Generate analysis reports from customer interaction history
* **Follow-up Automation**: Create personalized follow-up messages and recommendations


## Next Steps

For detailed setup instructions and advanced configuration options, please contact CrewAI AMP support who can provide tailored guidance for your specific Salesforce environment and business needs.



# Slack Trigger
Source: https://docs.crewai.com/en/enterprise/guides/slack-trigger

Trigger CrewAI crews directly from Slack using slash commands

This guide explains how to start a crew directly from Slack using CrewAI triggers.


## Prerequisites

* CrewAI Slack trigger installed and connected to your Slack workspace
* At least one crew configured in CrewAI


## Setup Steps

<Steps>
  <Step title="Ensure the CrewAI Slack trigger is set up">
    In the CrewAI dashboard, navigate to the **Triggers** section.

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6d976bf9516d737af0b7ea3a77aa2b2a" alt="CrewAI Slack Integration" data-og-width="1962" width="1962" data-og-height="1052" height="1052" data-path="images/enterprise/slack-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ce8a2090ccca8027450db4f447f65cd 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=72063bc9e37d7ca4f495cb4dcac4fd04 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bfb09bbf40fa85cff58485d75d6d2e55 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=30e1149f8bbe585c443d9b57c33d3888 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c6b943586531c6fab7eab1b9c2f61092 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/slack-integration.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=106a0fe6ed7e2f3a69b5bde02f21d860 2500w" />
    </Frame>

    Verify that Slack is listed and is connected.
  </Step>

  <Step title="Open your Slack channel">
    * Navigate to the channel where you want to kickoff the crew.
    * Type the slash command "**/kickoff**" to initiate the crew kickoff process.
    * You should see a  "**Kickoff crew**" appear as you type:
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=cf16579e88e59903af9ac3f2ef374555" alt="Kickoff crew" data-og-width="601" width="601" data-og-height="157" height="157" data-path="images/enterprise/kickoff-slack-crew.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f43ffa15817823e76313f33c889f5708 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bd173c20d88c0bf4466f1af1098bb285 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=00d64ee5b69f4c9497f32dd18335f53e 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6a38124f5f963b15b1cc0d6acaa1996f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=94c6909651b61ec2b4de17687d1ce95a 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=47df98421d2a98e3fbc19015d2cb48ee 2500w" />
      </Frame>
    * Press Enter or select the "**Kickoff crew**" option. A dialog box titled "**Kickoff an AI Crew**" will appear.
  </Step>

  <Step title="Select the crew you want to start">
    * In the dropdown menu labeled "**Select of the crews online:**", choose the crew you want to start.
    * In the example below, "**prep-for-meeting**" is selected:
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7c92f688fcd7f1f0251cd90670014e34" alt="Kickoff crew dropdown" data-og-width="631" width="631" data-og-height="333" height="333" data-path="images/enterprise/kickoff-slack-crew-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7efe2a1a20f23311e914b0fdedf7532a 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2bb784762404d9d7713743e8da6f0057 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5aa472c131ee27c39c925b555f6d451d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18b84066d96edbacc103e57e99be592e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=208d754df14ea8bcd287990df3d6bd55 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-dropdown.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=98efd80f079ee57494997f45e03455ed 2500w" />
      </Frame>
    * If your crew requires any inputs, click the "**Add Inputs**" button to provide them.
      <Note>
        The "**Add Inputs**" button is shown in the example above but is not yet clicked.
      </Note>
  </Step>

  <Step title="Click Kickoff and wait for the crew to complete">
    * Once you've selected the crew and added any necessary inputs, click "**Kickoff**" to start the crew.
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e5bebbf61fb92832dc1ebef0a77d5654" alt="Kickoff crew" data-og-width="628" width="628" data-og-height="771" height="771" data-path="images/enterprise/kickoff-slack-crew-kickoff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3c04a8e5c5f45211135c3b31423b3baf 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6d444a78f6991956f03eb92c8e83de0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=789ad738a8dd10a4e9ad83de0be5faf3 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a1fec0a13f00082ab70c7c12744d2954 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2d7e271cf05848aaebdd7445923f6daf 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-kickoff.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=912bf7b4abb0d51b46ddf3f9d02230c2 2500w" />
      </Frame>
    * The crew will start executing and you will see the results in the Slack channel.
      <Frame>
        <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a3d451c03c3ff7ebf64eb9bb1b41c18c" alt="Kickoff crew results" data-og-width="653" width="653" data-og-height="678" height="678" data-path="images/enterprise/kickoff-slack-crew-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fcaf9677647222c1a7c716ed197c9c60 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bf3ff58196c634ebbaa545ad815593ba 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=34fd1fcef59569b7503b47587e29b31b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ceeb582a0ea6ce7c4ce86080c5f09506 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7b1bac2cd281b5770f3ad33d13fc3e22 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/kickoff-slack-crew-results.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1bef274ced3f62e923578f882cc36fc8 2500w" />
      </Frame>
  </Step>
</Steps>


## Tips

* Make sure you have the necessary permissions to use the `/kickoff` command in your Slack workspace.
* If you don't see your desired crew in the dropdown, ensure it's properly configured and online in CrewAI.



# Update Crew
Source: https://docs.crewai.com/en/enterprise/guides/update-crew

Updating a Crew on CrewAI AMP

<Note>
  After deploying your crew to CrewAI AMP, you may need to make updates to the code, security settings, or configuration.
  This guide explains how to perform these common update operations.
</Note>


## Why Update Your Crew?

CrewAI won't automatically pick up GitHub updates by default, so you'll need to manually trigger updates, unless you checked the `Auto-update` option when deploying your crew.

There are several reasons you might want to update your crew deployment:

* You want to update the code with a latest commit you pushed to GitHub
* You want to reset the bearer token for security reasons
* You want to update environment variables


## 1. Updating Your Crew Code for a Latest Commit

When you've pushed new commits to your GitHub repository and want to update your deployment:

1. Navigate to your crew in the CrewAI AMP platform
2. Click on the `Re-deploy` button on your crew details page

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1dc96ae0dd8f0dc2f5f62f58ebd6e5d0" alt="Re-deploy Button" data-og-width="980" width="980" data-og-height="852" height="852" data-path="images/enterprise/redeploy-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8d240851abcc6a015002a129ac12274b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2655800484e20180df0d3bc88e563ef8 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f8d7850c288577c99242ada871e5eb7c 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d5c4dd51e512466df9209fa6218bbb9e 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=15e03da40d3e92fe0c9615b28f4efce8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/redeploy-button.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8d29aa1f4ac64a30a01c449b2f31aead 2500w" />
</Frame>

This will trigger an update that you can track using the progress bar. The system will pull the latest code from your repository and rebuild your deployment.


## 2. Resetting Bearer Token

If you need to generate a new bearer token (for example, if you suspect the current token might have been compromised):

1. Navigate to your crew in the CrewAI AMP platform
2. Find the `Bearer Token` section
3. Click the `Reset` button next to your current token

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c38b0a22de7a192a1962b4b371e03119" alt="Reset Token" data-og-width="980" width="980" data-og-height="840" height="840" data-path="images/enterprise/reset-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=759453ab874cffd228bbbc91db2cbe3c 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=365f3075be71ad8ed85e1a9ba7cbe9b5 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7b689e67e67abb1e39cd6e98efa1e562 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7dfbd9d08e16bb16de00d6e7fde00a6d 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=900c92322f9cd90732ccdfa1f8d9ea42 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/reset-token.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=000718aaaa645b109514bc72c2f0b70e 2500w" />
</Frame>

<Warning>
  Resetting your bearer token will invalidate the previous token immediately. Make sure to update any applications or scripts that are using the old token.
</Warning>


## 3. Updating Environment Variables

To update the environment variables for your crew:

1. First access the deployment page by clicking on your crew's name

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=740ad7bcf5b860f35fe9fddd7a707271" alt="Environment Variables Button" data-og-width="1216" width="1216" data-og-height="598" height="598" data-path="images/enterprise/env-vars-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a4bdc54aee3c54cedc4c25f0b0e28aaa 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f3012e2c4257313f080afeb2ab0c690b 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9532e4a7281391aacacc1faaf14e6f74 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ea0aaee0f92be7b9ef4b62cc64e12877 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ca4a47c02e4761b05b83af8fb118e915 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/env-vars-button.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=542188110b78b31121abba738a28019d 2500w" />
</Frame>

2. Locate the `Environment Variables` section (you will need to click the `Settings` icon to access it)
3. Edit the existing variables or add new ones in the fields provided
4. Click the `Update` button next to each variable you modify

<Frame>
    <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=461ca7ce61dd14a4344f6237c584b891" alt="Update Environment Variables" data-og-width="2888" width="2888" data-og-height="1914" height="1914" data-path="images/enterprise/update-env-vars.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9afc7b7e194a371365d7b69edc0ddac6 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8ccb5b296eab23dd57cc241f7f445589 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=374a4a1f02dd73e7eb7e30e4de59b0ac 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=23357a7c2e61f08b456e20450eaa255f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bb82e60664a74c99ae0fa88dae8366a8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/update-env-vars.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1d764223f3032607fd6d2577452c021a 2500w" />
</Frame>

5. Finally, click the `Update Deployment` button at the bottom of the page to apply the changes

<Note>
  Updating environment variables will trigger a new deployment, but this will only update the environment configuration and not the code itself.
</Note>


## After Updating

After performing any update:

1. The system will rebuild and redeploy your crew
2. You can monitor the deployment progress in real-time
3. Once complete, test your crew to ensure the changes are working as expected

<Tip>
  If you encounter any issues after updating, you can view deployment logs in the platform or contact support for assistance.
</Tip>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with updating your crew or troubleshooting deployment issues.
</Card>



# Zapier Trigger
Source: https://docs.crewai.com/en/enterprise/guides/zapier-trigger

Trigger CrewAI crews from Zapier workflows to automate cross-app workflows

This guide will walk you through the process of setting up Zapier triggers for CrewAI AMP, allowing you to automate workflows between CrewAI AMP and other applications.


## Prerequisites

* A CrewAI AMP account
* A Zapier account
* A Slack account (for this specific example)


## Step-by-Step Setup

<Steps>
  <Step title="Set Up the Slack Trigger">
    * In Zapier, create a new Zap.

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7602ce90ddcd4f0365fd821f4ff1ff2" alt="Zapier 1" data-og-width="621" width="621" data-og-height="463" height="463" data-path="images/enterprise/zapier-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3682030aedc56484321e678fe075bd97 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=cf755fd940ed2e79378b91369e620cd9 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e2fc3de247c9054220b0255a1544b160 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6f10592fc96a7ea63bbd8548328c8cea 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ab8d3cce86244b055400ad4ecf60d51d 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-1.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37b9df91c5efb53fd1d6c9a7fc34c624 2500w" />
    </Frame>
  </Step>

  <Step title="Choose Slack as your trigger app">
    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e5cdc5705b87b4e06178fa12fb5ef64b" alt="Zapier 2" data-og-width="670" width="670" data-og-height="684" height="684" data-path="images/enterprise/zapier-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f5d12f107504be7a7521ddf91d9ec413 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bebe1ccb4e8d4b4d077d4039b5a8c419 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=edb0a91b6ed81fc58470f998b3329978 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=262296a5be2e6762da49b77fcd9bd5e2 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=40b91cfb93939c2dd0b3f6222b376f90 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-2.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18bd414e6d18ec375cf94d94d2510775 2500w" />
    </Frame>

    * Select `New Pushed Message` as the Trigger Event.
    * Connect your Slack account if you haven't already.
  </Step>

  <Step title="Configure the CrewAI AMP Action">
    * Add a new action step to your Zap.
    * Choose CrewAI+ as your action app and Kickoff as the Action Event

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e52e2404a73623df30d125873bd8ff42" alt="Zapier 5" data-og-width="670" width="670" data-og-height="670" height="670" data-path="images/enterprise/zapier-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=786eec1ccf1fa275c710cd3f35d7c955 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bffb3ef5cd02ccd103a070893842ce2a 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=20c3a2004d6186a7217d6492f093dde5 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=3563e2fede93f6c678e6e25269a4781f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1641552fd6d8e6b477875ab53bd6f401 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-3.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=6c227ade8128df087cd958a98a398605 2500w" />
    </Frame>
  </Step>

  <Step title="Connect your CrewAI AMP account">
    * Connect your CrewAI AMP account.
    * Select the appropriate Crew for your workflow.

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=13aac37fdb67ee1c9f841a602ac3abf5" alt="Zapier 6" data-og-width="670" width="670" data-og-height="657" height="657" data-path="images/enterprise/zapier-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ad12e0febda29f3e6b68a245b83f17bd 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=08ff0773ed36f8fbb1c33acd90a50f79 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=cf788ee6daea3ef786b456c7a80d79a5 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b5a14e7f332b6ebef8131f6a26835417 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f0b27340ce1a510f990a305674d53107 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-4.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=061132e0ca03b82737f62cd4a113b12c 2500w" />
    </Frame>

    * Configure the inputs for the Crew using the data from the Slack message.
  </Step>

  <Step title="Format the CrewAI AMP Output">
    * Add another action step to format the text output from CrewAI AMP.
    * Use Zapier's formatting tools to convert the Markdown output to HTML.

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e772b4803dfffe4de12d9a7ea21484ce" alt="Zapier 8" data-og-width="670" width="670" data-og-height="674" height="674" data-path="images/enterprise/zapier-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d3de75f0a0d65af30620c7d9b89a1802 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=42ec43489c3e07aea4f64790efad63ef 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=68f473bd4c78acb0422d724a8dc9ac27 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d3149ba4fc03d00e00f81e6774dd4253 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ea05c3790b67091e18e32291c2ecceae 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-5.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a7519c4547a79061828c08d71091ac18 2500w" />
    </Frame>

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9fa4a34d5c511b6bb76f276348928699" alt="Zapier 9" data-og-width="670" width="670" data-og-height="675" height="675" data-path="images/enterprise/zapier-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=722c246b4c43b099734105a8c57e094c 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=91bfde61dfceb3998b85a0fd947b8f1b 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d56af89fb61384149deef33e22b57bfe 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d9097a2e0d8ddf13f0d17c7f65d4a263 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=59e5ad6b6f94117c4bdb264cde97a5ff 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-6.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=edf53161c63e0daf6e3e61abf1b1a265 2500w" />
    </Frame>
  </Step>

  <Step title="Send the Output via Email">
    * Add a final action step to send the formatted output via email.
    * Choose your preferred email service (e.g., Gmail, Outlook).
    * Configure the email details, including recipient, subject, and body.
    * Insert the formatted CrewAI AMP output into the email body.

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f3d2a0c67b29888cfdc5b0d81ba5c29b" alt="Zapier 7" data-og-width="670" width="670" data-og-height="673" height="673" data-path="images/enterprise/zapier-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=399cf0c5f81cbf170a3c8d4d8557b37f 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=8b6c488f27b8797c575a711f9b257b81 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f905970cb40554fe1c3674afa7f2209e 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=92ee968916226d374826eb358c264f66 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=1853357f43dd7032c890fd3a57fbd99e 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=9c5e507725c754d90937f0b7b1ee7699 2500w" />
    </Frame>
  </Step>

  <Step title="Kick Off the crew from Slack">
    * Enter the text in your Slack channel

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=916dbdffd171dc52c40ebc74cc39a38f" alt="Zapier 10" data-og-width="509" width="509" data-og-height="85" height="85" data-path="images/enterprise/zapier-7b.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=fce126149004d422a866d0e9ae00b9b0 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=c051b11bd9e2fd2db9a0fbd0997043cd 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=2f14112b9c9551239a1b82bd220b85fa 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f302f0da373ef859e49ca1b4a7540b94 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=386dfa4b1f1f4005e705771b39c1ec33 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-7b.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=57c6a7727031de0aebbdbeb65a03e27c 2500w" />
    </Frame>

    * Select the 3 ellipsis button and then chose Push to Zapier

    <Frame>
      <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=a6a6e2fd0b0b239af4c17ae1f34ad720" alt="Zapier 11" data-og-width="405" width="405" data-og-height="260" height="260" data-path="images/enterprise/zapier-8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e9bb5078ea66e8e7774b262caea53295 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=ec7f588235922fd96b8aea884cba1221 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d82c4c5d979814febba30bbfdeb2831d 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7a8f97770f17f96b4585c1b38b000fb8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=e8bae8057f2a294c977f7d568660f915 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/zapier-8.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=301cbedee7d42601db44f3710755653c 2500w" />
    </Frame>
  </Step>

  <Step title="Select the crew and then Push to Kick Off">
    <Frame>
      <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=eda865381d7121d38025c2b13abeccdf" alt="Zapier 12" data-og-width="659" width="659" data-og-height="531" height="531" data-path="images/enterprise/zapier-9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=283165c2ef289340b66aa9ed1719f97d 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d28641bc16596826f13a9d14ac0a2f2b 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e68731bab42671ec59dfd179c210bd80 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=234f5bffd3865f2a15d744455fef0c90 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d59b16a7bfbdf3b07d696ef70be0a31a 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/enterprise/zapier-9.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=1669d1af7e28868e5f260df18b36dd49 2500w" />
    </Frame>
  </Step>
</Steps>


## Tips for Success

* Ensure that your CrewAI AMP inputs are correctly mapped from the Slack message.
* Test your Zap thoroughly before turning it on to catch any potential issues.
* Consider adding error handling steps to manage potential failures in the workflow.

By following these steps, you'll have successfully set up Zapier triggers for CrewAI AMP, allowing for automated workflows triggered by Slack messages and resulting in email notifications with CrewAI AMP output.



# Asana Integration
Source: https://docs.crewai.com/en/enterprise/integrations/asana

Team task and project coordination with Asana integration for CrewAI.


## Overview

Enable your agents to manage tasks, projects, and team coordination through Asana. Create tasks, update project status, manage assignments, and streamline your team's workflow with AI-powered automation.


## Prerequisites

Before using the Asana integration, ensure you have:

* A [CrewAI AMP](https://app.crewai.com) account with an active subscription
* An Asana account with appropriate permissions
* Connected your Asana account through the [Integrations page](https://app.crewai.com/crewai_plus/connectors)


## Setting Up Asana Integration

### 1. Connect Your Asana Account

1. Navigate to [CrewAI AMP Integrations](https://app.crewai.com/crewai_plus/connectors)
2. Find **Asana** in the Authentication Integrations section
3. Click **Connect** and complete the OAuth flow
4. Grant the necessary permissions for task and project management
5. Copy your Enterprise Token from [Integration Settings](https://app.crewai.com/crewai_plus/settings/integrations)

### 2. Install Required Package

```bash  theme={null}
uv add crewai-tools
```

### 3. Environment Variable Setup

<Note>
  To use integrations with `Agent(apps=[])`, you must set the `CREWAI_PLATFORM_INTEGRATION_TOKEN` environment variable with your Enterprise Token.
</Note>

```bash  theme={null}
export CREWAI_PLATFORM_INTEGRATION_TOKEN="your_enterprise_token"
```

Or add it to your `.env` file:

```
CREWAI_PLATFORM_INTEGRATION_TOKEN=your_enterprise_token
```


## Available Actions

<AccordionGroup>
  <Accordion title="asana/create_comment">
    **Description:** Create a comment in Asana.

    **Parameters:**

    * `task` (string, required): Task ID - The ID of the Task the comment will be added to. The comment will be authored by the currently authenticated user.
    * `text` (string, required): Text (example: "This is a comment.").
  </Accordion>

  <Accordion title="asana/create_project">
    **Description:** Create a project in Asana.

    **Parameters:**

    * `name` (string, required): Name (example: "Stuff to buy").
    * `workspace` (string, required): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Projects in. Defaults to the user's first Workspace if left blank.
    * `team` (string, optional): Team - Use Connect Portal Workflow Settings to allow users to select which Team to share this Project with. Defaults to the user's first Team if left blank.
    * `notes` (string, optional): Notes (example: "These are things we need to purchase.").
  </Accordion>

  <Accordion title="asana/get_projects">
    **Description:** Get a list of projects in Asana.

    **Parameters:**

    * `archived` (string, optional): Archived - Choose "true" to show archived projects, "false" to display only active projects, or "default" to show both archived and active projects.
      * Options: `default`, `true`, `false`
  </Accordion>

  <Accordion title="asana/get_project_by_id">
    **Description:** Get a project by ID in Asana.

    **Parameters:**

    * `projectFilterId` (string, required): Project ID.
  </Accordion>

  <Accordion title="asana/create_task">
    **Description:** Create a task in Asana.

    **Parameters:**

    * `name` (string, required): Name (example: "Task Name").
    * `workspace` (string, optional): Workspace - Use Connect Portal Workflow Settings to allow users to select which Workspace to create Tasks in. Defaults to the user's first Workspace if left blank..
    * `project` (string, optional): Project - Use Connect Portal Workflow Settings to allow users to select which Project to create this Task in.
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

  <Accordion title="asana/update_task">
    **Description:** Update a task in Asana.

    **Parameters:**

    * `taskId` (string, required): Task ID - The ID of the Task that will be updated.
    * `completeStatus` (string, optional): Completed Status.
      * Options: `true`, `false`
    * `name` (string, optional): Name (example: "Task Name").
    * `notes` (string, optional): Notes.
    * `dueOnDate` (string, optional): Due On - The date on which this task is due. Cannot be used together with Due At. (example: "YYYY-MM-DD").
    * `dueAtDate` (string, optional): Due At - The date and time (ISO timestamp) at which this task is due. Cannot be used together with Due On. (example: "2019-09-15T02:06:58.147Z").
    * `assignee` (string, optional): Assignee - The ID of the Asana user this task will be assigned to. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `gid` (string, optional): External ID - An ID from your application to associate this task with. You can use this ID to sync updates to this task later.
  </Accordion>

  <Accordion title="asana/get_tasks">
    **Description:** Get a list of tasks in Asana.

    **Parameters:**

    * `workspace` (string, optional): Workspace - The ID of the Workspace to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Workspace.
    * `project` (string, optional): Project - The ID of the Project to filter tasks on. Use Connect Portal Workflow Settings to allow users to select a Project.
    * `assignee` (string, optional): Assignee - The ID of the assignee to filter tasks on. Use Connect Portal Workflow Settings to allow users to select an Assignee.
    * `completedSince` (string, optional): Completed since - Only return tasks that are either incomplete or that have been completed since this time (ISO or Unix timestamp). (example: "2014-04-25T16:15:47-04:00").
  </Accordion>

  <Accordion title="asana/get_tasks_by_id">
    **Description:** Get a list of tasks by ID in Asana.

    **Parameters:**

    * `taskId` (string, required): Task ID.
  </Accordion>

  <Accordion title="asana/get_task_by_external_id">
    **Description:** Get a task by external ID in Asana.

    **Parameters:**

    * `gid` (string, required): External ID - The ID that this task is associated or synced with, from your application.
  </Accordion>

  <Accordion title="asana/add_task_to_section">
    **Description:** Add a task to a section in Asana.

    **Parameters:**

    * `sectionId` (string, required): Section ID - The ID of the section to add this task to.
    * `taskId` (string, required): Task ID - The ID of the task. (example: "1204619611402340").
    * `beforeTaskId` (string, optional): Before Task ID - The ID of a task in this section that this task will be inserted before. Cannot be used with After Task ID. (example: "1204619611402340").
    * `afterTaskId` (string, optional): After Task ID - The ID of a task in this section that this task will be inserted after. Cannot be used with Before Task ID. (example: "1204619611402340").
  </Accordion>

  <Accordion title="asana/get_teams">
    **Description:** Get a list of teams in Asana.

    **Parameters:**

    * `workspace` (string, required): Workspace - Returns the teams in this workspace visible to the authorized user.
  </Accordion>

  <Accordion title="asana/get_workspaces">
    **Description:** Get a list of workspaces in Asana.

    **Parameters:** None required.
  </Accordion>
</AccordionGroup>


## Usage Examples

### Basic Asana Agent Setup

```python  theme={null}
from crewai import Agent, Task, Crew


---

**Navigation:** [← Previous](./06-website-rag-search.md) | [Index](./index.md) | [Next →](./08-create-an-agent-with-asana-capabilities.md)
