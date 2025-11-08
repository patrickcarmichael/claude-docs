---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## define the Agent

python_repl = PythonREPL()
python_tool = Tool(
    name="python_repl",
    description="Executes python code and returns the result. The code runs in a static sandbox without interactive mode, so print output or save output to a file.",
    func=python_repl.run,
)
python_tool.name = "python_interpreter"

class ToolInput(BaseModel):
    code: str = Field(description="Python code to execute.")
python_tool.args_schema = ToolInput
tools=[python_tool]

prompt = ChatPromptTemplate.from_template("{input}")
agent = create_cohere_react_agent(
   llm=llm,
   tools=tools,
   prompt=prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               return_intermediate_steps=True
                    )

preamble = """
You are an expert who answers the user's question in complete sentences. You are working with two pandas dataframe in Python. Ensure your output is a string.

Here is a preview of the `income_statement.csv` dataframe:
{table_1}

Here is a preview of the `balance_sheet.csv` dataframe:
{table_2}
""".format(table_1=income_statement.head(3).to_markdown(),table_2=balance_sheet.head(3).to_markdown())
```
We now define a new question.
```python PYTHON
question_dict ={
    'q1': ['what is the ratio of the largest stockholders equity to the smallest revenue'],
}
```
The answer to this question can be obtained only by accessing both the balance sheet and the income statement, as shown below:
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
