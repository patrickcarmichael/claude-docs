---
title: "Langgraph Documentation Index"
description: "Navigation hub for Langgraph formatted documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Langgraph Documentation

Welcome to the formatted Langgraph documentation. This documentation is organized into sections for easy navigation.

## Available Formats

- **[📄 Full Documentation](./documentation.md)** - Complete documentation in one file
- **[📝 Original Source](../llms-full.txt)** - Original llms-full.txt file
- **[📦 Chunked Version](../chunked/index.md)** - Optimized chunks for LLM context

---

## Documentation Sections

### [Introduction](./00-introduction.md)

### [How to interact with the deployment using RemoteGraph](./01-how-to-interact-with-the-deployment-using-remotegr.md)

### [Initializing the graph](./02-initializing-the-graph.md)

### [Invoking the graph](./03-invoking-the-graph.md)

### [invoke the graph](./04-invoke-the-graph.md)

### [stream outputs from the graph](./05-stream-outputs-from-the-graph.md)

### [invoke the graph](./06-invoke-the-graph.md)

### [stream outputs from the graph](./07-stream-outputs-from-the-graph.md)

### [Thread-level persistence](./08-thread-level-persistence.md)

### [create a thread (or use an existing thread instead)](./09-create-a-thread-or-use-an-existing-thread-instead.md)

### [invoke the graph with the thread config](./10-invoke-the-graph-with-the-thread-config.md)

### [verify that the state was persisted to the thread](./11-verify-that-the-state-was-persisted-to-the-thread.md)

### [Using as a subgraph](./12-using-as-a-subgraph.md)

### [define parent graph](./13-define-parent-graph.md)

### [add remote graph directly as a node](./14-add-remote-graph-directly-as-a-node.md)

### [invoke the parent graph](./15-invoke-the-parent-graph.md)

### [stream outputs from both the parent graph and subgraph](./16-stream-outputs-from-both-the-parent-graph-and-subg.md)

### [How to integrate LangGraph with AutoGen, CrewAI, and other frameworks](./17-how-to-integrate-langgraph-with-autogen-crewai-and.md)

### [Prerequisites](./18-prerequisites.md)

### [Setup](./19-setup.md)

### [1. Define AutoGen agent](./20-1-define-autogen-agent.md)

### [2. Create the graph](./21-2-create-the-graph.md)

### [Create the graph with memory for persistence](./22-create-the-graph-with-memory-for-persistence.md)

### [Build the graph](./23-build-the-graph.md)

### [Compile with checkpointer for persistence](./24-compile-with-checkpointer-for-persistence.md)

### [3. Test the graph locally](./25-3-test-the-graph-locally.md)

### [pass the thread ID to persist agent outputs for future interactions](./26-pass-the-thread-id-to-persist-agent-outputs-for-fu.md)

### [4. Prepare for deployment](./27-4-prepare-for-deployment.md)

### [5. Deploy to LangGraph Platform](./28-5-deploy-to-langgraph-platform.md)

### [Enable tracing for your application](./29-enable-tracing-for-your-application.md)

### [Learn more](./30-learn-more.md)

### [How to use the graph API](./31-how-to-use-the-graph-api.md)

### [Setup](./32-setup.md)

### [Define and update state](./33-define-and-update-state.md)

### [Define the schema for the input](./34-define-the-schema-for-the-input.md)

### [Define the schema for the output](./35-define-the-schema-for-the-output.md)

### [Define the overall schema, combining both input and output](./36-define-the-overall-schema-combining-both-input-and.md)

### [Define the node that processes the input and generates an answer](./37-define-the-node-that-processes-the-input-and-gener.md)

### [Build the graph with input and output schemas specified](./38-build-the-graph-with-input-and-output-schemas-spec.md)

### [Invoke the graph with an input and print the result](./39-invoke-the-graph-with-an-input-and-print-the-resul.md)

### [The overall state of the graph (this is the public state shared across nodes)](./40-the-overall-state-of-the-graph-this-is-the-public-.md)

### [Output from node_1 contains private data that is not part of the overall state](./41-output-from-node_1-contains-private-data-that-is-n.md)

### [The private data is only shared between node_1 and node_2](./42-the-private-data-is-only-shared-between-node_1-and.md)

### [Node 2 input only requests the private data available after node_1](./43-node-2-input-only-requests-the-private-data-availa.md)

