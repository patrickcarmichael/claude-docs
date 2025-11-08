---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define tools that we want the csv agent to have access to


def get_file_peek_tool() -> Tool:
    def file_peek(filename: str, num_rows: int = 5) -> str:
        """Returns the first textual contents of an uploaded file

        Args:
            table_path: the table path
            num_rows: the number of rows of the table to preview.
        """  # noqa E501

        if ".csv" in filename:
            return pd.read_csv(filename).head(num_rows).to_markdown()
        else:
            return "the table_path was not recognised"

    class file_peek_inputs(BaseModel):
        filename: str = Field(
            description="The name of the attached file to show a peek preview."
        )

    file_peek_tool = Tool(
        name="file_peek",
        description="The name of the attached file to show a peek preview.",  # noqa E501

        func=file_peek,
        args_schema=file_peek_inputs,
    )

    return file_peek_tool


def get_file_read_tool() -> Tool:
    def file_read(filename: str) -> str:
        """Returns the textual contents of an uploaded file, broken up in text chunks

        Args:
            filename (str): The name of the attached file to read.
        """  # noqa E501

        if ".csv" in filename:
            return pd.read_csv(filename).to_markdown()
        else:
            return "the table_path was not recognised"

    class file_read_inputs(BaseModel):
        filename: str = Field(
            description="The name of the attached file to read."
        )

    file_read_tool = Tool(
        name="file_read",
        description="Returns the textual contents of an uploaded file, broken up in text chunks",  # noqa E501

        func=file_read,
        args_schema=file_read_inputs,
    )

    return file_read_tool


def get_python_tool() -> Tool:
    """Returns a tool that will execute python code and return the output."""

    def python_interpreter(code: str) -> str:
        """A function that will return the output of the python code.

        Args:
            code: the python code to run.
        """
        return python_repl.run(code)

    python_repl = PythonAstREPLTool()
    python_tool = Tool(
        name="python_interpreter",
        description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",  # noqa E501

        func=python_interpreter,
    )

    class PythonToolInput(BaseModel):
        code: str = Field(description="Python code to execute.")

    python_tool.args_schema = PythonToolInput
    return python_tool
```

### Create helper functions

In the cell below, we will create some important helper functions that we can call to properly assemble the full prompt that the csv agent can utilize.
```python
def create_prompt(
    system_message: Optional[BaseMessage] = SystemMessage(
        content="You are a helpful AI assistant."
    ),
    extra_prompt_messages: Optional[
        List[BaseMessagePromptTemplate]
    ] = None,
) -> ChatPromptTemplate:
    """Create prompt for this agent.

    Args:
        system_message: Message to use as the system message that will be the
            first in the prompt.
        extra_prompt_messages: Prompt messages that will be placed between the
            system message and the new human input.

    Returns:
        A prompt template to pass into this agent.
    """
    _prompts = extra_prompt_messages or []
    messages: List[Union[BaseMessagePromptTemplate, BaseMessage]]
    if system_message:
        messages = [system_message]
    else:
        messages = []

    messages.extend(
        [
            *_prompts,
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    return ChatPromptTemplate(messages=messages)


def _get_csv_head_str(path: str, number_of_head_rows: int) -> str:
    with open(path, "r") as file:
        lines = []
        for _ in range(number_of_head_rows):
            lines.append(file.readline().strip("\n"))
        # validate that the head contents are well formatted csv

        return " ".join(lines)


def _get_prompt(
    path: Union[str, List[str]], number_of_head_rows: int
) -> ChatPromptTemplate:
    if isinstance(path, str):
        lines = _get_csv_head_str(path, number_of_head_rows)
        prompt_message = f"The user uploaded the following attachments:\nFilename: {path}\nWord Count: {count_words_in_file(path)}\nPreview: {lines}"  # noqa: E501

    elif isinstance(path, list):
        prompt_messages = []
        for file_path in path:
            lines = _get_csv_head_str(file_path, number_of_head_rows)
            prompt_messages.append(
                f"The user uploaded the following attachments:\nFilename: {file_path}\nWord Count: {count_words_in_file(file_path)}\nPreview: {lines}"  # noqa: E501

            )
        prompt_message = " ".join(prompt_messages)

    prompt = create_prompt(
        system_message=HumanMessage(prompt_message)
    )
    return prompt


def count_words_in_file(file_path: str) -> int:
    try:
        with open(file_path, "r") as file:
            content = file.readlines()
            words = [len(sentence.split()) for sentence in content]
            return sum(words)
    except FileNotFoundError:
        print("File not found.")
        return 0
    except Exception as e:
        print("An error occurred:", str(e))
        return 0
```

### Build the core csv agent abstraction

The cells below outline the assembly of the various components to build an agent abstraction tailored for intelligent CSV file interactions. We use langchain to provide the agent that has access to the tools declared above, along with additional capabilities to provide additional tools if needed, and put together an agentic abstraction using the prompts defined earlier to deliver an abstraction that can easily be called for natural language querying over csv files!
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
