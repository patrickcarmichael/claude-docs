---
title: "Langgraph: Define hotel advisor ReAct agent"
description: "Define hotel advisor ReAct agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Define hotel advisor ReAct agent

hotel_advisor_tools = [get_hotel_recommendations, transfer_to_travel_advisor]
hotel_advisor = create_react_agent(
    model,
    hotel_advisor_tools,
    prompt=(
        "You are a hotel expert that can provide hotel recommendations for a given destination. "
        "If you need help picking travel destinations, ask 'travel_advisor' for help."
        "You MUST include human-readable response before transferring to another agent."
    ),
)

@task
def call_hotel_advisor(messages):
    response = hotel_advisor.invoke({"messages": messages})
    return response["messages"]

checkpointer = InMemorySaver()

def string_to_uuid(input_string):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, input_string))

@entrypoint(checkpointer=checkpointer)
def multi_turn_graph(messages, previous):
    previous = previous or []
    messages = add_messages(previous, messages)
    call_active_agent = call_travel_advisor
    while True:
        agent_messages = call_active_agent(messages).result()
        messages = add_messages(messages, agent_messages)
        # Find the last AI message
        # If one of the handoff tools is called, the last message returned
        # by the agent will be a ToolMessage because we set them to have
        # "return_direct=True". This means that the last AIMessage will
        # have tool calls.
        # Otherwise, the last returned message will be an AIMessage with
        # no tool calls, which means we are ready for new input.
        ai_msg = next(m for m in reversed(agent_messages) if isinstance(m, AIMessage))
        if not ai_msg.tool_calls:
            user_input = interrupt(value="Ready for user input.")
            # Add user input as a human message
            # NOTE: we generate unique ID for the human message based on its content
            # it's important, since on subsequent invocations previous user input (interrupt) values
            # will be looked up again and we will attempt to add them again here
            # `add_messages` deduplicates messages based on the ID, ensuring correct message history
            human_message = {
                "role": "user",
                "content": user_input,
                "id": string_to_uuid(user_input),
            }
            messages = add_messages(messages, [human_message])
            continue

        tool_call = ai_msg.tool_calls[-1]
        if tool_call["name"] == "transfer_to_hotel_advisor":
            call_active_agent = call_hotel_advisor
        elif tool_call["name"] == "transfer_to_travel_advisor":
            call_active_agent = call_travel_advisor
        else:
            raise ValueError(f"Expected transfer tool, got '{tool_call['name']}'")

    return entrypoint.final(value=agent_messages[-1], save=messages)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define travel advisor ReAct agent](./167-define-travel-advisor-react-agent.md)

**Next:** [Test multi-turn conversation →](./169-test-multi-turn-conversation.md)