### [Node 3 only has access to the overall state (no access to private data from node_1)](./44-node-3-only-has-access-to-the-overall-state-no-acc.md)

### [Connect nodes in a sequence](./45-connect-nodes-in-a-sequence.md)

### [node_3 does not see the private data.](./46-node_3-does-not-see-the-private-data.md)

### [Invoke the graph with the initial state](./47-invoke-the-graph-with-the-initial-state.md)

### [The overall state of the graph (this is the public state shared across nodes)](./48-the-overall-state-of-the-graph-this-is-the-public-.md)

### [Build the state graph](./49-build-the-state-graph.md)

### [Test the graph with a valid input](./50-test-the-graph-with-a-valid-input.md)

### [Add runtime configuration](./51-add-runtime-configuration.md)

### [1. Specify config schema](./52-1-specify-config-schema.md)

### [2. Define a graph that accesses the config in a node](./53-2-define-a-graph-that-accesses-the-config-in-a-nod.md)

### [3. Pass in configuration at runtime:](./54-3-pass-in-configuration-at-runtime.md)

### [Add retry policies](./55-add-retry-policies.md)

### [Add node caching](./56-add-node-caching.md)

### [Create a sequence of steps](./57-create-a-sequence-of-steps.md)

### [Add nodes](./58-add-nodes.md)

### [Add edges](./59-add-edges.md)

### [Add nodes](./60-add-nodes.md)

### [Add edges](./61-add-edges.md)

### [Create branches](./62-create-branches.md)

### [Map-Reduce and the Send API](./63-map-reduce-and-the-send-api.md)

### [Call the graph: here we call it to generate a list of jokes](./64-call-the-graph-here-we-call-it-to-generate-a-list-.md)

### [Create and control loops](./65-create-and-control-loops.md)

### [Define nodes](./66-define-nodes.md)

### [Define edges](./67-define-edges.md)

### [Async](./68-async.md)

### [Combine control flow and state updates with `Command`](./69-combine-control-flow-and-state-updates-with-comman.md)

### [Define graph state](./70-define-graph-state.md)

### [Define the nodes](./71-define-the-nodes.md)

### [NOTE: there are no edges between nodes A, B and C!](./72-note-there-are-no-edges-between-nodes-a-b-and-c.md)

### [Visualize your graph](./73-visualize-your-graph.md)

### [Stream outputs](./74-stream-outputs.md)

### [Supported stream modes](./75-supported-stream-modes.md)

### [Stream from an agent](./76-stream-from-an-agent.md)

### [Stream from a workflow](./77-stream-from-a-workflow.md)

### [Use the functional API](./78-use-the-functional-api.md)

### [Creating a simple workflow](./79-creating-a-simple-workflow.md)

### [Parallel execution](./80-parallel-execution.md)

### [Calling graphs](./81-calling-graphs.md)

### [Call other entrypoints](./82-call-other-entrypoints.md)

### [Streaming](./83-streaming.md)

### [Retry policy](./84-retry-policy.md)

### [This variable is just used for demonstration purposes to simulate a network failure.](./85-this-variable-is-just-used-for-demonstration-purpo.md)

### [Let's configure the RetryPolicy to retry on ValueError.](./86-lets-configure-the-retrypolicy-to-retry-on-valueer.md)

### [Caching Tasks](./87-caching-tasks.md)

### [Resuming after an error](./88-resuming-after-an-error.md)

### [This variable is just used for demonstration purposes to simulate a network failure.](./89-this-variable-is-just-used-for-demonstration-purpo.md)

### [Initialize an in-memory checkpointer for persistence](./90-initialize-an-in-memory-checkpointer-for-persisten.md)

### [Workflow execution configuration with a unique thread identifier](./91-workflow-execution-configuration-with-a-unique-thr.md)

### [This invocation will take ~1 second due to the slow_task execution](./92-this-invocation-will-take-1-second-due-to-the-slow.md)

### [Human-in-the-loop](./93-human-in-the-loop.md)

### [Continue execution](./94-continue-execution.md)

### [Short-term memory](./95-short-term-memory.md)

### [Long-term memory](./96-long-term-memory.md)

### [Workflows](./97-workflows.md)

### [Agents](./98-agents.md)

### [Integrate with other libraries](./99-integrate-with-other-libraries.md)

### [Use subgraphs](./100-use-subgraphs.md)

