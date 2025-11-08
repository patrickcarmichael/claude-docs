---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run agent

Now, let's set up the agent using Cohere's tool use feature. We can think of a tool use system as consisting of four components:

* The user
* The application
* The LLM
* The tools

At its most basic, these four components interact in a workflow through four steps:

* Step 1: Get user message. The LLM gets the user message (via the application).
* Step 2: Generate tool calls. The LLM makes a decision on the tools to call (if any) and generates the tool calls.
* Step 3: Get tool results. The application executes the tools and sends the tool results to the LLM.
* Step 4: Generate response and citations. The LLM generates the response and citations and sends them back to the user.

Let's create a function called `run_assistant` to implement these steps and print out the key events and messages along the way. This function also optionally accepts the chat history as an argument to keep the state in a multi-turn conversation.
```python PYTHON
import json

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

    response = co.chat(
        model="model",  # Pass a dummy string

        messages=messages,
        tools=tools,
    )

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
            model="model",  # Pass a dummy string

            messages=messages,
            tools=tools,
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
Let’s now run the agent. We'll use an example of a new hire asking about IT access and the travel expense process.

Given three tools to choose from, the model is able to pick the right tools (in this case, `search_faqs` and `search_emails`) based on what the user is asking for.

Also, notice that the model first generates a plan about what it should do ("I will ...") before actually generating the tool call(s).

Additionally, the model also generates fine-grained citations in tool use mode based on the tool results it receives, the same way we saw with RAG.
```python PYTHON
messages = run_assistant(
    "Any doc on how do I submit travel expenses? Also, any emails about setting up IT access?"
)
```
```mdx
Question:
Any doc on how do I submit travel expenses? Also, any emails about setting up IT access?
==================================================
Tool plan:
I will search for a document on how to submit travel expenses, and also search for emails about setting up IT access. 

Tool calls:
Tool name: search_faqs | Parameters: {"query":"how to submit travel expenses"}
Tool name: search_emails | Parameters: {"query":"setting up IT access"}
==================================================
Response:
You can submit your travel expenses through the user-friendly finance tool.

You should have received an email from it@co1t.com with instructions for setting up your IT access.
==================================================

CITATIONS:
start=48 end=75 text='user-friendly finance tool.' sources=[ToolSource(type='tool', id='search_faqs_wkfggn2680c4:0', tool_output={'text': 'Submitting Travel Expenses:\nSubmit your expenses through our user-friendly finance tool.'})] type='TEXT_CONTENT' 

start=105 end=176 text='email from it@co1t.com with instructions for setting up your IT access.' sources=[ToolSource(type='tool', id='search_emails_8n0cvsh5xknt:1', tool_output={'date': '2024-06-24', 'from': 'it@co1t.com', 'subject': 'Instructions for IT Setup', 'text': 'Welcome, David! To get you started, please follow the attached guide to set up your work accounts.', 'to': 'david@co1t.com'})] type='TEXT_CONTENT' 
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
