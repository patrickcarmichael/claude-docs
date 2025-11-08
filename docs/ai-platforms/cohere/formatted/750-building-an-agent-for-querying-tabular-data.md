---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building an agent for querying tabular data

Next, let's create a `run_agent` function to run the agentic RAG workflow, the same as in Part 1.

The only change we are making here is to make the system message simpler and more specific since the agent now only has one tool.
```python PYTHON
system_message = """## Task and Context

ou are an assistant who helps developers analyze LLM application evaluation results from a CSV files."""
```
```python PYTHON
model = "command-a-03-2025"


def run_agent(query, messages=None):
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
        model=model, messages=messages, tools=tools, temperature=0.3
    )

    while response.message.tool_calls:

        print("TOOL PLAN:")
        print(response.message.tool_plan, "\n")
        print("TOOL CALLS:")
        for tc in response.message.tool_calls:
            if tc.function.name == "analyze_evaluation_results":
                print(f"Tool name: {tc.function.name}")
                tool_call_prettified = print(
                    "\n".join(
                        f"  {line}"
                        for line_num, line in enumerate(
                            json.loads(tc.function.arguments)[
                                "code"
                            ].splitlines()
                        )
                    )
                )
                print(tool_call_prettified)
            else:
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
            tool_content = [
                (
                    {
                        "type": "document",
                        "document": {"data": json.dumps(tool_result)},
                    }
                )
            ]

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
