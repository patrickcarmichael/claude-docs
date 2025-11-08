---
title: "Crewai: Streaming Responses"
description: "Streaming Responses section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Streaming Responses


CrewAI supports streaming responses from LLMs, allowing your application to receive and process outputs in real-time as they're generated.

<Tabs>
  <Tab title="Basic Setup">
    Enable streaming by setting the `stream` parameter to `True` when initializing your LLM:

    ```python  theme={null}
    from crewai import LLM

    # Create an LLM with streaming enabled
    llm = LLM(
        model="openai/gpt-4o",
        stream=True  # Enable streaming
    )
    ```

    When streaming is enabled, responses are delivered in chunks as they're generated, creating a more responsive user experience.
  </Tab>

  <Tab title="Event Handling">
    CrewAI emits events for each chunk received during streaming:

    ```python  theme={null}
    from crewai.events import (
      LLMStreamChunkEvent
    )
    from crewai.events import BaseEventListener

    class MyCustomListener(BaseEventListener):
        def setup_listeners(self, crewai_event_bus):
            @crewai_event_bus.on(LLMStreamChunkEvent)
            def on_llm_stream_chunk(self, event: LLMStreamChunkEvent):
              # Process each chunk as it arrives
              print(f"Received chunk: {event.chunk}")

    my_listener = MyCustomListener()
    ```

    <Tip>
      [Click here](https://docs.crewai.com/concepts/event-listener#event-listeners) for more details
    </Tip>
  </Tab>

  <Tab title="Agent & Task Tracking">
    All LLM events in CrewAI include agent and task information, allowing you to track and filter LLM interactions by specific agents or tasks:

    ```python  theme={null}
    from crewai import LLM, Agent, Task, Crew
    from crewai.events import LLMStreamChunkEvent
    from crewai.events import BaseEventListener

    class MyCustomListener(BaseEventListener):
        def setup_listeners(self, crewai_event_bus):
            @crewai_event_bus.on(LLMStreamChunkEvent)
            def on_llm_stream_chunk(source, event):
                if researcher.id == event.agent_id:
                    print("\n==============\n Got event:", event, "\n==============\n")

    my_listener = MyCustomListener()

    llm = LLM(model="gpt-4o-mini", temperature=0, stream=True)

    researcher = Agent(
        role="About User",
        goal="You know everything about the user.",
        backstory="""You are a master at understanding people and their preferences.""",
        llm=llm,
    )

    search = Task(
        description="Answer the following questions about the user: {question}",
        expected_output="An answer to the question.",
        agent=researcher,
    )

    crew = Crew(agents=[researcher], tasks=[search])

    result = crew.kickoff(
        inputs={"question": "..."}
    )
    ```

    <Info>
      This feature is particularly useful for:

      * Debugging specific agent behaviors
      * Logging LLM usage by task type
      * Auditing which agents are making what types of LLM calls
      * Performance monitoring of specific tasks
    </Info>
  </Tab>
</Tabs>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Provider Configuration Examples](./199-provider-configuration-examples.md)

**Next:** [Structured LLM Calls →](./201-structured-llm-calls.md)