### [Setup](./101-setup.md)

### [Shared state schemas](./102-shared-state-schemas.md)

### [Subgraph](./103-subgraph.md)

### [Parent graph](./104-parent-graph.md)

### [Different state schemas](./105-different-state-schemas.md)

### [Subgraph](./106-subgraph.md)

### [Parent graph](./107-parent-graph.md)

### [Add persistence](./108-add-persistence.md)

### [Subgraph](./109-subgraph.md)

### [Parent graph](./110-parent-graph.md)

### [View subgraph state](./111-view-subgraph-state.md)

### [Stream subgraph outputs](./112-stream-subgraph-outputs.md)

### [Build multi-agent systems](./113-build-multi-agent-systems.md)

### [Handoffs](./114-handoffs.md)

### [Build a multi-agent system](./115-build-a-multi-agent-system.md)

### [Handoffs](./116-handoffs.md)

### [Define agents](./117-define-agents.md)

### [Define multi-agent graph](./118-define-multi-agent-graph.md)

### [Multi-turn conversation](./119-multi-turn-conversation.md)

### [Prebuilt implementations](./120-prebuilt-implementations.md)

### [How to pass custom run ID or set tags and metadata for graph runs in LangSmith](./121-how-to-pass-custom-run-id-or-set-tags-and-metadata.md)

### [TLDR](./122-tldr.md)

### [Generate a random UUID -- it must be a UUID](./123-generate-a-random-uuid-it-must-be-a-uuid.md)

### [Works with all standard Runnable methods](./124-works-with-all-standard-runnable-methods.md)

### [Setup](./125-setup.md)

### [Define the graph](./126-define-the-graph.md)

### [First we initialize the model we want to use.](./127-first-we-initialize-the-model-we-want-to-use.md)

### [For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)](./128-for-this-tutorial-we-will-use-custom-tool-that-ret.md)

### [Define the graph](./129-define-the-graph.md)

### [Run your graph](./130-run-your-graph.md)

### [View the trace in LangSmith](./131-view-the-trace-in-langsmith.md)

### [Call tools](./132-call-tools.md)

### [Define a tool](./133-define-a-tool.md)

### [Run a tool](./134-run-a-tool.md)

### [Use in an agent](./135-use-in-an-agent.md)

### [Use in a workflow](./136-use-in-a-workflow.md)

### [Tool customization](./137-tool-customization.md)

### [Context management](./138-context-management.md)

### [Invocation example with an agent](./139-invocation-example-with-an-agent.md)

### [Example agent setup](./140-example-agent-setup.md)

### [Invocation: reads the name from state (initially empty)](./141-invocation-reads-the-name-from-state-initially-emp.md)

### [Advanced tool features](./142-advanced-tool-features.md)

### [Default error handling (enabled by default)](./143-default-error-handling-enabled-by-default.md)

### [Default error handling](./144-default-error-handling.md)

### [Prebuilt tools](./145-prebuilt-tools.md)

### [How to add cross-thread persistence (functional API)](./146-how-to-add-cross-thread-persistence-functional-api.md)

### [Setup](./147-setup.md)

### [Example: simple chatbot with long-term memory](./148-example-simple-chatbot-with-long-term-memory.md)

### [NOTE: we're passing the store object here when creating a workflow via entrypoint()](./149-note-were-passing-the-store-object-here-when-creat.md)

### [How to build a multi-agent network (functional API)](./150-how-to-build-a-multi-agent-network-functional-api.md)

### [Define a tool to signal intent to hand off to a different agent](./151-define-a-tool-to-signal-intent-to-hand-off-to-a-di.md)

### [define an agent](./152-define-an-agent.md)

### [define a task that calls an agent](./153-define-a-task-that-calls-an-agent.md)

### [define the multi-agent network workflow](./154-define-the-multi-agent-network-workflow.md)

### [Setup](./155-setup.md)

### [Travel agent example](./156-travel-agent-example.md)

### [Define travel advisor ReAct agent](./157-define-travel-advisor-react-agent.md)

### [Define hotel advisor ReAct agent](./158-define-hotel-advisor-react-agent.md)

### [How to add multi-turn conversation in a multi-agent application (functional API)](./159-how-to-add-multi-turn-conversation-in-a-multi-agen.md)

