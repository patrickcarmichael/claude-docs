---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running an agentic RAG workflow

We create a `run_agent` function to run the agentic RAG workflow, the same as in Part 1. If you want further details on how to set up the tools, check out Part 1.
```python PYTHON
tools = [
    search_developer_docs_tool,
    search_internet_tool,
    search_code_examples_tool,
]
```
```python PYTHON
system_message = """## Task and Context

You are an assistant who helps developers use Cohere. You are equipped with a number of tools that can provide different types of information. If you can't find the information you need from one tool, you should try other tools if there is a possibility that they could provide the information you need."""
```
```python PYTHON
model = "command-a-03-2025"


def run_agent(query, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    # Step 1: get user message

    print(f"QUESTION:\n{query}")
    print("=" * 50)

    messages.append({"role": "user", "content": query})

    # Step 2: Generate tool calls (if any)

    response = co.chat(
        model=model, messages=messages, tools=tools, temperature=0.3
    )

    while response.message.tool_calls:

        print("TOOL PLAN:")
        print(response.message.tool_plan, "\n")
        print("TOOL CALLS:")
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

        for tc in response.message.tool_calls:
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
            model=model,
            messages=messages,
            tools=tools,
            temperature=0.3,
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    # Print final response

    print("RESPONSE:")
    print(response.message.content[0].text)
    print("=" * 50)

    # Print citations (if any)

    verbose_source = (
        False  # Change to True to display the contents of a source

    )
    if response.message.citations:
        print("CITATIONS:\n")
        for citation in response.message.citations:
            print(
                f"Start: {citation.start}| End:{citation.end}| Text:'{citation.text}' "
            )
            print("Sources:")
            for idx, source in enumerate(citation.sources):
                print(f"{idx+1}. {source.id}")
                if verbose_source:
                    print(f"{source.tool_output}")
            print("\n")

    return messages
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
