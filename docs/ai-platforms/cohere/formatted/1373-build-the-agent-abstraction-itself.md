---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Build the agent abstraction itself

def create_csv_agent(
    llm: BaseLanguageModel,
    path: Union[str, List[str]],
    extra_tools: List[BaseTool] = [],
    pandas_kwargs: Optional[dict] = None,
    prompt: Optional[ChatPromptTemplate] = None,
    number_of_head_rows: int = 5,
    verbose: bool = True,
    return_intermediate_steps: bool = True,
) -> AgentExecutor:
    """Create csv agent with the specified language model.

    Args:
        llm: Language model to use for the agent.
        path: A string path, or a list of string paths
            that can be read in as pandas DataFrames with pd.read_csv().
        number_of_head_rows: Number of rows to display in the prompt for sample data
        include_df_in_prompt: Display the DataFrame sample values in the prompt.
        pandas_kwargs: Named arguments to pass to pd.read_csv().
        prefix: Prompt prefix string.
        suffix: Prompt suffix string.
        prompt: Prompt to use for the agent. This takes precedence over the other prompt arguments, such as suffix and prefix.
        temp_path_dir: Temporary directory to store the csv files in for the python repl.
        delete_temp_path: Whether to delete the temporary directory after the agent is done. This only works if temp_path_dir is not provided.

    Returns:
        An AgentExecutor with the specified agent_type agent and access to
        a PythonREPL and any user-provided extra_tools.

    Example:
        .. code-block:: python

            from langchain_cohere import ChatCohere, create_csv_agent

            llm = ChatCohere(model="command-a-03-2025", temperature=0)
            agent_executor = create_csv_agent(
                llm,
                "titanic.csv"
            )
            resp = agent_executor.invoke({"input":"How many people were on the titanic?"})
            print(resp.get("output"))
    """  # noqa: E501

    try:
        import pandas as pd
    except ImportError:
        raise ImportError(
            "pandas package not found, please install with `pip install pandas`."
        )

    _kwargs = pandas_kwargs or {}
    if isinstance(path, (str)):
        df = pd.read_csv(path, **_kwargs)

    elif isinstance(path, list):
        df = []
        for item in path:
            if not isinstance(item, (str, IOBase)):
                raise ValueError(
                    f"Expected str or file-like object, got {type(path)}"
                )
            df.append(pd.read_csv(item, **_kwargs))
    else:
        raise ValueError(
            f"Expected str, list, or file-like object, got {type(path)}"
        )

    if not prompt:
        prompt = _get_prompt(path, number_of_head_rows)

    final_tools = [
        get_file_read_tool(),
        get_file_peek_tool(),
        get_python_tool(),
    ] + extra_tools
    if "preamble" in llm.__dict__ and not llm.__dict__.get(
        "preamble"
    ):
        llm = ChatCohere(**llm.__dict__)
        llm.preamble = CSV_PREAMBLE.format(
            current_date=datetime.now().strftime(
                "%A, %B %d, %Y %H:%M:%S"
            )
        )

    agent = create_tool_calling_agent(
        llm=llm, tools=final_tools, prompt=prompt
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=final_tools,
        verbose=verbose,
        return_intermediate_steps=return_intermediate_steps,
    )
    return agent_executor
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