### [Define a tool to signal intent to hand off to a different agent](./160-define-a-tool-to-signal-intent-to-hand-off-to-a-di.md)

### [`workflow()` below handles the handoffs explicitly](./161-workflow-below-handles-the-handoffs-explicitly.md)

### [define an agent](./162-define-an-agent.md)

### [define a task that calls an agent](./163-define-a-task-that-calls-an-agent.md)

### [define the multi-agent network workflow](./164-define-the-multi-agent-network-workflow.md)

### [Setup](./165-setup.md)

### [%%capture --no-stderr](./166-capture-no-stderr.md)

### [Define travel advisor ReAct agent](./167-define-travel-advisor-react-agent.md)

### [Define hotel advisor ReAct agent](./168-define-hotel-advisor-react-agent.md)

### [Test multi-turn conversation](./169-test-multi-turn-conversation.md)

### [How to add thread-level persistence (functional API)](./170-how-to-add-thread-level-persistence-functional-api.md)

### [Setup](./171-setup.md)

### [Example: simple chatbot with short-term memory](./172-example-simple-chatbot-with-short-term-memory.md)

### [How to manage conversation history in a ReAct Agent](./173-how-to-manage-conversation-history-in-a-react-agen.md)

### [Setup](./174-setup.md)

### [Keep the original message history unmodified](./175-keep-the-original-message-history-unmodified.md)

### [This function will be added as a new node in ReAct agent graph](./176-this-function-will-be-added-as-a-new-node-in-react.md)

### [The messages returned by this function will be the input to the LLM.](./177-the-messages-returned-by-this-function-will-be-the.md)

### [Overwrite the original message history](./178-overwrite-the-original-message-history.md)

### [Summarizing message history](./179-summarizing-message-history.md)

### [How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks](./180-how-to-integrate-langgraph-functional-api-with-aut.md)

### [Setup](./181-setup.md)

### [Define AutoGen agent](./182-define-autogen-agent.md)

### [Create the workflow](./183-create-the-workflow.md)

### [add short-term memory for storing conversation history](./184-add-short-term-memory-for-storing-conversation-his.md)

### [Run the graph](./185-run-the-graph.md)

### [pass the thread ID to persist agent outputs for future interactions](./186-pass-the-thread-id-to-persist-agent-outputs-for-fu.md)

### [filename: fibonacci_range.py](./187-filename-fibonacci_rangepy.md)

### [How to handle large numbers of tools](./188-how-to-handle-large-numbers-of-tools.md)

### [Setup](./189-setup.md)

### [Define the tools](./190-define-the-tools.md)

### [Abbreviated list of S&P 500 companies for demonstration](./191-abbreviated-list-of-sp-500-companies-for-demonstra.md)

### [Create a tool for each company and store it in a registry with a unique UUID as the key](./192-create-a-tool-for-each-company-and-store-it-in-a-r.md)

### [Define the graph](./193-define-the-graph.md)

### [Define the state structure using TypedDict.](./194-define-the-state-structure-using-typeddict.md)

### [and a list of selected tool IDs.](./195-and-a-list-of-selected-tool-ids.md)

### [Retrieve all available tools from the tool registry.](./196-retrieve-all-available-tools-from-the-tool-registr.md)

### [The agent function processes the current state](./197-the-agent-function-processes-the-current-state.md)

### [The select_tools function selects tools based on the user's last message content.](./198-the-select_tools-function-selects-tools-based-on-t.md)

### [Repeating tool selection](./199-repeating-tool-selection.md)

### [Next steps](./200-next-steps.md)

### [How to create a ReAct agent from scratch](./201-how-to-create-a-react-agent-from-scratch.md)

### [Setup](./202-setup.md)

### [Create ReAct agent](./203-create-react-agent.md)

### [Define our tool node](./204-define-our-tool-node.md)

### [Define the node that calls the model](./205-define-the-node-that-calls-the-model.md)

### [Define the conditional edge that determines whether to continue or not](./206-define-the-conditional-edge-that-determines-whethe.md)

### [Define a new graph](./207-define-a-new-graph.md)

### [Define the two nodes we will cycle between](./208-define-the-two-nodes-we-will-cycle-between.md)

### [Set the entrypoint as `agent`](./209-set-the-entrypoint-as-agent.md)

### [We now add a conditional edge](./210-we-now-add-a-conditional-edge.md)

