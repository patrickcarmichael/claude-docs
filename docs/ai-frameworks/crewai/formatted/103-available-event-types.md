---
title: "Crewai: Available Event Types"
description: "Available Event Types section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Available Event Types


CrewAI provides a wide range of events that you can listen for:

### Crew Events

* **CrewKickoffStartedEvent**: Emitted when a Crew starts execution
* **CrewKickoffCompletedEvent**: Emitted when a Crew completes execution
* **CrewKickoffFailedEvent**: Emitted when a Crew fails to complete execution
* **CrewTestStartedEvent**: Emitted when a Crew starts testing
* **CrewTestCompletedEvent**: Emitted when a Crew completes testing
* **CrewTestFailedEvent**: Emitted when a Crew fails to complete testing
* **CrewTrainStartedEvent**: Emitted when a Crew starts training
* **CrewTrainCompletedEvent**: Emitted when a Crew completes training
* **CrewTrainFailedEvent**: Emitted when a Crew fails to complete training

### Agent Events

* **AgentExecutionStartedEvent**: Emitted when an Agent starts executing a task
* **AgentExecutionCompletedEvent**: Emitted when an Agent completes executing a task
* **AgentExecutionErrorEvent**: Emitted when an Agent encounters an error during execution

### Task Events

* **TaskStartedEvent**: Emitted when a Task starts execution
* **TaskCompletedEvent**: Emitted when a Task completes execution
* **TaskFailedEvent**: Emitted when a Task fails to complete execution
* **TaskEvaluationEvent**: Emitted when a Task is evaluated

### Tool Usage Events

* **ToolUsageStartedEvent**: Emitted when a tool execution is started
* **ToolUsageFinishedEvent**: Emitted when a tool execution is completed
* **ToolUsageErrorEvent**: Emitted when a tool execution encounters an error
* **ToolValidateInputErrorEvent**: Emitted when a tool input validation encounters an error
* **ToolExecutionErrorEvent**: Emitted when a tool execution encounters an error
* **ToolSelectionErrorEvent**: Emitted when there's an error selecting a tool

### Knowledge Events

* **KnowledgeRetrievalStartedEvent**: Emitted when a knowledge retrieval is started
* **KnowledgeRetrievalCompletedEvent**: Emitted when a knowledge retrieval is completed
* **KnowledgeQueryStartedEvent**: Emitted when a knowledge query is started
* **KnowledgeQueryCompletedEvent**: Emitted when a knowledge query is completed
* **KnowledgeQueryFailedEvent**: Emitted when a knowledge query fails
* **KnowledgeSearchQueryFailedEvent**: Emitted when a knowledge search query fails

### LLM Guardrail Events

* **LLMGuardrailStartedEvent**: Emitted when a guardrail validation starts. Contains details about the guardrail being applied and retry count.
* **LLMGuardrailCompletedEvent**: Emitted when a guardrail validation completes. Contains details about validation success/failure, results, and error messages if any.

### Flow Events

* **FlowCreatedEvent**: Emitted when a Flow is created
* **FlowStartedEvent**: Emitted when a Flow starts execution
* **FlowFinishedEvent**: Emitted when a Flow completes execution
* **FlowPlotEvent**: Emitted when a Flow is plotted
* **MethodExecutionStartedEvent**: Emitted when a Flow method starts execution
* **MethodExecutionFinishedEvent**: Emitted when a Flow method completes execution
* **MethodExecutionFailedEvent**: Emitted when a Flow method fails to complete execution

### LLM Events

* **LLMCallStartedEvent**: Emitted when an LLM call starts
* **LLMCallCompletedEvent**: Emitted when an LLM call completes
* **LLMCallFailedEvent**: Emitted when an LLM call fails
* **LLMStreamChunkEvent**: Emitted for each chunk received during streaming LLM responses

### Memory Events

* **MemoryQueryStartedEvent**: Emitted when a memory query is started. Contains the query, limit, and optional score threshold.
* **MemoryQueryCompletedEvent**: Emitted when a memory query is completed successfully. Contains the query, results, limit, score threshold, and query execution time.
* **MemoryQueryFailedEvent**: Emitted when a memory query fails. Contains the query, limit, score threshold, and error message.
* **MemorySaveStartedEvent**: Emitted when a memory save operation is started. Contains the value to be saved, metadata, and optional agent role.
* **MemorySaveCompletedEvent**: Emitted when a memory save operation is completed successfully. Contains the saved value, metadata, agent role, and save execution time.
* **MemorySaveFailedEvent**: Emitted when a memory save operation fails. Contains the value, metadata, agent role, and error message.
* **MemoryRetrievalStartedEvent**: Emitted when memory retrieval for a task prompt starts. Contains the optional task ID.
* **MemoryRetrievalCompletedEvent**: Emitted when memory retrieval for a task prompt completes successfully. Contains the task ID, memory content, and retrieval execution time.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← In your crew.py or flow.py file](./102-in-your-crewpy-or-flowpy-file.md)

**Next:** [Event Handler Structure →](./104-event-handler-structure.md)
