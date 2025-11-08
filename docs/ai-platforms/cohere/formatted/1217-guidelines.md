---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Guidelines

You are an expert who answers the user's question.
You have access to a vectorsearch tool that will use your query to search through documents and find the relevant answer.
You also have access to a python interpreter tool which you can use to run code for mathematical operations.
"""
        self.get_tools(rag_retriever)
        self.build_agent()

    def get_tools(self,rag_retriever):
        @tool
        def vectorsearch(query: str):
            """Uses the query to search through a list of documents and return the most relevant documents as well as the answer."""
            final_answer, final_answer_docs=rag_retriever.process_query(query)
            return final_answer + final_answer_docs
        vectorsearch.name = "vectorsearch" # use python case

        vectorsearch.description = "Uses the query to search through a list of documents and return the most relevant documents as well as the answer."
        class vectorsearch_inputs(BaseModel):
            query: str = Field(description="the users query")
        vectorsearch.args_schema = vectorsearch_inputs


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

        self.alltools = [vectorsearch,python_tool]

    def build_agent(self):
        # Prompt template

        prompt = ChatPromptTemplate.from_template("{input}")
        # Create the ReAct agent

        agent = create_cohere_react_agent(
            llm=self.llm,
            tools=self.alltools,
            prompt=prompt,
        )
        self.agent_executor = AgentExecutor(agent=agent, tools=self.alltools, verbose=True,return_intermediate_steps=True)


    def run_agent(self,query,history=None):
        if history:
            response=self.agent_executor.invoke({
            "input": query,
            "preamble": self.preamble,
            "chat_history": history
        })
        else:
            response=self.agent_executor.invoke({
            "input": query,
            "preamble": self.preamble,
        })
        return response
```
```python PYTHON
agent_object=react_agent(rag_retriever=rag_object)
```
```python PYTHON
step1_response=agent_object.run_agent("what are the charges for services in 2022 and 2023")
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will search for the charges for services in 2022 and 2023.
{'tool_name': 'vectorsearch', 'parameters': {'query': 'charges for services in 2022 and 2023'}}
[0m[36;1m[1;3mThe charges for services in 2022 were $5,266 million and in 2023 were $5,769 million.The final answer is from the documents below:

        [{'id': 'doc_0', 'snippet': 'Program and General Revenues FY 2023 FY 2022 FY 2021 Category (in millions) Charges for Services (CS) $5,769 $5,266 $5,669 Operating Grants and Contributions (OGC) 27,935 31,757 28,109 Capital Grants and Contributions (CGC) 657 656 675 Real Estate Taxes (RET) 31,502 29,507 31,421 Sales and Use Taxes (SUT) 10,577 10,106 7,614 Personal Income Taxes (PIT) 15,313 15,520 15,795 Income Taxes, Other (ITO) 13,181 9,521 9,499 Other Taxes* (OT) 3,680 3,777 2,755 Investment Income* (II) 694 151 226 Unrestricted Federal and State Aid (UFSA) 234 549 108 Other* (O) Total Program and General Revenues - Primary Government 2,305 $110,250 $107,535 $104,176 708 725', 'title': 'chunk 0'}][0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The charges for services in 2022 were $5,266 million and in 2023 were $5,769 million.
Grounded answer: The charges for services in <co: 0="">2022</co:> were <co: 0="">$5,266 million</co:> and in <co: 0="">2023</co:> were <co: 0="">$5,769 million</co:>.[0m

[1m> Finished chain.[0m
```
Just like earlier, we can also pass chat history to the LangChain agent to refer to for any other queries.
```python PYTHON
from langchain_core.messages import HumanMessage, AIMessage
```
```python PYTHON
chat_history=[
HumanMessage(content=step1_response['input']),
AIMessage(content=step1_response['output'])
]
```
```python PYTHON
agent_object.run_agent("what is the mean of the two values",history=chat_history)
```
```txt title="Output"
[1m> Entering new AgentExecutor chain...[0m


Python REPL can execute arbitrary code. Use with caution.


[32;1m[1;3m
I will use the Python Interpreter tool to calculate the mean of the two values.
{'tool_name': 'python_interpreter', 'parameters': {'code': 'import numpy as np\n\n# Data\nvalues = [5266, 5769]\n\n# Calculate the mean\nmean_value = np.mean(values)\n\nprint(f"The mean of the two values is: {mean_value:.0f} million")'}}

[0m[33;1m[1;3mThe mean of the two values is: 5518 million
[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: The mean of the two values is 5518 million.
Grounded answer: The mean of the two values is <co: 0="">5518 million</co:>.[0m

[1m> Finished chain.[0m
```
````python title="Output"
{'input': 'what is the mean of the two values',
'preamble': "\n## Task &amp; Context\nYou help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user's needs as best you can, which will be wide-ranging.\n\n## Style Guide\nUnless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.\n\n## Guidelines\nYou are an expert who answers the user's question. \nYou have access to a vectorsearch tool that will use your query to search through documents and find the relevant answer.\nYou also have access to a python interpreter tool which you can use to run code for mathematical operations.\n",

'chat_history': [HumanMessage(content='what are the charges for services in 2022 and 2023'),
AIMessage(content='The charges for services in 2022 were $5,266 million and in 2023 were $5,769 million.')],
'output': 'The mean of the two values is 5518 million.',
'citations': [CohereCitation(start=30, end=42, text='5518 million', documents=[{'output': 'The mean of the two values is: 5518 million\n'}])],
'intermediate_steps': [(AgentActionMessageLog(tool='python_interpreter', tool_input={'code': 'import numpy as np\n\n# Data\nvalues = [5266, 5769]\n\n# Calculate the mean\nmean_value = np.mean(values)\n\nprint(f"The mean of the two values is: {mean_value:.0f} million")'}, log='\nI will use the Python Interpreter tool to calculate the mean of the two values.\n{\'tool_name\': \'python_interpreter\', \'parameters\': {\'code\': \'import numpy as np\\n\\n# Data\\nvalues = [5266, 5769]\\n\\n# Calculate the mean\\nmean_value = np.mean(values)\\n\\nprint(f"The mean of the two values is: {mean_value:.0f} million")\'}}\n', message_log=[AIMessage(content='\nPlan: I will use the Python Interpreter tool to calculate the mean of the two values.\nAction: ```json\n[\n    {\n        "tool_name": "python_interpreter",\n        "parameters": {\n            "code": "import numpy as np\\n\\n# Data\\nvalues = [5266, 5769]\\n\\n# Calculate the mean\\nmean_value = np.mean(values)\\n\\nprint(f\\"The mean of the two values is: {mean_value:.0f} million\\")"\n        }\n    }\n]\n```')]),

'The mean of the two values is: 5518 million\n')]}
````

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