### [We now add a normal edge from `tools` to `agent`.](./211-we-now-add-a-normal-edge-from-tools-to-agent.md)

### [Now we can compile and visualize our graph](./212-now-we-can-compile-and-visualize-our-graph.md)

### [Use ReAct agent](./213-use-react-agent.md)

### [Helper function for formatting the stream nicely](./214-helper-function-for-formatting-the-stream-nicely.md)

### [How to force tool-calling agent to structure output](./215-how-to-force-tool-calling-agent-to-structure-outpu.md)

### [Setup](./216-setup.md)

### [Define model, tools, and graph state](./217-define-model-tools-and-graph-state.md)

### [Inherit 'messages' key from MessagesState, which is a list of chat messages](./218-inherit-messages-key-from-messagesstate-which-is-a.md)

### [Option 1: Bind output as tool](./219-option-1-bind-output-as-tool.md)

### [Force the model to use tools by passing tool_choice="any"](./220-force-the-model-to-use-tools-by-passing-tool_choic.md)

### [Define the function that calls the model](./221-define-the-function-that-calls-the-model.md)

### [Define the function that responds to the user](./222-define-the-function-that-responds-to-the-user.md)

### [Define the function that determines whether to continue or not](./223-define-the-function-that-determines-whether-to-con.md)

### [Define a new graph](./224-define-a-new-graph.md)

### [Define the two nodes we will cycle between](./225-define-the-two-nodes-we-will-cycle-between.md)

### [Set the entrypoint as `agent`](./226-set-the-entrypoint-as-agent.md)

### [We now add a conditional edge](./227-we-now-add-a-conditional-edge.md)

### [Option 2: 2 LLMs](./228-option-2-2-llms.md)

### [Define the function that calls the model](./229-define-the-function-that-calls-the-model.md)

### [Define the function that responds to the user](./230-define-the-function-that-responds-to-the-user.md)

### [Define the function that determines whether to continue or not](./231-define-the-function-that-determines-whether-to-con.md)

### [Define a new graph](./232-define-a-new-graph.md)

### [Define the two nodes we will cycle between](./233-define-the-two-nodes-we-will-cycle-between.md)

### [Set the entrypoint as `agent`](./234-set-the-entrypoint-as-agent.md)

### [We now add a conditional edge](./235-we-now-add-a-conditional-edge.md)

### [How to disable streaming for models that don't support it](./236-how-to-disable-streaming-for-models-that-dont-supp.md)

### [Without disabling streaming](./237-without-disabling-streaming.md)

### [Disabling streaming](./238-disabling-streaming.md)

### [How to create a ReAct agent from scratch (Functional API)](./239-how-to-create-a-react-agent-from-scratch-functiona.md)

### [Setup](./240-setup.md)

### [Create ReAct agent](./241-create-react-agent.md)

### [Usage](./242-usage.md)

### [Add thread-level persistence](./243-add-thread-level-persistence.md)

### [Assistants](./244-assistants.md)

### [Configuration](./245-configuration.md)

### [Versioning](./246-versioning.md)

### [Execution](./247-execution.md)

### [LangGraph Studio](./248-langgraph-studio.md)

### [Features](./249-features.md)

### [Learn more](./250-learn-more.md)

### [Double Texting](./251-double-texting.md)

### [Reject](./252-reject.md)

### [Enqueue](./253-enqueue.md)

### [Interrupt](./254-interrupt.md)

### [Rollback](./255-rollback.md)

### [LangGraph runtime](./256-langgraph-runtime.md)

### [Overview](./257-overview.md)

### [Actors](./258-actors.md)

### [Channels](./259-channels.md)

### [Examples](./260-examples.md)

### [High-level API](./261-high-level-api.md)

### [LangGraph Platform Plans](./262-langgraph-platform-plans.md)

### [Overview](./263-overview.md)

### [Plan Details](./264-plan-details.md)

### [Related](./265-related.md)

### [Template Applications](./266-template-applications.md)

### [Install the LangGraph CLI](./267-install-the-langgraph-cli.md)

### [Available Templates](./268-available-templates.md)

### [🌱 Create a LangGraph App](./269-create-a-langgraph-app.md)

### [Next Steps](./270-next-steps.md)

### [Tools](./271-tools.md)

### [Tool calling](./272-tool-calling.md)

