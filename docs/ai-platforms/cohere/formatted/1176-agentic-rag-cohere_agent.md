---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Agentic RAG - cohere\_agent()

```python PYTHON
def cohere_agent(
    message: str,
    preamble: str,
    tools: list[dict],
    force_single_step=False,
    verbose: bool = False,
    temperature: float = 0.3,
) -> str:
    """
    Function to handle multi-step tool use api.

    Args:
        message (str): The message to send to the Cohere AI model.
        preamble (str): The preamble or context for the conversation.
        tools (list of dict): List of tools to use in the conversation.
        verbose (bool, optional): Whether to print verbose output. Defaults to False.

    Returns:
        str: The final response from the call.
    """

    counter = 1

    response = co.chat(
        model=COHERE_MODEL,
        message=message,
        preamble=preamble,
        tools=tools,
        force_single_step=force_single_step,
        temperature=temperature,
    )

    if verbose:
        print(f"\nrunning 0th step.")
        print(response.text)

    while response.tool_calls:
        tool_results = []

        if verbose:
            print(f"\nrunning {counter}th step.")

        for tool_call in response.tool_calls:
            output = functions_map[tool_call.name](**tool_call.parameters)
            outputs = [output]
            tool_results.append({"call": tool_call, "outputs": outputs})

            if verbose:
                print(
                    f"= running tool {tool_call.name}, with parameters: \n{tool_call.parameters}"
                )
                print(f"== tool results:")
                pprint(output)

        response = co.chat(
            model=COHERE_MODEL,
            message="",
            chat_history=response.chat_history,
            preamble=preamble,
            tools=tools,
            force_single_step=force_single_step,
            tool_results=tool_results,
            temperature=temperature,
        )

        if verbose:
            print(response.text)
            counter += 1

    return response.text
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
