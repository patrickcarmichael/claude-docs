---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-step tool use

The model can execute more complex tasks in tool use – tasks that require tool calls to happen in a sequence. This is referred to as "multi-step" tool use.

Let's create a function to called `run_assistant` to implement these steps, and along the way, print out the key events and messages. Optionally, this function also accepts the chat history as an argument to keep the state in a multi-turn conversation.
```python PYTHON
model = "command-a-03-2025"

system_message = """## Task and Context

You are an assistant who assists new employees of Co1t with their first week. You respond to their questions and assist them with their needs. Today is Monday, June 24, 2024"""


def run_assistant(query, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    # Step 1: get user message

    print(f"Question:\n{query}")
    print("=" * 50)

    messages.append({"role": "user", "content": query})

    # Step 2: Generate tool calls (if any)

    response = co.chat(model=model, messages=messages, tools=tools)

    while response.message.tool_calls:

        print("Tool plan:")
        print(response.message.tool_plan, "\n")
        print("Tool calls:")
        for tc in response.message.tool_calls:
            print(
                f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
            )
        print("=" * 50)

        messages.append(
            {
                "role": "assistant",
                "tool_calls": response.message.tool_calls,
                "tool_plan": response.message.tool_plan,
            }
        )

        # Step 3: Get tool results

        for idx, tc in enumerate(response.message.tool_calls):
            tool_result = functions_map[tc.function.name](
                **json.loads(tc.function.arguments)
            )
            tool_content = []
            for data in tool_result:
                tool_content.append(
                    {
                        "type": "document",
                        "document": {"data": json.dumps(data)},
                    }
                )
                # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_content,
                }
            )

        # Step 4: Generate response and citations

        response = co.chat(
            model=model, messages=messages, tools=tools
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    # Print final response

    print("Response:")
    print(response.message.content[0].text)
    print("=" * 50)

    # Print citations (if any)

    if response.message.citations:
        print("\nCITATIONS:")
        for citation in response.message.citations:
            print(citation, "\n")

    return messages
```
To illustrate the concept of multi-step tool user, let's ask the assistant to block time for any lunch invites received in the email.

This requires tasks to happen over multiple steps in a sequence. Here, we see the assistant running these steps:

* First, it calls the `search_emails` tool to find any lunch invites, which it found one.
* Next, it calls the `create_calendar_event` tool to create an event to block the person's calendar on the day mentioned by the email.

This is also an example of tool use enabling a write operation instead of just a read operation that we saw with RAG.
```python PYTHON
messages = run_assistant(
    "Can you check if there are any lunch invites, and for those days, create a one-hour event on my calendar at 12PM."
)
```
```
Question:
Can you check if there are any lunch invites, and for those days, create a one-hour event on my calendar at 12PM.
==================================================
Tool plan:
I will first search the user's emails for lunch invites. Then, I will create a one-hour event on the user's calendar at 12PM for each day that the user has a lunch invite. 

Tool calls:
Tool name: search_emails | Parameters: {"query":"lunch invites"}
==================================================
Tool plan:
I have found one lunch invite for Thursday at noon. I will now create a one-hour event on the user's calendar for Thursday at noon. 

Tool calls:
Tool name: create_calendar_event | Parameters: {"date":"06/27/24","duration":1,"time":"12:00"}
==================================================
Response:
I found one lunch invite for Thursday, June 27, 2024. I have created a one-hour event on your calendar for that day at 12pm.
==================================================

CITATIONS:
start=29 end=53 text='Thursday, June 27, 2024.' sources=[ToolSource(type='tool', id='search_emails_1dxqzwragh9g:1', tool_output={'date': '2024-06-24', 'from': 'john@co1t.com', 'subject': 'First Week Check-In', 'text': "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!", 'to': 'david@co1t.com'})] 

start=71 end=85 text='one-hour event' sources=[ToolSource(type='tool', id='create_calendar_event_w11caj6hmqz2:0', tool_output={'content': '"is_success"'})] 

start=119 end=124 text='12pm.' sources=[ToolSource(type='tool', id='search_emails_1dxqzwragh9g:1', tool_output={'date': '2024-06-24', 'from': 'john@co1t.com', 'subject': 'First Week Check-In', 'text': "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!", 'to': 'david@co1t.com'})] 
```typescript
In this tutorial, you learned about:

* How to create tools
* How tool planning and calling happens
* How tool execution happens
* How to generate the response and citations
* How to run tool use in a multi-step scenario

And that concludes our 7-part Cohere tutorial. We hope that they have provided you with a foundational understanding of the Cohere API, the available models and endpoints, and the types of use cases that you can build with them.

To continue your learning, check out:

* [LLM University - A range of courses and step-by-step guides to help you start building](https://cohere.com/llmu)
* [Cookbooks - A collection of basic to advanced example applications](https://docs.cohere.com/page/cookbooks)
* [Cohere's documentation](https://docs.cohere.com/docs/the-cohere-platform)
* [The Cohere API reference](https://docs.cohere.com/reference/about)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