### [-> AIMessage(tool_calls=[{'name': 'multiply', 'args': {'a': 2, 'b': 3}, ...}])](./273-aimessagetool_callsname-multiply-args-a-2-b-3.md)

### [Prebuilt tools](./274-prebuilt-tools.md)

### [Custom tools](./275-custom-tools.md)

### [Tool execution](./276-tool-execution.md)

### [Subgraphs](./277-subgraphs.md)

### [Cloud SaaS](./278-cloud-saas.md)

### [Overview](./279-overview.md)

### [Architecture](./280-architecture.md)

### [Components](./281-components.md)

### [Standalone Container](./282-standalone-container.md)

### [Overview](./283-overview.md)

### [Architecture](./284-architecture.md)

### [Compute Platforms](./285-compute-platforms.md)

### [Human-in-the-loop](./286-human-in-the-loop.md)

### [Key capabilities](./287-key-capabilities.md)

### [Patterns](./288-patterns.md)

### [MCP endpoint in LangGraph Server](./289-mcp-endpoint-in-langgraph-server.md)

### [Requirements](./290-requirements.md)

### [Exposing an agent as MCP tool](./291-exposing-an-agent-as-mcp-tool.md)

### [Define input schema](./292-define-input-schema.md)

### [Define output schema](./293-define-output-schema.md)

### [Combine input and output](./294-combine-input-and-output.md)

### [Define the processing node](./295-define-the-processing-node.md)

### [Build the graph with explicit schemas](./296-build-the-graph-with-explicit-schemas.md)

### [Run the graph](./297-run-the-graph.md)

### [Usage overview](./298-usage-overview.md)

### [Create server parameters for stdio connection](./299-create-server-parameters-for-stdio-connection.md)

### [Session behavior](./300-session-behavior.md)

### [Authentication](./301-authentication.md)

### [Disable MCP](./302-disable-mcp.md)

### [Self-Hosted Data Plane](./303-self-hosted-data-plane.md)

### [Requirements](./304-requirements.md)

### [Self-Hosted Data Plane](./305-self-hosted-data-plane.md)

### [Streaming](./306-streaming.md)

### [What’s possible with LangGraph streaming](./307-whats-possible-with-langgraph-streaming.md)

### [Functional API concepts](./308-functional-api-concepts.md)

### [Overview](./309-overview.md)

### [Functional API vs. Graph API](./310-functional-api-vs-graph-api.md)

### [Example](./311-example.md)

### [Entrypoint](./312-entrypoint.md)

### [Task](./313-task.md)

### [When to use a task](./314-when-to-use-a-task.md)

### [Serialization](./315-serialization.md)

### [Determinism](./316-determinism.md)

### [Idempotency](./317-idempotency.md)

### [Common Pitfalls](./318-common-pitfalls.md)

### [Deployment Options](./319-deployment-options.md)

### [Free deployment](./320-free-deployment.md)

### [Production deployment](./321-production-deployment.md)

### [Cloud SaaS](./322-cloud-saas.md)

### [Self-Hosted Data Plane](./323-self-hosted-data-plane.md)

### [Self-Hosted Control Plane](./324-self-hosted-control-plane.md)

### [Standalone Container](./325-standalone-container.md)

### [Related](./326-related.md)

### [LangGraph SDK](./327-langgraph-sdk.md)

### [Installation](./328-installation.md)

### [Python sync vs. async](./329-python-sync-vs-async.md)

### [Learn more](./330-learn-more.md)

### [LangGraph Server](./331-langgraph-server.md)

### [Application structure](./332-application-structure.md)

### [Parts of a deployment](./333-parts-of-a-deployment.md)

### [Learn more](./334-learn-more.md)

### [LangGraph Platform](./335-langgraph-platform.md)

### [Why use LangGraph Platform?](./336-why-use-langgraph-platform.md)

### [Tracing](./337-tracing.md)

### [Learn more](./338-learn-more.md)

### [Memory](./339-memory.md)

### [Short-term memory](./340-short-term-memory.md)

### [Long-term memory](./341-long-term-memory.md)

### [Node that *uses* the instructions](./342-node-that-uses-the-instructions.md)

### [Node that updates instructions](./343-node-that-updates-instructions.md)

### [InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.](./344-inmemorystore-saves-data-to-an-in-memory-dictionar.md)

### [get the "memory" by ID](./345-get-the-memory-by-id.md)

