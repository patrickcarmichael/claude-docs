---
title: "Crewai: Supported Events"
description: "Supported Events section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

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

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Webhook Format](./1491-webhook-format.md)

**Next:** [Triggers Overview →](./1493-triggers-overview.md)
