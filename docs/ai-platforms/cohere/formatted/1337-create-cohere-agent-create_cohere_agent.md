---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create Cohere Agent \[#create\_cohere\_agent]

As [Multi-Step Tool Use](https://docs.cohere.com/page/basic-multi-step) shows, you have a lot of flexiblity on how you can customize and interact with the cohere agent. Here I am creating a wrapper so that it automatically determines when to stop calling the tools and output final answer. It will run maximum of 15 steps.
```python PYTHON
def cohere_agent(
    message: str,
    preamble: str,
    tools: List[dict],
    force_single_step=False,
    verbose: bool = False,
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
                    f"= running tool {tool_call.name}, with parameters: {tool_call.parameters}"
                )
                print(f"== tool results: {outputs}")

        response = co.chat(
            model=COHERE_MODEL,
            message="",
            chat_history=response.chat_history,
            preamble=preamble,
            tools=tools,
            force_single_step=force_single_step,
            tool_results=tool_results,
        )

        if verbose:
            print(response.text)

            counter += 1

    return response.text


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