### [search for "memories" within this namespace, filtering on content equivalence, sorted by vector similarity](./346-search-for-memories-within-this-namespace-filterin.md)

### [Agent architectures](./347-agent-architectures.md)

### [Router](./348-router.md)

### [Tool-calling agent](./349-tool-calling-agent.md)

### [Custom agent architectures](./350-custom-agent-architectures.md)

### [Authentication & Access Control](./351-authentication-access-control.md)

### [Core Concepts](./352-core-concepts.md)

### [Default Security Models](./353-default-security-models.md)

### [System Architecture](./354-system-architecture.md)

### [Authentication](./355-authentication.md)

### [Authorization](./356-authorization.md)

### [Generic / global handler catches calls that aren't handled by more specific handlers](./357-generic-global-handler-catches-calls-that-arent-ha.md)

### [Matches the "thread" resource and all actions - create, read, update, delete, search](./358-matches-the-thread-resource-and-all-actions-create.md)

### [over the generic handler for all actions on the "threads" resource](./359-over-the-generic-handler-for-all-actions-on-the-th.md)

### [Thread creation. This will match only on thread create actions](./360-thread-creation-this-will-match-only-on-thread-cre.md)

### [it will take precedence for any "create" actions on the "threads" resources](./361-it-will-take-precedence-for-any-create-actions-on-.md)

### [Reading a thread. Since this is also more specific than the generic @auth.on handler, and the @auth.on.threads handler,](./362-reading-a-thread-since-this-is-also-more-specific-.md)

### [Run creation, streaming, updates, etc.](./363-run-creation-streaming-updates-etc.md)

### [Assistant creation](./364-assistant-creation.md)

### [Common Access Patterns](./365-common-access-patterns.md)

### [In your auth handler:](./366-in-your-auth-handler.md)

### [Supported Resources](./367-supported-resources.md)

### [Next Steps](./368-next-steps.md)

### [FAQ](./369-faq.md)

### [Do I need to use LangChain to use LangGraph? What’s the difference?](./370-do-i-need-to-use-langchain-to-use-langgraph-whats-.md)

### [How is LangGraph different from other agent frameworks?](./371-how-is-langgraph-different-from-other-agent-framew.md)

### [Does LangGraph impact the performance of my app?](./372-does-langgraph-impact-the-performance-of-my-app.md)

### [Is LangGraph open source? Is it free?](./373-is-langgraph-open-source-is-it-free.md)

### [How are LangGraph and LangGraph Platform different?](./374-how-are-langgraph-and-langgraph-platform-different.md)

### [Is LangGraph Platform open source?](./375-is-langgraph-platform-open-source.md)

### [Does LangGraph work with LLMs that don't support tool calling?](./376-does-langgraph-work-with-llms-that-dont-support-to.md)

### [Does LangGraph work with OSS LLMs?](./377-does-langgraph-work-with-oss-llms.md)

### [Can I use LangGraph Studio without logging in to LangSmith](./378-can-i-use-langgraph-studio-without-logging-in-to-l.md)

### [What does "nodes executed" mean for LangGraph Platform usage?](./379-what-does-nodes-executed-mean-for-langgraph-platfo.md)

### [MCP](./380-mcp.md)

### [Multi-agent systems](./381-multi-agent-systems.md)

### [Multi-agent architectures](./382-multi-agent-architectures.md)

### [this is the agent function that will be called as tool](./383-this-is-the-agent-function-that-will-be-called-as-.md)

### [the simplest way to build a supervisor w/ tool-calling is to use prebuilt ReAct agent graph](./384-the-simplest-way-to-build-a-supervisor-w-tool-call.md)

### [define team 1 (same as the single supervisor example above)](./385-define-team-1-same-as-the-single-supervisor-exampl.md)

### [define team 2 (same as the single supervisor example above)](./386-define-team-2-same-as-the-single-supervisor-exampl.md)

### [define top-level supervisor](./387-define-top-level-supervisor.md)

### [define the flow explicitly](./388-define-the-flow-explicitly.md)

### [Communication and state management](./389-communication-and-state-management.md)

### [Scalability & Resilience](./390-scalability-resilience.md)

### [Server scalability](./391-server-scalability.md)

### [Queue scalability](./392-queue-scalability.md)

### [Resilience](./393-resilience.md)

### [Postgres resilience](./394-postgres-resilience.md)

### [Redis resilience](./395-redis-resilience.md)

### [Graph API concepts](./396-graph-api-concepts.md)

### [Graphs](./397-graphs.md)

### [State](./398-state.md)

### [{'graph_output': 'My name is Lance'}](./399-graph_output-my-name-is-lance.md)

### [this is supported](./400-this-is-supported.md)

### [and this is also supported](./401-and-this-is-also-supported.md)

### [Nodes](./402-nodes.md)

### [You can then create edges to/from this node by referencing it as `"my_node"`](./403-you-can-then-create-edges-tofrom-this-node-by-refe.md)

### [Edges](./404-edges.md)

### [`Send`](./405-send.md)

### [`Command`](./406-command.md)

### [Graph Migrations](./407-graph-migrations.md)

### [Runtime Context](./408-runtime-context.md)

### [Visualization](./409-visualization.md)

### [LangGraph Control Plane](./410-langgraph-control-plane.md)

### [Control Plane UI](./411-control-plane-ui.md)

### [Control Plane API](./412-control-plane-api.md)

### [Control Plane Features](./413-control-plane-features.md)

### [Durable Execution](./414-durable-execution.md)

### [Requirements](./415-requirements.md)

### [Determinism and Consistent Replay](./416-determinism-and-consistent-replay.md)

### [Durability modes](./417-durability-modes.md)

### [Using tasks in nodes](./418-using-tasks-in-nodes.md)

### [Resuming Workflows](./419-resuming-workflows.md)

### [Starting Points for Resuming Workflows](./420-starting-points-for-resuming-workflows.md)

### [LangGraph Data Plane](./421-langgraph-data-plane.md)

### [Server Infrastructure](./422-server-infrastructure.md)

### ["Listener" Application](./423-listener-application.md)

### [Postgres](./424-postgres.md)

### [Redis](./425-redis.md)

### [Data Plane Features](./426-data-plane-features.md)

### [Overview](./427-overview.md)

### [Learn LangGraph basics](./428-learn-langgraph-basics.md)

### [Self-Hosted Control Plane](./429-self-hosted-control-plane.md)

### [Requirements](./430-requirements.md)

### [Self-Hosted Control Plane](./431-self-hosted-control-plane.md)

### [LangGraph CLI](./432-langgraph-cli.md)

### [Installation](./433-installation.md)

### [Commands](./434-commands.md)

### [Persistence](./435-persistence.md)

### [Threads](./436-threads.md)

### [Checkpoints](./437-checkpoints.md)

### [get the latest state snapshot](./438-get-the-latest-state-snapshot.md)

### [get a state snapshot for a specific checkpoint_id](./439-get-a-state-snapshot-for-a-specific-checkpoint_id.md)

### [Memory Store](./440-memory-store.md)

### [Find memories about food preferences](./441-find-memories-about-food-preferences.md)

### [Store with specific fields to embed](./442-store-with-specific-fields-to-embed.md)

### [Store without embedding (still retrievable, but not searchable)](./443-store-without-embedding-still-retrievable-but-not-.md)

### [We need this because we want to enable threads (conversations)](./444-we-need-this-because-we-want-to-enable-threads-con.md)

### [... Define the graph ...](./445-define-the-graph.md)

### [Compile the graph with the checkpointer and store](./446-compile-the-graph-with-the-checkpointer-and-store.md)

### [Invoke the graph](./447-invoke-the-graph.md)

### [First let's just say hi to the AI](./448-first-lets-just-say-hi-to-the-ai.md)

### [Invoke the graph](./449-invoke-the-graph.md)

### [Let's say hi again](./450-lets-say-hi-again.md)

### [Checkpointer libraries](./451-checkpointer-libraries.md)

### [... Define the graph ...](./452-define-the-graph.md)

### [Capabilities](./453-capabilities.md)

### [Application Structure](./454-application-structure.md)

### [Overview](./455-overview.md)

### [Key Concepts](./456-key-concepts.md)

### [File Structure](./457-file-structure.md)

### [Configuration File {#configuration-file-concepts}](./458-configuration-file-configuration-file-concepts.md)

### [Dependencies](./459-dependencies.md)

### [Graphs](./460-graphs.md)

### [Environment Variables](./461-environment-variables.md)

### [Time Travel ⏱️](./462-time-travel.md)

---

*Documentation formatted on 2025-11-08*
